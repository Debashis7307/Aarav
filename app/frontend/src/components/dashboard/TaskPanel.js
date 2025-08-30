import React, { useState } from "react";
import { Card } from "../ui/card";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Textarea } from "../ui/textarea";
import { Badge } from "../ui/badge";
import { 
  Terminal, 
  Play, 
  Pause, 
  Square, 
  Settings, 
  Code, 
  Database,
  FileText,
  Cpu,
  Zap,
  CheckCircle,
  Clock,
  AlertCircle
} from "lucide-react";

const TaskPanel = () => {
  const [activeTab, setActiveTab] = useState('terminal');
  const [terminalInput, setTerminalInput] = useState('');
  const [terminalHistory, setTerminalHistory] = useState([
    { type: 'system', content: 'AARAV Terminal v2.1.0 initialized', timestamp: '14:30:15' },
    { type: 'system', content: 'All AI modules loaded successfully', timestamp: '14:30:16' },
    { type: 'user', content: 'status', timestamp: '14:30:20' },
    { type: 'output', content: 'System Status: ONLINE | CPU: 23% | Memory: 67%', timestamp: '14:30:20' }
  ]);

  const [tasks] = useState([
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
  ]);

  const handleTerminalSubmit = (e) => {
    e.preventDefault();
    if (!terminalInput.trim()) return;

    const newEntry = {
      type: 'user',
      content: terminalInput,
      timestamp: new Date().toLocaleTimeString('en-US', { hour12: false })
    };

    // Mock response based on command
    let response = 'Command not recognized';
    if (terminalInput.toLowerCase().includes('status')) {
      response = 'System Status: ONLINE | All modules active';
    } else if (terminalInput.toLowerCase().includes('help')) {
      response = 'Available commands: status, clear, tasks, ai-status, system-info';
    } else if (terminalInput.toLowerCase().includes('clear')) {
      setTerminalHistory([]);
      setTerminalInput('');
      return;
    } else if (terminalInput.toLowerCase().includes('tasks')) {
      response = `Active tasks: ${tasks.filter(t => t.status === 'running').length} | Completed: ${tasks.filter(t => t.status === 'completed').length}`;
    }

    const responseEntry = {
      type: 'output',
      content: response,
      timestamp: new Date().toLocaleTimeString('en-US', { hour12: false })
    };

    setTerminalHistory(prev => [...prev, newEntry, responseEntry]);
    setTerminalInput('');
  };

  const getTaskIcon = (type) => {
    switch (type) {
      case 'data': return Database;
      case 'ai': return Cpu;
      case 'security': return Settings;
      case 'database': return FileText;
      default: return Code;
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'running': return 'text-green-400';
      case 'completed': return 'text-blue-400';
      case 'pending': return 'text-yellow-400';
      case 'paused': return 'text-orange-400';
      default: return 'text-gray-400';
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'running': return Play;
      case 'completed': return CheckCircle;
      case 'pending': return Clock;
      case 'paused': return Pause;
      default: return AlertCircle;
    }
  };

  return (
    <div className="h-full p-4 space-y-4">
      {/* Tab Navigation */}
      <div className="flex space-x-2 border-b border-green-500/20 pb-2">
        <Button
          variant={activeTab === 'terminal' ? 'default' : 'ghost'}
          size="sm"
          onClick={() => setActiveTab('terminal')}
          className={`font-mono text-xs ${activeTab === 'terminal' 
            ? 'bg-green-500/20 text-green-400 border-green-500/50' 
            : 'text-green-300 hover:text-green-200'
          }`}
        >
          <Terminal className="w-4 h-4 mr-2" />
          TERMINAL
        </Button>
        <Button
          variant={activeTab === 'tasks' ? 'default' : 'ghost'}
          size="sm"
          onClick={() => setActiveTab('tasks')}
          className={`font-mono text-xs ${activeTab === 'tasks' 
            ? 'bg-green-500/20 text-green-400 border-green-500/50' 
            : 'text-green-300 hover:text-green-200'
          }`}
        >
          <Cpu className="w-4 h-4 mr-2" />
          TASKS
        </Button>
        <Button
          variant={activeTab === 'control' ? 'default' : 'ghost'}
          size="sm"
          onClick={() => setActiveTab('control')}
          className={`font-mono text-xs ${activeTab === 'control' 
            ? 'bg-green-500/20 text-green-400 border-green-500/50' 
            : 'text-green-300 hover:text-green-200'
          }`}
        >
          <Settings className="w-4 h-4 mr-2" />
          CONTROL
        </Button>
      </div>

      {/* Terminal Tab */}
      {activeTab === 'terminal' && (
        <Card className="bg-black/80 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10 h-[calc(100vh-200px)]">
          <div className="p-4 h-full flex flex-col">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-green-400 font-mono text-sm font-semibold flex items-center">
                <Terminal className="w-4 h-4 mr-2" />
                AARAV TERMINAL
              </h3>
              <div className="flex space-x-1">
                <div className="w-3 h-3 rounded-full bg-red-500"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
              </div>
            </div>
            
            <div className="flex-1 bg-gray-900/50 rounded-lg p-4 font-mono text-sm overflow-y-auto mb-4">
              {terminalHistory.map((entry, index) => (
                <div key={index} className="mb-2 flex">
                  <span className="text-green-600 mr-2">[{entry.timestamp}]</span>
                  <span className={`${
                    entry.type === 'user' ? 'text-green-400' :
                    entry.type === 'system' ? 'text-cyan-400' :
                    'text-green-200'
                  }`}>
                    {entry.type === 'user' && '> '}
                    {entry.content}
                  </span>
                </div>
              ))}
            </div>

            <form onSubmit={handleTerminalSubmit} className="flex space-x-2">
              <span className="text-green-400 font-mono self-center">></span>
              <Input
                value={terminalInput}
                onChange={(e) => setTerminalInput(e.target.value)}
                className="flex-1 bg-gray-900/50 border-green-500/30 text-green-200 font-mono placeholder-green-600"
                placeholder="Enter command..."
                autoComplete="off"
              />
              <Button 
                type="submit"
                size="sm"
                className="bg-green-500/20 text-green-400 border-green-500/50 hover:bg-green-500/30"
              >
                <Play className="w-4 h-4" />
              </Button>
            </form>
          </div>
        </Card>
      )}

      {/* Tasks Tab */}
      {activeTab === 'tasks' && (
        <Card className="bg-black/80 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10 h-[calc(100vh-200px)]">
          <div className="p-4">
            <h3 className="text-green-400 font-mono text-sm font-semibold mb-4 flex items-center">
              <Cpu className="w-4 h-4 mr-2" />
              ACTIVE TASKS
            </h3>
            <div className="space-y-3 max-h-[calc(100vh-300px)] overflow-y-auto">
              {tasks.map((task) => {
                const TaskIcon = getTaskIcon(task.type);
                const StatusIcon = getStatusIcon(task.status);
                
                return (
                  <div key={task.id} className="p-4 rounded-lg bg-gray-900/50 border border-green-500/20 hover:border-green-500/40 transition-colors">
                    <div className="flex items-center justify-between mb-3">
                      <div className="flex items-center space-x-3">
                        <TaskIcon className="w-5 h-5 text-green-400" />
                        <span className="text-green-200 font-semibold">{task.name}</span>
                      </div>
                      <div className="flex items-center space-x-2">
                        <StatusIcon className={`w-4 h-4 ${getStatusColor(task.status)}`} />
                        <Badge className={`font-mono text-xs ${getStatusColor(task.status)} bg-transparent border`}>
                          {task.status.toUpperCase()}
                        </Badge>
                      </div>
                    </div>
                    
                    <div className="mb-3">
                      <div className="flex items-center justify-between text-xs text-green-400 mb-1">
                        <span>Progress</span>
                        <span>{task.progress}%</span>
                      </div>
                      <div className="w-full h-2 bg-gray-800 rounded-full overflow-hidden">
                        <div 
                          className="h-full bg-gradient-to-r from-green-600 to-green-400 transition-all duration-500"
                          style={{ width: `${task.progress}%` }}
                        ></div>
                      </div>
                    </div>
                    
                    <div className="flex items-center justify-between text-xs">
                      <span className="text-green-600">
                        {task.startTime ? `Started: ${task.startTime}` : 'Not started'}
                      </span>
                      <div className="flex space-x-1">
                        {task.status === 'running' && (
                          <Button size="sm" variant="outline" className="h-6 w-6 p-0 border-yellow-500/50 text-yellow-400 hover:bg-yellow-500/20">
                            <Pause className="w-3 h-3" />
                          </Button>
                        )}
                        {task.status === 'paused' && (
                          <Button size="sm" variant="outline" className="h-6 w-6 p-0 border-green-500/50 text-green-400 hover:bg-green-500/20">
                            <Play className="w-3 h-3" />
                          </Button>
                        )}
                        <Button size="sm" variant="outline" className="h-6 w-6 p-0 border-red-500/50 text-red-400 hover:bg-red-500/20">
                          <Square className="w-3 h-3" />
                        </Button>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </Card>
      )}

      {/* Control Tab */}
      {activeTab === 'control' && (
        <Card className="bg-black/80 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10 h-[calc(100vh-200px)]">
          <div className="p-4">
            <h3 className="text-green-400 font-mono text-sm font-semibold mb-4 flex items-center">
              <Settings className="w-4 h-4 mr-2" />
              SYSTEM CONTROL
            </h3>
            
            <div className="space-y-4">
              <div>
                <label className="text-green-300 text-sm font-mono mb-2 block">AI Response Mode</label>
                <select className="w-full bg-gray-900/50 border border-green-500/30 text-green-200 p-2 rounded-lg font-mono text-sm">
                  <option value="normal">Normal Response</option>
                  <option value="detailed">Detailed Analysis</option>
                  <option value="quick">Quick Response</option>
                </select>
              </div>
              
              <div>
                <label className="text-green-300 text-sm font-mono mb-2 block">Voice Recognition Sensitivity</label>
                <input 
                  type="range" 
                  min="1" 
                  max="10" 
                  defaultValue="7"
                  className="w-full accent-green-500"
                />
              </div>
              
              <div>
                <label className="text-green-300 text-sm font-mono mb-2 block">System Commands</label>
                <Textarea
                  className="w-full bg-gray-900/50 border-green-500/30 text-green-200 font-mono text-sm"
                  placeholder="Enter system commands..."
                  rows={4}
                />
              </div>
              
              <div className="flex space-x-2">
                <Button className="flex-1 bg-green-500/20 text-green-400 border-green-500/50 hover:bg-green-500/30 font-mono">
                  <Zap className="w-4 h-4 mr-2" />
                  Execute
                </Button>
                <Button variant="outline" className="border-red-500/50 text-red-400 hover:bg-red-500/20 font-mono">
                  <Square className="w-4 h-4 mr-2" />
                  Stop
                </Button>
              </div>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
};

export default TaskPanel;