import React, { useState, useEffect } from "react";
import { Card } from "../ui/card";
import { Badge } from "../ui/badge";
import { 
  Server, 
  Database, 
  Wifi, 
  Shield, 
  Zap, 
  Activity,
  CheckCircle,
  AlertTriangle,
  XCircle,
  Cpu,
  MemoryStick,
  HardDrive,
  Network
} from "lucide-react";

const FeaturesPanel = () => {
  const [systemMetrics, setSystemMetrics] = useState({
    cpu: 23,
    memory: 67,
    storage: 45,
    network: 89
  });

  const [apiHealth, setApiHealth] = useState([
    { name: "Speech Recognition", status: "online", latency: 45 },
    { name: "Face Detection", status: "online", latency: 32 },
    { name: "NLP Engine", status: "online", latency: 28 },
    { name: "Voice Synthesis", status: "warning", latency: 156 },
    { name: "Database", status: "online", latency: 12 },
    { name: "Cloud Storage", status: "offline", latency: 0 }
  ]);

  const [features] = useState([
    { name: "Real-time Chat", enabled: true, icon: Activity },
    { name: "Voice Commands", enabled: true, icon: Zap },
    { name: "Face Recognition", enabled: true, icon: Shield },
    { name: "Task Automation", enabled: false, icon: Cpu },
    { name: "Data Analytics", enabled: true, icon: Database },
    { name: "Security Monitor", enabled: true, icon: Server }
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      setSystemMetrics(prev => ({
        cpu: Math.max(10, Math.min(90, prev.cpu + (Math.random() - 0.5) * 10)),
        memory: Math.max(20, Math.min(95, prev.memory + (Math.random() - 0.5) * 5)),
        storage: Math.max(30, Math.min(85, prev.storage + (Math.random() - 0.5) * 3)),
        network: Math.max(50, Math.min(100, prev.network + (Math.random() - 0.5) * 8))
      }));
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  const getStatusIcon = (status) => {
    switch (status) {
      case 'online':
        return <CheckCircle className="w-4 h-4 text-green-400" />;
      case 'warning':
        return <AlertTriangle className="w-4 h-4 text-yellow-400" />;
      case 'offline':
        return <XCircle className="w-4 h-4 text-red-400" />;
      default:
        return <CheckCircle className="w-4 h-4 text-green-400" />;
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'online':
        return 'text-green-400';
      case 'warning':
        return 'text-yellow-400';
      case 'offline':
        return 'text-red-400';
      default:
        return 'text-green-400';
    }
  };

  return (
    <div className="h-full p-4 space-y-4 overflow-y-auto">
      {/* System Metrics */}
      <Card className="bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10">
        <div className="p-4">
          <h3 className="text-green-400 font-mono text-sm font-semibold mb-4 flex items-center">
            <Activity className="w-4 h-4 mr-2" />
            SYSTEM METRICS
          </h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Cpu className="w-4 h-4 text-green-400" />
                <span className="text-green-200 text-sm">CPU</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-20 h-2 bg-gray-800 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-green-600 to-green-400 transition-all duration-500"
                    style={{ width: `${systemMetrics.cpu}%` }}
                  ></div>
                </div>
                <span className="text-green-400 text-xs font-mono w-8">{Math.round(systemMetrics.cpu)}%</span>
              </div>
            </div>
            
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <MemoryStick className="w-4 h-4 text-emerald-400" />
                <span className="text-green-200 text-sm">RAM</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-20 h-2 bg-gray-800 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-emerald-600 to-emerald-400 transition-all duration-500"
                    style={{ width: `${systemMetrics.memory}%` }}
                  ></div>
                </div>
                <span className="text-emerald-400 text-xs font-mono w-8">{Math.round(systemMetrics.memory)}%</span>
              </div>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <HardDrive className="w-4 h-4 text-cyan-400" />
                <span className="text-green-200 text-sm">SSD</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-20 h-2 bg-gray-800 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-cyan-600 to-cyan-400 transition-all duration-500"
                    style={{ width: `${systemMetrics.storage}%` }}
                  ></div>
                </div>
                <span className="text-cyan-400 text-xs font-mono w-8">{Math.round(systemMetrics.storage)}%</span>
              </div>
            </div>

            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <Network className="w-4 h-4 text-blue-400" />
                <span className="text-green-200 text-sm">NET</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-20 h-2 bg-gray-800 rounded-full overflow-hidden">
                  <div 
                    className="h-full bg-gradient-to-r from-blue-600 to-blue-400 transition-all duration-500"
                    style={{ width: `${systemMetrics.network}%` }}
                  ></div>
                </div>
                <span className="text-blue-400 text-xs font-mono w-8">{Math.round(systemMetrics.network)}%</span>
              </div>
            </div>
          </div>
        </div>
      </Card>

      {/* API Health Status */}
      <Card className="bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10">
        <div className="p-4">
          <h3 className="text-green-400 font-mono text-sm font-semibold mb-4 flex items-center">
            <Server className="w-4 h-4 mr-2" />
            API HEALTH
          </h3>
          <div className="space-y-2">
            {apiHealth.map((api, index) => (
              <div key={index} className="flex items-center justify-between p-2 rounded-lg bg-gray-900/50 hover:bg-gray-800/50 transition-colors">
                <div className="flex items-center space-x-3">
                  {getStatusIcon(api.status)}
                  <span className="text-green-200 text-sm">{api.name}</span>
                </div>
                <div className="flex items-center space-x-2">
                  <span className={`text-xs font-mono ${getStatusColor(api.status)}`}>
                    {api.latency}ms
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </Card>

      {/* Features Status */}
      <Card className="bg-black/60 backdrop-blur-xl border-green-500/30 shadow-lg shadow-green-500/10">
        <div className="p-4">
          <h3 className="text-green-400 font-mono text-sm font-semibold mb-4 flex items-center">
            <Zap className="w-4 h-4 mr-2" />
            FEATURES
          </h3>
          <div className="space-y-2">
            {features.map((feature, index) => {
              const IconComponent = feature.icon;
              return (
                <div key={index} className="flex items-center justify-between p-2 rounded-lg bg-gray-900/50 hover:bg-gray-800/50 transition-colors">
                  <div className="flex items-center space-x-3">
                    <IconComponent className={`w-4 h-4 ${feature.enabled ? 'text-green-400' : 'text-gray-500'}`} />
                    <span className={`text-sm ${feature.enabled ? 'text-green-200' : 'text-gray-400'}`}>
                      {feature.name}
                    </span>
                  </div>
                  <Badge 
                    variant={feature.enabled ? "default" : "secondary"}
                    className={`text-xs font-mono ${
                      feature.enabled 
                        ? 'bg-green-500/20 text-green-400 border-green-500/50' 
                        : 'bg-gray-600/20 text-gray-400 border-gray-600/50'
                    }`}
                  >
                    {feature.enabled ? 'ACTIVE' : 'INACTIVE'}
                  </Badge>
                </div>
              );
            })}
          </div>
        </div>
      </Card>
    </div>
  );
};

export default FeaturesPanel;