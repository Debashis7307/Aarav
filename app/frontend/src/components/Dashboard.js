import React, { useState, useEffect } from "react";
import ChatPanel from "./dashboard/ChatPanel";
import FeaturesPanel from "./dashboard/FeaturesPanel";
import TaskPanel from "./dashboard/TaskPanel";
import { Activity, Zap, Cpu } from "lucide-react";
import { DotLottieReact } from '@lottiefiles/dotlottie-react';

const Dashboard = () => {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-emerald-950 relative overflow-hidden">
      {/* Animated Background Grid */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute inset-0 bg-[linear-gradient(90deg,transparent_24%,rgba(34,197,94,0.2)_25%,rgba(34,197,94,0.2)_26%,transparent_27%,transparent_74%,rgba(34,197,94,0.2)_75%,rgba(34,197,94,0.2)_76%,transparent_77%,transparent),linear-gradient(transparent_24%,rgba(34,197,94,0.2)_25%,rgba(34,197,94,0.2)_26%,transparent_27%,transparent_74%,rgba(34,197,94,0.2)_75%,rgba(34,197,94,0.2)_76%,transparent_77%,transparent)] bg-[length:30px_30px] animate-pulse"></div>
      </div>

      {/* Top Header Bar */}
      <header className="relative z-10 border-b border-green-500/20 bg-black/50 backdrop-blur-xl">
        <div className="px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="w-16 h-16 flex items-center justify-center">
                <DotLottieReact
                  src="https://lottie.host/a9497b0d-926b-4367-b43c-435811f72422/1no1qH4biu.lottie"
                  loop
                  autoplay
                  className="w-12 h-12"
                />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-300 bg-clip-text text-transparent">
                  AARAV Dashboard
                </h1>
                <p className="text-green-400/70 text-sm font-mono">Advanced AI Control Center</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-6">
              {/* System Status */}
              <div className="flex items-center space-x-2">
                <Activity className="w-4 h-4 text-green-400 animate-pulse" />
                <span className="text-green-400 font-mono text-sm">ONLINE</span>
              </div>
              
              {/* System Time */}
              <div className="text-green-300 font-mono text-sm">
                {currentTime.toLocaleTimeString()}
              </div>
              
              {/* System Load */}
              <div className="flex items-center space-x-2">
                <Cpu className="w-4 h-4 text-green-400" />
                <span className="text-green-400 font-mono text-sm">CPU: 23%</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Dashboard Layout */}
      <main className="flex h-[calc(100vh-80px)] relative z-10">
        {/* Left Panel - Features & API Health */}
        <div className="w-1/4 border-r border-green-500/20 bg-black/30 backdrop-blur-xl overflow-y-auto">
          <FeaturesPanel />
        </div>

        {/* Center Panel - Task Interface */}
        <div className="flex-1 bg-black/20 backdrop-blur-sm">
          <TaskPanel />
        </div>

        {/* Right Panel - Chat Interface */}
        <div className="w-1/3 border-l border-green-500/20 bg-black/30 backdrop-blur-xl overflow-y-auto">
          <ChatPanel />
        </div>
      </main>

      {/* Bottom Status Bar */}
      <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-green-600 via-emerald-500 to-cyan-400"></div>
    </div>
  );
};

export default Dashboard;