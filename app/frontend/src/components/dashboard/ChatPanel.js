import React, { useState, useEffect, useRef } from "react";
import { Card } from "../ui/card";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Avatar } from "../ui/avatar";
import { Badge } from "../ui/badge";
import { 
  MessageSquare, 
  Send, 
  Mic, 
  MicOff, 
  Volume2, 
  VolumeX,
  User,
  Bot,
  Circle,
  Zap
} from "lucide-react";

const ChatPanel = () => {
  const [message, setMessage] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'system',
      content: 'AARAV AI Assistant initialized successfully',
      timestamp: '14:30:15',
      sender: 'system'
    },
    {
      id: 2,
      type: 'ai',
      content: 'Hello! I\'m AARAV, your advanced AI assistant. How can I help you today?',
      timestamp: '14:30:16',
      sender: 'aarav'
    },
    {
      id: 3,
      type: 'user',
      content: 'Show me system status',
      timestamp: '14:30:45',
      sender: 'user'
    },
    {
      id: 4,
      type: 'ai',
      content: 'System Status: All modules are operational. CPU usage is at 23%, memory at 67%. All API endpoints are responding normally. Current network latency is optimal at 12ms average.',
      timestamp: '14:30:46',
      sender: 'aarav'
    }
  ]);

  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    const userMessage = {
      id: messages.length + 1,
      type: 'user',
      content: message,
      timestamp: new Date().toLocaleTimeString('en-US', { hour12: false }),
      sender: 'user'
    };

    setMessages(prev => [...prev, userMessage]);
    setMessage('');

    // Simulate AI response
    setTimeout(() => {
      const aiResponse = {
        id: messages.length + 2,
        type: 'ai',
        content: generateAIResponse(message),
        timestamp: new Date().toLocaleTimeString('en-US', { hour12: false }),
        sender: 'aarav'
      };
      setMessages(prev => [...prev, aiResponse]);
    }, 1000 + Math.random() * 2000);
  };

  const generateAIResponse = (userInput) => {
    const responses = [
      "I understand your request. Let me process that information and provide you with the most accurate response.",
      "Analyzing your query... Based on current system parameters, here's what I found.",
      "Processing complete. The data indicates optimal performance across all monitored metrics.",
      "Your request has been logged and processed. All systems are functioning within normal parameters.",
      "I've cross-referenced your query with our database. Here are the relevant findings.",
      "Task initiated successfully. I'll monitor the progress and update you with any significant changes."
    ];
    
    if (userInput.toLowerCase().includes('status')) {
      return "Current system status: All AI modules are online and functioning optimally. CPU load is stable, memory usage is within acceptable limits, and network connectivity is excellent.";
    } else if (userInput.toLowerCase().includes('help')) {
      return "I can assist you with system monitoring, task automation, data analysis, voice commands, and much more. Just let me know what you need!";
    } else if (userInput.toLowerCase().includes('task')) {
      return "I can help you create, monitor, and manage various tasks. Would you like me to show you the current task queue or create a new automated task?";
    }
    
    return responses[Math.floor(Math.random() * responses.length)];
  };

  const toggleListening = () => {
    setIsListening(!isListening);
    if (!isListening) {
      // Simulate voice recognition
      setTimeout(() => {
        setIsListening(false);
      }, 3000);
    }
  };

  const toggleSpeaking = () => {
    setIsSpeaking(!isSpeaking);
  };

  const getMessageIcon = (sender) => {
    switch (sender) {
      case 'user':
        return <User className="w-4 h-4" />;
      case 'aarav':
        return <Bot className="w-4 h-4" />;
      default:
        return <Circle className="w-4 h-4" />;
    }
  };

  const getMessageStyle = (sender) => {
    switch (sender) {
      case 'user':
        return 'bg-green-500/20 border-green-500/50 ml-12';
      case 'aarav':
        return 'bg-blue-500/20 border-blue-500/50 mr-12';
      default:
        return 'bg-gray-600/20 border-gray-600/50 mx-8';
    }
  };

  return (
    <div className="h-full p-4 flex flex-col">
      {/* Chat Header */}
      <Card className="bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10 mb-4">
        <div className="p-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-400 to-cyan-600 rounded-full flex items-center justify-center shadow-lg shadow-blue-500/30 relative">
                <Bot className="w-6 h-6 text-black" />
                <div className="absolute -top-1 -right-1 w-3 h-3 bg-green-400 rounded-full border-2 border-black animate-pulse"></div>
              </div>
              <div>
                <h3 className="text-green-400 font-mono text-sm font-semibold">AARAV</h3>
                <p className="text-green-400/70 text-xs">AI Assistant • Online</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-2">
              <Button
                variant="outline"
                size="sm"
                onClick={toggleSpeaking}
                className={`h-8 w-8 p-0 ${
                  isSpeaking 
                    ? 'border-green-500 bg-green-500/20 text-green-400' 
                    : 'border-gray-600 text-gray-400'
                }`}
              >
                {isSpeaking ? <Volume2 className="w-4 h-4" /> : <VolumeX className="w-4 h-4" />}
              </Button>
              
              <Badge className="bg-green-500/20 text-green-400 border-green-500/50 font-mono text-xs">
                ACTIVE
              </Badge>
            </div>
          </div>
        </div>
      </Card>

      {/* Messages Area */}
      <Card className="flex-1 bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10 mb-4 overflow-hidden">
        <div className="p-4 h-full flex flex-col">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-green-400 font-mono text-sm font-semibold flex items-center">
              <MessageSquare className="w-4 h-4 mr-2" />
              CONVERSATION
            </h3>
            <div className="text-green-600 font-mono text-xs">
              {messages.filter(m => m.type !== 'system').length} messages
            </div>
          </div>
          
          <div className="flex-1 overflow-y-auto space-y-3 pr-2">
            {messages.map((msg) => (
              <div
                key={msg.id}
                className={`p-3 rounded-lg border backdrop-blur-sm ${getMessageStyle(msg.sender)}`}
              >
                <div className="flex items-start space-x-3">
                  <Avatar className="w-8 h-8 flex-shrink-0">
                    <div className={`w-full h-full rounded-full flex items-center justify-center ${
                      msg.sender === 'user' 
                        ? 'bg-green-500 text-black' 
                        : msg.sender === 'aarav'
                        ? 'bg-blue-500 text-black'
                        : 'bg-gray-600 text-white'
                    }`}>
                      {getMessageIcon(msg.sender)}
                    </div>
                  </Avatar>
                  
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center space-x-2 mb-1">
                      <span className="text-green-300 font-mono text-sm font-semibold">
                        {msg.sender === 'user' ? 'You' : msg.sender === 'aarav' ? 'AARAV' : 'System'}
                      </span>
                      <span className="text-green-600 font-mono text-xs">
                        {msg.timestamp}
                      </span>
                    </div>
                    <p className="text-green-100 text-sm leading-relaxed">
                      {msg.content}
                    </p>
                  </div>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        </div>
      </Card>

      {/* Input Area */}
      <Card className="bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10">
        <div className="p-4">
          <form onSubmit={handleSendMessage} className="flex space-x-2">
            <div className="flex-1 relative">
              <Input
                ref={inputRef}
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your message or use voice command..."
                className="bg-gray-900/50 border-green-500/30 text-green-200 placeholder-green-600 pr-12 font-mono"
                disabled={isListening}
              />
              {isListening && (
                <div className="absolute right-3 top-1/2 transform -translate-y-1/2">
                  <div className="flex space-x-1">
                    {[...Array(3)].map((_, i) => (
                      <div
                        key={i}
                        className="w-1 h-4 bg-green-400 rounded-full animate-bounce"
                        style={{ animationDelay: `${i * 0.2}s` }}
                      ></div>
                    ))}
                  </div>
                </div>
              )}
            </div>
            
            <Button
              type="button"
              onClick={toggleListening}
              className={`h-10 w-10 p-0 ${
                isListening 
                  ? 'bg-red-500/20 border-red-500/50 text-red-400 hover:bg-red-500/30' 
                  : 'bg-emerald-500/20 border-emerald-500/50 text-emerald-400 hover:bg-emerald-500/30'
              }`}
              variant="outline"
            >
              {isListening ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
            </Button>
            
            <Button 
              type="submit"
              className="bg-green-500/20 text-green-400 border-green-500/50 hover:bg-green-500/30 h-10 px-6"
              variant="outline"
              disabled={!message.trim() || isListening}
            >
              <Send className="w-4 h-4 mr-2" />
              Send
            </Button>
          </form>
          
          <div className="mt-3 flex items-center justify-between text-xs">
            <div className="flex items-center space-x-4 text-green-600">
              <span className="flex items-center">
                <Zap className="w-3 h-3 mr-1" />
                Voice: {isListening ? 'Listening...' : 'Ready'}
              </span>
              <span className="flex items-center">
                <Circle className="w-3 h-3 mr-1 fill-current" />
                Audio: {isSpeaking ? 'Enabled' : 'Muted'}
              </span>
            </div>
            <div className="text-green-600 font-mono">
              Press Ctrl+/ for shortcuts
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
};

export default ChatPanel;