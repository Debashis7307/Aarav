import React, { useState, useEffect } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import AuthModal from "./components/AuthModal";
import Dashboard from "./components/Dashboard";
import { Toaster } from "./components/ui/toaster";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate app initialization
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 2000);
    return () => clearTimeout(timer);
  }, []);

  const handleAuthentication = (method) => {
    console.log(`Authentication method: ${method}`);
    // Simulate authentication process
    setTimeout(() => {
      setIsAuthenticated(true);
    }, 2000);
  };

  if (isLoading) {
    return (
      <div className="min-h-screen bg-black flex items-center justify-center">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-green-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <div className="text-green-400 font-mono text-xl">Initializing AARAV System...</div>
          <div className="text-green-600 font-mono text-sm mt-2">Loading AI Modules</div>
        </div>
      </div>
    );
  }

  return (
    <div className="App min-h-screen bg-black overflow-hidden">
      <BrowserRouter>
        <Routes>
          <Route 
            path="/" 
            element={
              isAuthenticated ? (
                <Dashboard />
              ) : (
                <AuthModal onAuthenticate={handleAuthentication} />
              )
            } 
          />
        </Routes>
      </BrowserRouter>
      <Toaster />
    </div>
  );
}

export default App;