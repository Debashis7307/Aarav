// Mock data for AARAV AI Assistant Dashboard

export const mockSystemMetrics = {
  cpu: 23,
  memory: 67,
  storage: 45,
  network: 89
};

export const mockApiHealth = [
  { name: "Speech Recognition", status: "online", latency: 45 },
  { name: "Face Detection", status: "online", latency: 32 },
  { name: "NLP Engine", status: "online", latency: 28 },
  { name: "Voice Synthesis", status: "warning", latency: 156 },
  { name: "Database", status: "online", latency: 12 },
  { name: "Cloud Storage", status: "offline", latency: 0 }
];

export const mockFeatures = [
  { name: "Real-time Chat", enabled: true, icon: "Activity" },
  { name: "Voice Commands", enabled: true, icon: "Zap" },
  { name: "Face Recognition", enabled: true, icon: "Shield" },
  { name: "Task Automation", enabled: false, icon: "Cpu" },
  { name: "Data Analytics", enabled: true, icon: "Database" },
  { name: "Security Monitor", enabled: true, icon: "Server" }
];

export const mockTasks = [
  {
    id: 1,
    name: 'Data Processing Pipeline',
    status: 'running',
    progress: 67,
    type: 'data',
    startTime: '14:25:30'
  },
  {
    id: 2,
    name: 'Neural Network Training',
    status: 'completed',
    progress: 100,
    type: 'ai',
    startTime: '13:45:12'
  },
  {
    id: 3,
    name: 'Security Scan',
    status: 'pending',
    progress: 0,
    type: 'security',
    startTime: null
  },
  {
    id: 4,
    name: 'Database Optimization',
    status: 'paused',
    progress: 34,
    type: 'database',
    startTime: '14:10:45'
  }
];

export const mockChatMessages = [
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
];

export const mockTerminalHistory = [
  { type: 'system', content: 'AARAV Terminal v2.1.0 initialized', timestamp: '14:30:15' },
  { type: 'system', content: 'All AI modules loaded successfully', timestamp: '14:30:16' },
  { type: 'user', content: 'status', timestamp: '14:30:20' },
  { type: 'output', content: 'System Status: ONLINE | CPU: 23% | Memory: 67%', timestamp: '14:30:20' }
];

export const mockAIResponses = [
  "I understand your request. Let me process that information and provide you with the most accurate response.",
  "Analyzing your query... Based on current system parameters, here's what I found.",
  "Processing complete. The data indicates optimal performance across all monitored metrics.",
  "Your request has been logged and processed. All systems are functioning within normal parameters.",
  "I've cross-referenced your query with our database. Here are the relevant findings.",
  "Task initiated successfully. I'll monitor the progress and update you with any significant changes."
];

// Authentication simulation data
export const mockAuthMethods = [
  {
    type: 'face',
    name: 'Show Me Your Face',
    description: 'Biometric Verification',
    icon: 'Eye',
    processingMessage: 'SCANNING FACE...',
    instructions: 'Please look directly at the camera'
  },
  {
    type: 'voice',
    name: 'Turn On By Voice',
    description: 'Voice Recognition',
    icon: 'Volume2',
    processingMessage: 'LISTENING...',
    instructions: 'Say "Aarav, activate system"'
  }
];

// Utility functions for mock data
export const generateRandomMetric = (current, min, max, variance = 10) => {
  const change = (Math.random() - 0.5) * variance;
  return Math.max(min, Math.min(max, current + change));
};

export const getRandomAIResponse = () => {
  return mockAIResponses[Math.floor(Math.random() * mockAIResponses.length)];
};

export const simulateApiLatency = (baseLatency = 50) => {
  return baseLatency + Math.floor(Math.random() * 100);
};

export default {
  mockSystemMetrics,
  mockApiHealth,
  mockFeatures,
  mockTasks,
  mockChatMessages,
  mockTerminalHistory,
  mockAIResponses,
  mockAuthMethods,
  generateRandomMetric,
  getRandomAIResponse,
  simulateApiLatency
};