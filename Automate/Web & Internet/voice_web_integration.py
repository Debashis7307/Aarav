#!/usr/bin/env python3
"""
Voice Command Integration for Web Scraping and Document Analysis

This module integrates the web scraping and document analysis capabilities
with Aarav's voice command system for seamless interaction.
"""

import os
import sys
import re
from typing import Dict, Any

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(project_root)

try:
    from Automate.Web_and_Internet.web_scraper import get_analyzer, analyze_request
except ImportError:
    from web_scraper import get_analyzer, analyze_request

class VoiceWebIntegration:
    def __init__(self):
        """Initialize voice-web integration."""
        self.analyzer = get_analyzer()
        
        # Voice command patterns for different functionalities
        self.command_patterns = {
            'search': [
                r'search (?:for )?(.+)',
                r'google (.+)',
                r'find (?:information about )?(.+)',
                r'look up (.+)',
                r'tell me about (.+) from (?:the )?internet',
                r'what is (.+)',
                r'who is (.+)',
                r'how (?:to )?(.+)',
                r'explain (.+)'
            ],
            'weather': [
                r'(?:current )?weather(?: in (.+))?',
                r'temperature(?: in (.+))?',
                r'forecast(?: for (.+))?',
                r'what\'s the weather(?: in (.+))?',
                r'how\'s the weather(?: in (.+))?'
            ],
            'website': [
                r'open (?:website )?(.+)',
                r'scrape (.+)',
                r'analyze (?:website )?(.+)',
                r'summarize (?:website )?(.+)',
                r'visit (.+)'
            ],
            'document': [
                r'analyze (?:document )?(.+\.pdf)',
                r'read (?:document )?(.+\.pdf)',
                r'summarize (?:document )?(.+\.pdf)',
                r'open (?:pdf )?(.+\.pdf)'
            ]
        }

    def _ensure_concise_response(self, text: str, max_sentences: int = 4) -> str:
        """
        Ensure response is concise and within sentence limits.
        
        Args:
            text (str): Original text
            max_sentences (int): Maximum number of sentences
            
        Returns:
            str: Concise text
        """
        text = text.strip()
        sentences = text.split('. ')
        
        if len(sentences) > max_sentences:
            # Take the first max_sentences and ensure proper ending
            concise_text = '. '.join(sentences[:max_sentences])
            if not concise_text.endswith('.'):
                concise_text += '.'
            return concise_text
        
        return text

    def parse_voice_command(self, command: str) -> Dict[str, Any]:
        """
        Parse voice command to determine intent and extract parameters.
        
        Args:
            command (str): Voice command from user
            
        Returns:
            dict: Parsed command with intent and parameters
        """
        command = command.lower().strip()
        
        # Remove common voice command prefixes
        prefixes_to_remove = [
            'aarav', 'hey aarav', 'please', 'can you', 'could you',
            'would you', 'i want to', 'i need to', 'help me'
        ]
        
        for prefix in prefixes_to_remove:
            if command.startswith(prefix):
                command = command[len(prefix):].strip()
        
        # Check each command pattern
        for intent, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, command)
                if match:
                    extracted_text = match.group(1) if match.groups() else command
                    
                    return {
                        'intent': intent,
                        'extracted_text': extracted_text.strip() if extracted_text else '',
                        'original_command': command,
                        'confidence': 0.9  # High confidence for pattern matches
                    }
        
        # Fallback: treat as search if no specific pattern matches
        return {
            'intent': 'search',
            'extracted_text': command,
            'original_command': command,
            'confidence': 0.6  # Lower confidence for fallback
        }

    def process_voice_command(self, command: str) -> Dict[str, Any]:
        """
        Process a voice command and return appropriate response.
        
        Args:
            command (str): Voice command from user
            
        Returns:
            dict: Response with content and metadata
        """
        parsed = self.parse_voice_command(command)
        intent = parsed['intent']
        extracted_text = parsed['extracted_text']
        
        try:
            if intent == 'weather':
                location = extracted_text if extracted_text else "current location"
                result = self.analyzer.get_weather_info(location)
                
                if result['success']:
                    content = self._ensure_concise_response(result['content'], 3)
                    return {
                        'success': True,
                        'response': content,
                        'type': 'weather',
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'response': f"Sorry, I couldn't get weather information for {location}. {result['content']}",
                        'type': 'weather_error'
                    }
            
            elif intent == 'search':
                if not extracted_text:
                    return {
                        'success': False,
                        'response': "I need something to search for. Please tell me what you'd like to know about.",
                        'type': 'search_error'
                    }
                
                result = self.analyzer.process_user_request(f"search for {extracted_text}")
                
                if result['success']:
                    # Format the response to be more conversational and concise
                    sources_info = ""
                    if 'sources' in result and result['sources']:
                        sources_info = f" Based on {len(result['sources'])} reliable sources."
                    
                    content = self._ensure_concise_response(result['content'], 4)
                    
                    return {
                        'success': True,
                        'response': f"{content}{sources_info}",
                        'type': 'search_results',
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'response': f"Sorry, I couldn't find reliable information about {extracted_text}. {result['content']}",
                        'type': 'search_error'
                    }
            
            elif intent == 'website':
                if not extracted_text:
                    return {
                        'success': False,
                        'response': "Please specify which website you'd like me to analyze.",
                        'type': 'website_error'
                    }
                
                # Ensure URL format
                url = extracted_text
                if not url.startswith(('http://', 'https://')):
                    if '.' in url:
                        url = 'https://' + url
                    else:
                        # Treat as search if not a clear URL
                        return self.process_voice_command(f"search for {extracted_text}")
                
                scraped = self.analyzer.scrape_website(url)
                
                if scraped['success']:
                    summary = self.analyzer.summarize_content(
                        scraped['content'],
                        "Provide a clear and informative summary of this website content in 3-4 sentences.",
                        query_context=f"website analysis for {extracted_text}"
                    )
                    
                    summary = self._ensure_concise_response(summary, 4)
                    
                    return {
                        'success': True,
                        'response': summary,
                        'type': 'website_summary',
                        'data': {
                            'title': scraped['title'],
                            'url': scraped['url'],
                            'content': summary
                        }
                    }
                else:
                    return {
                        'success': False,
                        'response': f"Sorry, I couldn't access or analyze that website. {scraped['content']}",
                        'type': 'website_error'
                    }
            
            elif intent == 'document':
                if not extracted_text:
                    return {
                        'success': False,
                        'response': "Please specify which document you'd like me to analyze.",
                        'type': 'document_error'
                    }
                
                # Check if it's a URL or local file
                if extracted_text.startswith(('http://', 'https://')):
                    result = self.analyzer.analyze_pdf_from_url(extracted_text)
                else:
                    result = self.analyzer.analyze_local_pdf(extracted_text)
                
                if result['success']:
                    return {
                        'success': True,
                        'response': f"Here's the analysis of the document: {result['content']}",
                        'type': 'document_analysis',
                        'data': result
                    }
                else:
                    return {
                        'success': False,
                        'response': f"Sorry, I couldn't analyze that document. {result['content']}",
                        'type': 'document_error'
                    }
            
            else:
                # Fallback to search
                return self.process_voice_command(f"search for {extracted_text}")
                
        except Exception as e:
            return {
                'success': False,
                'response': f"Sorry, I encountered an error while processing your request: {str(e)}",
                'type': 'system_error',
                'error': str(e)
            }

    def get_quick_help(self) -> str:
        """Return quick help text for voice commands."""
        return """
🌐 Web & Internet Commands:

🔍 Search & Information:
• "Search for [topic]" or "Tell me about [topic]"
• "What is [something]" or "Who is [someone]"
• "Find information about [topic]"

🌤️ Weather:
• "Current weather" or "Weather in [location]"
• "What's the temperature?"
• "Weather forecast for [city]"

📄 Website Analysis:
• "Open [website.com]" or "Analyze [website]"
• "Summarize [website]"
• "Scrape [website URL]"

📋 Document Analysis:
• "Analyze document [file.pdf]"
• "Read PDF [file path or URL]"
• "Summarize document [file]"

Examples:
• "Tell me about artificial intelligence from the internet"
• "Current weather in New York"
• "Analyze website github.com"
• "Search for latest tech news"
        """

# Global integration instance
_integration = None

def get_integration():
    """Get or create the global integration instance."""
    global _integration
    if _integration is None:
        _integration = VoiceWebIntegration()
    return _integration

def process_web_command(command: str) -> Dict[str, Any]:
    """
    Simple function to process web-related voice commands.
    
    Args:
        command (str): Voice command
        
    Returns:
        dict: Processing results
    """
    integration = get_integration()
    return integration.process_voice_command(command)

def is_web_command(command: str) -> bool:
    """
    Check if a command is web/internet related.
    
    Args:
        command (str): Voice command
        
    Returns:
        bool: True if web-related
    """
    web_keywords = [
        'search', 'google', 'find', 'look up', 'tell me about',
        'weather', 'temperature', 'forecast',
        'website', 'open', 'analyze', 'scrape', 'visit',
        'document', 'pdf', 'read', 'summarize',
        'internet', 'web', 'online', 'from the internet'
    ]
    
    command_lower = command.lower()
    return any(keyword in command_lower for keyword in web_keywords)

if __name__ == "__main__":
    # Test the integration
    integration = VoiceWebIntegration()
    
    print("🎤 Testing Voice-Web Integration...")
    print("=" * 50)
    
    test_commands = [
        "search for latest AI news",
        "current weather",
        "tell me about Python programming from the internet",
        "what's the weather in London",
        "analyze website example.com"
    ]
    
    for command in test_commands:
        print(f"\n🗣️ Command: '{command}'")
        parsed = integration.parse_voice_command(command)
        print(f"📝 Parsed: Intent={parsed['intent']}, Text='{parsed['extracted_text']}'")
        
        # Uncomment to test actual processing (requires API keys)
        # result = integration.process_voice_command(command)
        # print(f"🤖 Response: {result['response'][:100]}...")
    
    print(f"\n📚 Help text:\n{integration.get_quick_help()}")