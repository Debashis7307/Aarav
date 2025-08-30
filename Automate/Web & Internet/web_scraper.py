#!/usr/bin/env python3
"""
Web Scraping and Document Analysis Module for Aarav AI Assistant

This module provides comprehensive web scraping and document analysis capabilities:
- Web content scraping and summarization
- PDF document analysis and understanding
- Google search integration
- Weather information fetching
- Real-time data extraction and summarization

Features:
- Voice command integration
- Multiple data source support
- Intelligent content summarization
- Error handling and fallbacks
"""

import os
import sys
import requests
from bs4 import BeautifulSoup
import json
import io
import httpx
from pathlib import Path
from urllib.parse import urlparse, urljoin
from dotenv import load_dotenv
import time
import re

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("⚠️ Google Generative AI not installed. Install with: pip install google-generativeai")
    genai = None

# Load environment variables
load_dotenv()

class WebScraperAnalyzer:
    def __init__(self):
        """Initialize the web scraper and document analyzer."""
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
        
        # Initialize Gemini client
        if genai:
            self.client = genai.Client(api_key=self.gemini_api_key)
        else:
            self.client = None
            print("⚠️ Gemini client not available. Some features will be limited.")
        
        # Headers for web requests
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Common weather sites for weather information
        self.weather_sites = [
            'https://api.openweathermap.org/data/2.5/weather',
            'https://weather.com',
            'https://www.weather.gov'
        ]

    def google_search(self, query, num_results=5):
        """
        Perform a Google search and return top results.
        
        Args:
            query (str): Search query
            num_results (int): Number of results to return
            
        Returns:
            list: List of search results with titles, URLs, and snippets
        """
        try:
            # Simple Google search simulation using DuckDuckGo (to avoid API restrictions)
            search_url = f"https://duckduckgo.com/html/?q={query}"
            response = requests.get(search_url, headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []
                
                # Extract search results
                for result in soup.find_all('div', class_='result')[:num_results]:
                    title_elem = result.find('a', class_='result__a')
                    snippet_elem = result.find('a', class_='result__snippet')
                    
                    if title_elem:
                        title = title_elem.get_text().strip()
                        url = title_elem.get('href', '')
                        snippet = snippet_elem.get_text().strip() if snippet_elem else ""
                        
                        results.append({
                            'title': title,
                            'url': url,
                            'snippet': snippet
                        })
                
                return results
            
        except Exception as e:
            print(f"❌ Google search error: {e}")
            return []

    def scrape_website(self, url):
        """
        Scrape content from a website.
        
        Args:
            url (str): Website URL to scrape
            
        Returns:
            dict: Scraped content with title, text, and metadata
        """
        try:
            # Ensure URL has protocol
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header", "aside"]):
                script.decompose()
            
            # Extract title
            title = soup.find('title')
            title_text = title.get_text().strip() if title else "No title found"
            
            # Extract main content
            content_selectors = [
                'article', 'main', '.content', '.post-content', 
                '.entry-content', '.article-content', '.story-body'
            ]
            
            main_content = None
            for selector in content_selectors:
                main_content = soup.select_one(selector)
                if main_content:
                    break
            
            if not main_content:
                main_content = soup.find('body')
            
            # Extract text content
            if main_content:
                # Get all paragraphs and headings
                text_elements = main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div'])
                text_content = []
                
                for element in text_elements:
                    text = element.get_text().strip()
                    if text and len(text) > 20:  # Filter out short/empty texts
                        text_content.append(text)
                
                full_text = '\n\n'.join(text_content)
            else:
                full_text = soup.get_text()
            
            # Clean up text
            full_text = re.sub(r'\n\s*\n', '\n\n', full_text)
            full_text = re.sub(r'\s+', ' ', full_text).strip()
            
            return {
                'title': title_text,
                'url': url,
                'content': full_text[:5000],  # Limit content length
                'word_count': len(full_text.split()),
                'success': True
            }
            
        except Exception as e:
            return {
                'title': '',
                'url': url,
                'content': f"Error scraping website: {str(e)}",
                'word_count': 0,
                'success': False
            }

    def analyze_pdf_from_url(self, pdf_url, prompt="Summarize this document"):
        """
        Analyze a PDF document from a URL using Gemini.
        
        Args:
            pdf_url (str): URL of the PDF document
            prompt (str): Analysis prompt
            
        Returns:
            dict: Analysis results
        """
        if not self.client:
            return {
                'success': False,
                'content': "Gemini client not available for PDF analysis."
            }
        
        try:
            # Download PDF content
            doc_data = httpx.get(pdf_url, timeout=30).content
            
            # Analyze with Gemini
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[
                    types.Part.from_bytes(
                        data=doc_data,
                        mime_type='application/pdf',
                    ),
                    prompt
                ]
            )
            
            return {
                'success': True,
                'content': response.text,
                'source': pdf_url,
                'type': 'pdf_analysis'
            }
            
        except Exception as e:
            return {
                'success': False,
                'content': f"Error analyzing PDF: {str(e)}",
                'source': pdf_url
            }

    def analyze_local_pdf(self, file_path, prompt="Summarize this document"):
        """
        Analyze a local PDF document using Gemini.
        
        Args:
            file_path (str): Path to the PDF file
            prompt (str): Analysis prompt
            
        Returns:
            dict: Analysis results
        """
        if not self.client:
            return {
                'success': False,
                'content': "Gemini client not available for PDF analysis."
            }
        
        try:
            filepath = Path(file_path)
            if not filepath.exists():
                return {
                    'success': False,
                    'content': f"File not found: {file_path}"
                }
            
            # Analyze with Gemini
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[
                    types.Part.from_bytes(
                        data=filepath.read_bytes(),
                        mime_type='application/pdf',
                    ),
                    prompt
                ]
            )
            
            return {
                'success': True,
                'content': response.text,
                'source': file_path,
                'type': 'local_pdf_analysis'
            }
            
        except Exception as e:
            return {
                'success': False,
                'content': f"Error analyzing local PDF: {str(e)}",
                'source': file_path
            }

    def get_weather_info(self, location="current location"):
        """
        Fetch current weather information.
        
        Args:
            location (str): Location for weather info
            
        Returns:
            dict: Weather information
        """
        try:
            # Try to get weather from a simple API or scrape a weather site
            # For demo purposes, we'll scrape a weather site
            weather_query = f"current weather in {location}"
            search_results = self.google_search(weather_query, 3)
            
            weather_content = []
            for result in search_results:
                if any(weather_site in result['url'] for weather_site in ['weather.com', 'weather.gov', 'accuweather']):
                    scraped = self.scrape_website(result['url'])
                    if scraped['success']:
                        weather_content.append(scraped['content'][:1000])
            
            if weather_content:
                combined_content = '\n\n'.join(weather_content)
                
                # Summarize weather info with Gemini
                if self.client:
                    summary_response = self.client.models.generate_content(
                        model="gemini-2.0-flash-exp",
                        contents=[
                            f"Extract and summarize the current weather information for {location} in exactly 2-3 sentences. "
                            f"Include temperature, conditions, and key details only. Be concise and conversational.\n\n"
                            f"Content:\n{combined_content}"
                        ]
                    )
                    
                    return {
                        'success': True,
                        'content': summary_response.text,
                        'location': location,
                        'type': 'weather_info'
                    }
                else:
                    return {
                        'success': True,
                        'content': combined_content[:500],
                        'location': location,
                        'type': 'weather_info'
                    }
            else:
                return {
                    'success': False,
                    'content': f"Could not fetch weather information for {location}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'content': f"Error fetching weather: {str(e)}"
            }

    def summarize_content(self, content, prompt="Summarize this content", query_context=None):
        """
        Summarize content using Gemini with focus on conciseness and context.
        
        Args:
            content (str): Content to summarize
            prompt (str): Summarization prompt
            query_context (str): Original user query for contextual summarization
            
        Returns:
            str: Concise, contextual summary (3-4 lines)
        """
        if not self.client:
            return content[:300] + "..." if len(content) > 300 else content
        
        try:
            # Create a contextual prompt for concise summarization
            if query_context:
                enhanced_prompt = (
                    f"Based on the user's query about '{query_context}', provide a concise and highly relevant summary "
                    f"in exactly 3-4 sentences that directly answers their question. Focus only on the most important "
                    f"information that relates to their specific interest. Be conversational and informative.\n\n"
                    f"Content:\n{content}"
                )
            else:
                enhanced_prompt = (
                    f"Provide a clear and concise summary in exactly 3-4 sentences. Focus on the most important "
                    f"and relevant information. Be conversational and informative.\n\n"
                    f"Content:\n{content}"
                )
            
            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[enhanced_prompt]
            )
            
            # Ensure the response is concise (max 4 sentences)
            summary = response.text.strip()
            sentences = summary.split('. ')
            
            # Limit to 4 sentences maximum
            if len(sentences) > 4:
                summary = '. '.join(sentences[:4]) + '.'
            
            return summary
            
        except Exception as e:
            return f"Error summarizing content: {str(e)}"

    def process_user_request(self, user_input):
        """
        Process user requests for web scraping, document analysis, or information retrieval.
        
        Args:
            user_input (str): User's voice command or text input
            
        Returns:
            dict: Processing results with summary and metadata
        """
        user_input = user_input.lower().strip()
        
        # Determine request type
        if any(phrase in user_input for phrase in ['weather', 'temperature', 'forecast']):
            # Weather request
            location = "current location"
            if "in " in user_input:
                location = user_input.split("in ")[-1].strip()
            elif "for " in user_input:
                location = user_input.split("for ")[-1].strip()
            
            return self.get_weather_info(location)
        
        elif any(phrase in user_input for phrase in ['search', 'google', 'find', 'look up']):
            # Search request
            # Extract search query
            search_triggers = ['search for', 'google', 'find', 'look up', 'tell me about']
            query = user_input
            
            for trigger in search_triggers:
                if trigger in user_input:
                    query = user_input.split(trigger)[-1].strip()
                    break
            
            # Perform search and scrape top results
            search_results = self.google_search(query, 3)
            
            if search_results:
                # Scrape and summarize top results
                combined_content = []
                sources = []
                
                for result in search_results[:3]:
                    scraped = self.scrape_website(result['url'])
                    if scraped['success']:
                        combined_content.append(f"From {result['title']}: {scraped['content']}")
                        sources.append(result['url'])
                
                if combined_content:
                    full_content = '\n\n'.join(combined_content)
                    summary = self.summarize_content(
                        full_content, 
                        f"Provide a concise answer about '{query}' in 3-4 sentences based on this information. "
                        f"Focus on the most relevant and up-to-date information.",
                        query_context=query
                    )
                    
                    return {
                        'success': True,
                        'content': summary,
                        'sources': sources,
                        'query': query,
                        'type': 'search_results'
                    }
            
            return {
                'success': False,
                'content': f"Could not find reliable information about '{query}'"
            }
        
        elif 'pdf' in user_input or user_input.endswith('.pdf'):
            # PDF analysis request
            if user_input.startswith('http'):
                return self.analyze_pdf_from_url(user_input)
            else:
                return self.analyze_local_pdf(user_input)
        
        elif user_input.startswith('http') or '.' in user_input:
            # Direct website scraping
            scraped = self.scrape_website(user_input)
            if scraped['success']:
                summary = self.summarize_content(
                    scraped['content'],
                    "Provide a clear and informative summary of this website content in 3-4 sentences.",
                    query_context="website content analysis"
                )
                
                return {
                    'success': True,
                    'content': summary,
                    'source': scraped['url'],
                    'title': scraped['title'],
                    'type': 'website_summary'
                }
            else:
                return scraped
        
        else:
            # General information request
            query = user_input.replace('tell me about', '').strip()
            return self.process_user_request(f"search for {query}")

# Global analyzer instance
_analyzer = None

def get_analyzer():
    """Get or create the global analyzer instance."""
    global _analyzer
    if _analyzer is None:
        _analyzer = WebScraperAnalyzer()
    return _analyzer

def analyze_request(user_input):
    """
    Simple function to analyze user requests.
    
    Args:
        user_input (str): User's request
        
    Returns:
        dict: Analysis results
    """
    analyzer = get_analyzer()
    return analyzer.process_user_request(user_input)

def scrape_and_summarize(url, custom_prompt=None):
    """
    Scrape a website and provide a summary.
    
    Args:
        url (str): Website URL
        custom_prompt (str): Custom summarization prompt
        
    Returns:
        dict: Scraping and analysis results
    """
    analyzer = get_analyzer()
    scraped = analyzer.scrape_website(url)
    
    if scraped['success']:
        prompt = custom_prompt or "Provide a clear and informative summary of this content."
        summary = analyzer.summarize_content(scraped['content'], prompt)
        
        return {
            'success': True,
            'content': summary,
            'source': scraped['url'],
            'title': scraped['title'],
            'type': 'website_analysis'
        }
    else:
        return scraped

if __name__ == "__main__":
    # Test the analyzer
    analyzer = WebScraperAnalyzer()
    
    print("🔍 Testing Web Scraper and Document Analyzer...")
    print("=" * 50)
    
    # Test search functionality
    test_query = "artificial intelligence news"
    print(f"🔎 Testing search: '{test_query}'")
    results = analyzer.process_user_request(f"search for {test_query}")
    
    if results['success']:
        print(f"✅ Search successful!")
        print(f"📝 Summary: {results['content'][:200]}...")
    else:
        print(f"❌ Search failed: {results['content']}")
    
    print("\n🌤️ Testing weather functionality...")
    weather_results = analyzer.process_user_request("current weather")
    if weather_results['success']:
        print(f"✅ Weather info retrieved!")
        print(f"🌡️ Info: {weather_results['content'][:200]}...")
    else:
        print(f"❌ Weather failed: {weather_results['content']}")