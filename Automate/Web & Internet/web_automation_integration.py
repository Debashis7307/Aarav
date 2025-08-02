#!/usr/bin/env python3
"""
Web Automation Integration for Aarav AI
Handles voice commands for web browsing tasks during conversation
"""

import webbrowser
import time
import os
import re
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup
import pyautogui
from datetime import datetime

class WebAutomationIntegration:
    def __init__(self):
        """Initialize web automation integration."""
        # Create screenshots directory if it doesn't exist
        self.screenshots_dir = "screenshots"
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        
        # Common website URLs for quick access
        self.websites = {
            'google': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'facebook': 'https://www.facebook.com',
            'instagram': 'https://www.instagram.com',
            'twitter': 'https://twitter.com',
            'linkedin': 'https://www.linkedin.com',
            'reddit': 'https://www.reddit.com',
            'amazon': 'https://www.amazon.com',
            'netflix': 'https://www.netflix.com',
            'spotify': 'https://open.spotify.com',
            'gmail': 'https://mail.google.com',
            'outlook': 'https://outlook.live.com',
            'yahoo': 'https://mail.yahoo.com',
            'wikipedia': 'https://www.wikipedia.org',
            'weather': 'https://weather.com',
            'maps': 'https://maps.google.com',
            'drive': 'https://drive.google.com',
            'calendar': 'https://calendar.google.com',
            'github': 'https://github.com',
            'stackoverflow': 'https://stackoverflow.com'
        }
        
        # Social media platforms
        self.social_media = {
            'facebook': 'https://www.facebook.com',
            'instagram': 'https://www.instagram.com',
            'twitter': 'https://twitter.com',
            'linkedin': 'https://www.linkedin.com',
            'reddit': 'https://www.reddit.com',
            'tiktok': 'https://www.tiktok.com',
            'snapchat': 'https://web.snapchat.com',
            'pinterest': 'https://www.pinterest.com',
            'telegram': 'https://web.telegram.org',
            'discord': 'https://discord.com/app'
        }
        
        # Music and video platforms
        self.media_platforms = {
            'youtube': 'https://www.youtube.com',
            'spotify': 'https://open.spotify.com',
            'netflix': 'https://www.netflix.com',
            'amazon prime': 'https://www.primevideo.com',
            'disney plus': 'https://www.disneyplus.com',
            'apple music': 'https://music.apple.com',
            'soundcloud': 'https://soundcloud.com',
            'vimeo': 'https://vimeo.com',
            'dailymotion': 'https://www.dailymotion.com'
        }
    
    def process_voice_command(self, command):
        """
        Process voice commands for web automation.
        
        Args:
            command (str): Voice command from user
            
        Returns:
            tuple: (success, response_message)
        """
        command_lower = command.lower().strip()
        
        # Tab management commands (check first)
        if self._is_tab_management_command(command_lower):
            return self._handle_tab_management_command(command_lower)
        
        # Screenshot commands
        elif self._is_screenshot_command(command_lower):
            return self._handle_screenshot_command(command_lower)
        
        # Open website commands
        elif self._is_open_website_command(command_lower):
            return self._handle_open_website_command(command_lower)
        
        # Search commands
        elif self._is_search_command(command_lower):
            return self._handle_search_command(command_lower)
        
        # Music/video commands
        elif self._is_media_command(command_lower):
            return self._handle_media_command(command_lower)
        
        # Social media commands
        elif self._is_social_media_command(command_lower):
            return self._handle_social_media_command(command_lower)
        
        # Email commands
        elif self._is_email_command(command_lower):
            return self._handle_email_command(command_lower)
        
        # Weather commands
        elif self._is_weather_command(command_lower):
            return self._handle_weather_command(command_lower)
        
        # Maps/navigation commands
        elif self._is_maps_command(command_lower):
            return self._handle_maps_command(command_lower)
        
        # Default response
        else:
            return False, "I didn't understand that web command. Try saying 'open Google', 'search for something', 'take screenshot', or 'close tab'"
    
    def _is_tab_management_command(self, command):
        """Check if command is for tab management."""
        tab_keywords = [
            'close tab', 'close the tab', 'close current tab', 'close this tab',
            'remove tab', 'remove the tab', 'remove current tab', 'remove this tab',
            'delete tab', 'delete the tab', 'delete current tab', 'delete this tab',
            'cross tab', 'cross the tab', 'cross current tab', 'cross this tab',
            'shut tab', 'shut the tab', 'shut current tab', 'shut this tab',
            'exit tab', 'exit the tab', 'exit current tab', 'exit this tab',
            'close browser', 'close the browser', 'close current browser',
            'close window', 'close the window', 'close current window'
        ]
        return any(keyword in command for keyword in tab_keywords)
    
    def _is_screenshot_command(self, command):
        """Check if command is for taking screenshots."""
        screenshot_keywords = [
            'screenshot', 'screen shot', 'capture screen', 'take screenshot',
            'take a screenshot', 'capture', 'snap', 'photo', 'picture',
            'save screen', 'screen capture', 'take picture', 'take photo'
        ]
        return any(keyword in command for keyword in screenshot_keywords)
    
    def _is_open_website_command(self, command):
        """Check if command is to open a website."""
        open_keywords = ['open', 'go to', 'navigate to', 'visit', 'launch', 'start']
        return any(keyword in command for keyword in open_keywords)
    
    def _is_search_command(self, command):
        """Check if command is a search request."""
        search_keywords = ['search', 'find', 'look for', 'search for']
        return any(keyword in command for keyword in search_keywords)
    
    def _is_media_command(self, command):
        """Check if command is for music/video."""
        media_keywords = ['play', 'music', 'video', 'song', 'watch', 'listen']
        return any(keyword in command for keyword in media_keywords)
    
    def _is_social_media_command(self, command):
        """Check if command is for social media."""
        social_keywords = ['facebook', 'instagram', 'twitter', 'linkedin', 'reddit', 'tiktok']
        return any(keyword in command for keyword in social_keywords)
    
    def _is_email_command(self, command):
        """Check if command is for email."""
        email_keywords = ['email', 'gmail', 'outlook', 'mail', 'yahoo']
        return any(keyword in command for keyword in email_keywords)
    
    def _is_weather_command(self, command):
        """Check if command is for weather."""
        weather_keywords = ['weather', 'temperature', 'forecast']
        return any(keyword in command for keyword in weather_keywords)
    
    def _is_maps_command(self, command):
        """Check if command is for maps/navigation."""
        maps_keywords = ['map', 'maps', 'location', 'directions', 'navigate']
        return any(keyword in command for keyword in maps_keywords)
    
    def _handle_tab_management_command(self, command):
        """Handle tab management commands."""
        try:
            # Use Ctrl+W to close the current tab
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.5)  # Small delay to ensure the action completes
            
            return True, "Current tab closed successfully!"
            
        except Exception as e:
            return False, f"Sorry, I couldn't close the tab. Error: {e}"
    
    def _handle_screenshot_command(self, command):
        """Handle screenshot commands."""
        try:
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            # Take screenshot
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            
            # Get file size for response
            file_size = os.path.getsize(filepath)
            file_size_kb = file_size / 1024
            
            return True, f"Screenshot captured and saved as '{filename}' ({file_size_kb:.1f} KB) in the screenshots folder!"
            
        except Exception as e:
            return False, f"Sorry, I couldn't take a screenshot. Error: {e}"
    
    def _handle_open_website_command(self, command):
        """Handle opening website commands."""
        # Extract website name from command
        for website, url in self.websites.items():
            if website in command:
                try:
                    webbrowser.open(url)
                    return True, f"Opening {website} for you!"
                except Exception as e:
                    return False, f"Sorry, I couldn't open {website}. Error: {e}"
        
        # If no specific website found, try to construct URL
        words = command.split()
        for word in words:
            if word not in ['open', 'go', 'to', 'navigate', 'visit', 'launch', 'start']:
                try:
                    url = f"https://www.{word}.com"
                    webbrowser.open(url)
                    return True, f"Opening {word} for you!"
                except:
                    continue
        
        return False, "I couldn't find that website. Try saying 'open Google' or 'open YouTube'"
    
    def _handle_search_command(self, command):
        """Handle search commands."""
        # Extract search query
        search_engines = {
            'google': 'https://www.google.com/search?q=',
            'youtube': 'https://www.youtube.com/results?search_query=',
            'bing': 'https://www.bing.com/search?q=',
            'duckduckgo': 'https://duckduckgo.com/?q='
        }
        
        # Determine search engine
        search_engine = 'google'  # default
        for engine in search_engines.keys():
            if engine in command:
                search_engine = engine
                break
        
        # Extract search query
        query = self._extract_search_query(command)
        if not query:
            return False, "What would you like me to search for?"
        
        try:
            search_url = search_engines[search_engine] + quote_plus(query)
            webbrowser.open(search_url)
            return True, f"Searching {search_engine} for '{query}'"
        except Exception as e:
            return False, f"Sorry, I couldn't perform the search. Error: {e}"
    
    def _handle_media_command(self, command):
        """Handle music/video commands."""
        # YouTube music/video commands
        if 'youtube' in command or 'video' in command:
            query = self._extract_search_query(command)
            if query:
                try:
                    search_url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
                    webbrowser.open(search_url)
                    return True, f"Searching YouTube for '{query}'"
                except Exception as e:
                    return False, f"Sorry, I couldn't search YouTube. Error: {e}"
            else:
                try:
                    webbrowser.open("https://www.youtube.com")
                    return True, "Opening YouTube for you!"
                except Exception as e:
                    return False, f"Sorry, I couldn't open YouTube. Error: {e}"
        
        # Spotify music commands
        elif 'spotify' in command or 'music' in command:
            query = self._extract_search_query(command)
            if query:
                try:
                    search_url = f"https://open.spotify.com/search/{quote_plus(query)}"
                    webbrowser.open(search_url)
                    return True, f"Searching Spotify for '{query}'"
                except Exception as e:
                    return False, f"Sorry, I couldn't search Spotify. Error: {e}"
            else:
                try:
                    webbrowser.open("https://open.spotify.com")
                    return True, "Opening Spotify for you!"
                except Exception as e:
                    return False, f"Sorry, I couldn't open Spotify. Error: {e}"
        
        # Netflix commands
        elif 'netflix' in command:
            try:
                webbrowser.open("https://www.netflix.com")
                return True, "Opening Netflix for you!"
            except Exception as e:
                return False, f"Sorry, I couldn't open Netflix. Error: {e}"
        
        # Generic play command
        elif 'play' in command:
            query = self._extract_search_query(command)
            if query:
                try:
                    # Try YouTube first for play commands
                    search_url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
                    webbrowser.open(search_url)
                    return True, f"Searching for '{query}' on YouTube"
                except Exception as e:
                    return False, f"Sorry, I couldn't search for that. Error: {e}"
        
        return False, "I didn't understand that media command. Try saying 'play music on YouTube' or 'open Spotify'"
    
    def _handle_social_media_command(self, command):
        """Handle social media commands."""
        for platform, url in self.social_media.items():
            if platform in command:
                try:
                    webbrowser.open(url)
                    return True, f"Opening {platform} for you!"
                except Exception as e:
                    return False, f"Sorry, I couldn't open {platform}. Error: {e}"
        
        return False, "I didn't recognize that social media platform. Try saying 'open Facebook' or 'open Instagram'"
    
    def _handle_email_command(self, command):
        """Handle email commands."""
        if 'gmail' in command or 'google mail' in command:
            try:
                webbrowser.open("https://mail.google.com")
                return True, "Opening Gmail for you!"
            except Exception as e:
                return False, f"Sorry, I couldn't open Gmail. Error: {e}"
        
        elif 'outlook' in command:
            try:
                webbrowser.open("https://outlook.live.com")
                return True, "Opening Outlook for you!"
            except Exception as e:
                return False, f"Sorry, I couldn't open Outlook. Error: {e}"
        
        elif 'yahoo' in command:
            try:
                webbrowser.open("https://mail.yahoo.com")
                return True, "Opening Yahoo Mail for you!"
            except Exception as e:
                return False, f"Sorry, I couldn't open Yahoo Mail. Error: {e}"
        
        else:
            try:
                webbrowser.open("https://mail.google.com")
                return True, "Opening Gmail for you!"
            except Exception as e:
                return False, f"Sorry, I couldn't open email. Error: {e}"
    
    def _handle_weather_command(self, command):
        """Handle weather commands."""
        try:
            webbrowser.open("https://weather.com")
            return True, "Opening weather information for you!"
        except Exception as e:
            return False, f"Sorry, I couldn't open weather information. Error: {e}"
    
    def _handle_maps_command(self, command):
        """Handle maps/navigation commands."""
        try:
            webbrowser.open("https://maps.google.com")
            return True, "Opening Google Maps for you!"
        except Exception as e:
            return False, f"Sorry, I couldn't open maps. Error: {e}"
    
    def _extract_search_query(self, command):
        """Extract search query from command."""
        # Remove common words and extract the search terms
        remove_words = [
            'search', 'for', 'find', 'look', 'play', 'on', 'in', 'at', 'the', 'a', 'an',
            'google', 'youtube', 'spotify', 'netflix', 'facebook', 'instagram', 'twitter',
            'music', 'video', 'song', 'watch', 'listen', 'open', 'go', 'to', 'navigate',
            'screenshot', 'screen', 'shot', 'capture', 'snap', 'photo', 'picture', 'save',
            'close', 'remove', 'delete', 'cross', 'shut', 'exit', 'tab', 'browser', 'window'
        ]
        
        words = command.split()
        query_words = [word for word in words if word.lower() not in remove_words]
        
        return ' '.join(query_words) if query_words else None

# Voice command patterns for integration
VOICE_COMMAND_PATTERNS = {
    'tab_management': [
        r'close\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?tab',
        r'remove\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?tab',
        r'delete\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?tab',
        r'cross\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?tab',
        r'shut\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?tab',
        r'close\s+(?:the\s+)?(?:current\s+)?(?:this\s+)?(?:browser|window)'
    ],
    'screenshot': [
        r'take\s+(?:a\s+)?screenshot',
        r'capture\s+(?:the\s+)?screen',
        r'screen\s+shot',
        r'take\s+(?:a\s+)?picture',
        r'take\s+(?:a\s+)?photo',
        r'snap\s+(?:a\s+)?screenshot',
        r'save\s+(?:the\s+)?screen'
    ],
    'open_website': [
        r'open\s+(\w+)',
        r'go\s+to\s+(\w+)',
        r'navigate\s+to\s+(\w+)',
        r'visit\s+(\w+)',
        r'launch\s+(\w+)'
    ],
    'search': [
        r'search\s+(?:for\s+)?(.+)',
        r'find\s+(?:me\s+)?(.+)',
        r'look\s+for\s+(.+)',
        r'search\s+google\s+(?:for\s+)?(.+)',
        r'search\s+youtube\s+(?:for\s+)?(.+)'
    ],
    'play_music': [
        r'play\s+(.+)',
        r'play\s+music\s+(?:on\s+)?(\w+)',
        r'play\s+(.+)?\s+on\s+youtube',
        r'play\s+(.+)?\s+on\s+spotify'
    ],
    'social_media': [
        r'open\s+(facebook|instagram|twitter|linkedin|reddit)',
        r'go\s+to\s+(facebook|instagram|twitter|linkedin|reddit)'
    ]
}

# Example usage and testing
def test_web_automation():
    """Test the web automation integration."""
    web_auto = WebAutomationIntegration()
    
    test_commands = [
        "take screenshot",
        "open Google",
        "search for Python programming",
        "play music on YouTube",
        "open Facebook",
        "open Gmail",
        "search YouTube for tutorials",
        "open weather",
        "open maps",
        "capture screen",
        "close tab",
        "remove current tab",
        "cross tab"
    ]
    
    print("Testing Web Automation Integration...")
    for command in test_commands:
        print(f"\nCommand: {command}")
        success, response = web_auto.process_voice_command(command)
        print(f"Response: {response}")

if __name__ == "__main__":
    test_web_automation() 