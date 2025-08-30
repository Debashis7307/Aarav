# 🌐 Web Scraping & Document Analysis Module

Advanced web scraping, document analysis, and information retrieval system for Aarav AI Assistant.

## 🚀 Features

### 🔍 **Web Content Analysis**
- **Smart Web Scraping**: Extract and analyze content from any website
- **Google Search Integration**: Search the internet and get summarized results
- **Content Summarization**: AI-powered summaries of web content
- **Multi-source Analysis**: Combine information from multiple sources

### 📄 **Document Processing**
- **PDF Analysis**: Advanced PDF document understanding using Gemini 2.0
- **Local & Remote Files**: Process PDFs from URLs or local files
- **Multi-document Analysis**: Compare and analyze multiple documents
- **Structure Preservation**: Understand charts, tables, and layouts

### 🌤️ **Real-time Information**
- **Weather Reports**: Current weather and forecasts for any location
- **News & Updates**: Latest information on any topic
- **Live Data Extraction**: Real-time web data retrieval

### 🎤 **Voice Integration**
- **Natural Commands**: Speak naturally to request information
- **Smart Intent Recognition**: Understands context and intent
- **Concise Responses**: AI-powered 3-4 sentence summaries optimized for voice
- **Contextual Summarization**: Responses tailored to your specific query

## 📋 Voice Commands

### 🔍 Search & Information
```
"Search for artificial intelligence news"
"Tell me about quantum computing from the internet"
"What is machine learning?"
"Find information about climate change"
"Look up the latest tech trends"
```

### 🌤️ Weather Information
```
"Current weather"
"Weather in New York"
"What's the temperature in London?"
"Weather forecast for tomorrow"
```

### 🌐 Website Analysis
```
"Analyze website github.com"
"Summarize reddit.com"
"Open and analyze news.ycombinator.com"
"Scrape content from example.com"
```

### 📄 Document Analysis
```
"Analyze document report.pdf"
"Read PDF https://example.com/document.pdf"
"Summarize the research paper"
"Compare these two documents"
```

## 🛠️ Installation

### 1. Install Dependencies
```bash
cd "Automate/Web & Internet"
pip install -r requirements.txt
```

### 2. Set Up API Keys
Add to your `brain/.env` file:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Test Installation
```bash
python web_scraper.py
python voice_web_integration.py
```

## 🎯 Usage Examples

### Basic Web Scraping
```python
from web_scraper import get_analyzer

analyzer = get_analyzer()

# Scrape and summarize a website
result = analyzer.scrape_website("https://example.com")
summary = analyzer.summarize_content(result['content'])
print(summary)
```

### Voice Command Processing
```python
from voice_web_integration import process_web_command

# Process voice commands
result = process_web_command("search for latest AI news")
print(result['response'])
```

### Document Analysis
```python
# Analyze PDF from URL
result = analyzer.analyze_pdf_from_url("https://example.com/document.pdf")
print(result['content'])

# Analyze local PDF
result = analyzer.analyze_local_pdf("path/to/document.pdf")
print(result['content'])
```

## 🔧 Technical Details

### Architecture
- **Modular Design**: Separate modules for scraping, analysis, and integration
- **Error Handling**: Robust error handling with fallbacks
- **Caching**: Intelligent content caching for performance
- **Rate Limiting**: Respectful web scraping with delays

### Data Processing
- **Content Extraction**: Smart content identification and extraction
- **Text Cleaning**: Advanced text preprocessing and cleaning
- **Summarization**: AI-powered content summarization
- **Structure Analysis**: Understanding of document layouts and formatting

### Integration
- **Voice Commands**: Seamless integration with Aarav's voice system
- **Intent Recognition**: Advanced natural language understanding
- **Response Generation**: Context-aware response creation

## 📊 Supported Formats

### Web Content
- ✅ HTML pages
- ✅ News articles
- ✅ Blog posts
- ✅ Documentation sites
- ✅ Social media content (limited)

### Documents
- ✅ PDF files (up to 1000 pages)
- ✅ Multi-page documents
- ✅ Documents with images and charts
- ✅ Scientific papers and reports

### Data Sources
- ✅ Any public website
- ✅ Search engines
- ✅ Weather services
- ✅ News sites
- ✅ Academic repositories

## 🎛️ Configuration

### Environment Variables
```bash
# Required
GEMINI_API_KEY=your_gemini_api_key

# Optional
OPENWEATHER_API_KEY=your_weather_api_key  # For enhanced weather
```

### Customization
- **User Agents**: Customizable browser headers
- **Timeout Settings**: Adjustable request timeouts
- **Content Limits**: Configurable content length limits
- **Summarization Prompts**: Custom AI prompts

## 🔒 Security & Ethics

### Respectful Scraping
- ✅ Rate limiting and delays
- ✅ Robots.txt compliance
- ✅ User-agent identification
- ✅ No aggressive scraping

### Privacy
- ✅ No data storage without permission
- ✅ Secure API key handling
- ✅ Local processing when possible

### Legal Compliance
- ✅ Public content only
- ✅ Fair use principles
- ✅ Attribution when required

## 🐛 Troubleshooting

### Common Issues

**"GEMINI_API_KEY not found"**
- Ensure API key is set in `brain/.env` file
- Check file permissions and location

**"Failed to scrape website"**
- Check internet connection
- Verify website is accessible
- Some sites may block automated access

**"PDF analysis failed"**
- Ensure PDF is publicly accessible
- Check file size (max 20MB for inline processing)
- Verify PDF is not password protected

### Debug Mode
```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🚀 Advanced Features

### Batch Processing
```python
# Process multiple URLs
urls = ["site1.com", "site2.com", "site3.com"]
for url in urls:
    result = analyzer.scrape_website(url)
    summary = analyzer.summarize_content(result['content'])
```

### Custom Prompts
```python
# Custom analysis prompts
custom_prompt = "Extract key statistics and findings from this research"
result = analyzer.analyze_pdf_from_url(pdf_url, custom_prompt)
```

### Multi-document Analysis
```python
# Compare multiple documents
doc1 = analyzer.analyze_pdf_from_url(url1)
doc2 = analyzer.analyze_pdf_from_url(url2)
comparison = analyzer.summarize_content(
    f"Document 1: {doc1['content']}\n\nDocument 2: {doc2['content']}",
    "Compare and contrast these two documents"
)
```

## 📈 Performance

- **Response Time**: 2-10 seconds for web scraping
- **Document Analysis**: 5-30 seconds depending on size
- **Concurrent Requests**: Limited to prevent overload
- **Memory Usage**: Optimized for large documents

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

## 📄 License

This module is part of the Aarav AI Assistant project and follows the same licensing terms.

---

## 🎉 Get Started

Ready to supercharge Aarav with web intelligence? 

1. Install dependencies
2. Set up API keys  
3. Start asking questions!

**Example**: *"Hey Aarav, tell me about the latest developments in artificial intelligence from the internet!"*

**Response**: *"AI companies achieved breakthrough performance in 2024 with new multimodal models combining text, images, and voice. Major developments include improved reasoning capabilities and 50% cost reductions in AI processing. Leading tech companies invested $200B+ in AI infrastructure this year. Based on 3 reliable sources."*

Your AI assistant is now ready to explore the entire web with concise, conversational responses! 🌐✨