import React, { useState } from "react";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Scan, Mic, Shield, Zap, Eye, Volume2 } from "lucide-react";
import { useToast } from "../hooks/use-toast";

const AuthModal = ({ onAuthenticate }) => {
  const [selectedMethod, setSelectedMethod] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const { toast } = useToast();

  const handleAuthentication = async (method) => {
    setSelectedMethod(method);
    setIsProcessing(true);

    toast({
      title: `${method === 'face' ? 'Face' : 'Voice'} Authentication`,
      description: `Initializing ${method} recognition...`,
    });

    // Simulate authentication process
    setTimeout(() => {
      toast({
        title: "Authentication Successful",
        description: `Welcome back! ${method} verification completed.`,
      });
      setTimeout(() => {
        onAuthenticate(method);
      }, 1000);
    }, 3000);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-emerald-950 flex items-center justify-center p-4 relative overflow-hidden">
      {/* Animated Background Grid */}
      <div className="absolute inset-0 opacity-20">
        <div className="absolute inset-0 bg-[linear-gradient(90deg,transparent_24%,rgba(34,197,94,0.3)_25%,rgba(34,197,94,0.3)_26%,transparent_27%,transparent_74%,rgba(34,197,94,0.3)_75%,rgba(34,197,94,0.3)_76%,transparent_77%,transparent),linear-gradient(transparent_24%,rgba(34,197,94,0.3)_25%,rgba(34,197,94,0.3)_26%,transparent_27%,transparent_74%,rgba(34,197,94,0.3)_75%,rgba(34,197,94,0.3)_76%,transparent_77%,transparent)] bg-[length:50px_50px]"></div>
      </div>

      {/* Floating Particles */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        {[...Array(20)].map((_, i) => (
          <div
            key={i}
            className="absolute w-1 h-1 bg-green-400 rounded-full animate-pulse"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              animationDelay: `${Math.random() * 3}s`,
              animationDuration: `${2 + Math.random() * 2}s`
            }}
          />
        ))}
      </div>

      <Card className="w-full max-w-md bg-black/80 backdrop-blur-xl border-green-500/30 shadow-[0_0_50px_rgba(34,197,94,0.3)] relative z-10">
        <div className="p-8">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-20 h-20 mx-auto mb-4 relative">
              <div className="w-full h-full bg-gradient-to-br from-green-400 to-emerald-600 rounded-full flex items-center justify-center shadow-lg shadow-green-500/50">
                <Shield className="w-10 h-10 text-black" />
              </div>
              <div className="absolute -inset-2 border-2 border-green-400/50 rounded-full animate-pulse"></div>
            </div>
            <h1 className="text-3xl font-bold bg-gradient-to-r from-green-400 to-emerald-300 bg-clip-text text-transparent mb-2">
              AARAV
            </h1>
            <p className="text-green-300/80 font-mono text-sm">
              Advanced AI Assistant System
            </p>
            <div className="w-32 h-px bg-gradient-to-r from-transparent via-green-400 to-transparent mx-auto mt-4"></div>
          </div>

          {!isProcessing ? (
            <>
              <div className="text-center mb-6">
                <p className="text-green-200 font-mono text-sm mb-2">
                  AUTHENTICATION REQUIRED
                </p>
                <p className="text-gray-400 text-xs">
                  Choose your preferred authentication method
                </p>
              </div>

              <div className="space-y-4">
                <Button
                  onClick={() => handleAuthentication('face')}
                  className="w-full h-16 bg-gradient-to-r from-green-600/20 to-emerald-600/20 border-2 border-green-500/50 hover:border-green-400 transition-all duration-300 hover:shadow-lg hover:shadow-green-500/30 group relative overflow-hidden"
                  variant="outline"
                >
                  <div className="absolute inset-0 bg-gradient-to-r from-green-400/10 to-emerald-400/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div className="flex items-center space-x-4 relative z-10">
                    <div className="p-3 bg-green-500/20 rounded-lg group-hover:bg-green-500/30 transition-colors">
                      <Eye className="w-6 h-6 text-green-400" />
                    </div>
                    <div className="text-left">
                      <div className="text-green-200 font-semibold">Show Me Your Face</div>
                      <div className="text-green-400/70 text-sm font-mono">Biometric Verification</div>
                    </div>
                  </div>
                </Button>

                <Button
                  onClick={() => handleAuthentication('voice')}
                  className="w-full h-16 bg-gradient-to-r from-emerald-600/20 to-cyan-600/20 border-2 border-emerald-500/50 hover:border-emerald-400 transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/30 group relative overflow-hidden"
                  variant="outline"
                >
                  <div className="absolute inset-0 bg-gradient-to-r from-emerald-400/10 to-cyan-400/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                  <div className="flex items-center space-x-4 relative z-10">
                    <div className="p-3 bg-emerald-500/20 rounded-lg group-hover:bg-emerald-500/30 transition-colors">
                      <Volume2 className="w-6 h-6 text-emerald-400" />
                    </div>
                    <div className="text-left">
                      <div className="text-green-200 font-semibold">Turn On By Voice</div>
                      <div className="text-emerald-400/70 text-sm font-mono">Voice Recognition</div>
                    </div>
                  </div>
                </Button>
              </div>
            </>
          ) : (
            <div className="text-center py-8">
              <div className="relative w-24 h-24 mx-auto mb-6">
                <Scan className="w-24 h-24 text-green-400 animate-pulse" />
                <div className="absolute inset-0 border-4 border-green-400/30 rounded-full animate-spin"></div>
              </div>
              <div className="space-y-2">
                <p className="text-green-400 font-mono text-lg">
                  {selectedMethod === 'face' ? 'SCANNING FACE...' : 'LISTENING...'}
                </p>
                <p className="text-green-600 text-sm">
                  {selectedMethod === 'face' 
                    ? 'Please look directly at the camera' 
                    : 'Say "Aarav, activate system"'
                  }
                </p>
              </div>
              <div className="mt-6 flex justify-center space-x-1">
                {[...Array(3)].map((_, i) => (
                  <div
                    key={i}
                    className="w-2 h-2 bg-green-400 rounded-full animate-bounce"
                    style={{ animationDelay: `${i * 0.2}s` }}
                  ></div>
                ))}
              </div>
            </div>
          )}

          {/* Footer */}
          <div className="mt-8 pt-4 border-t border-green-500/20">
            <div className="flex items-center justify-center space-x-2 text-green-600 text-xs font-mono">
              <Zap className="w-3 h-3" />
              <span>SECURE CONNECTION ESTABLISHED</span>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
};

export default AuthModal;