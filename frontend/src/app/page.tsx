import { ArrowRight, Bot, Code, Cloud, Shield } from "lucide-react";
import ChatWidget from "@/components/ChatWidget";

export default function Home() {
  return (
    <div className="relative min-h-[calc(100vh-4rem)] flex flex-col items-center justify-center overflow-hidden">
      {/* Background Decor */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/20 rounded-full blur-[120px] -z-10" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px] -z-10" />

      {/* Hero Content */}
      <div className="max-w-4xl mx-auto px-4 text-center space-y-8 z-10 py-20">
        <div className="inline-flex items-center space-x-2 glass-panel px-4 py-2 rounded-full mb-4">
          <span className="relative flex h-3 w-3">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
            <span className="relative inline-flex rounded-full h-3 w-3 bg-primary"></span>
          </span>
          <span className="text-sm text-gray-300 font-medium">AI Support Agent Online 24/7</span>
        </div>
        
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-white mb-6">
          Next-Gen Support for <br/>
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-emerald-300 glow-text">TrNu Tech</span>
        </h1>
        
        <p className="text-xl text-gray-400 max-w-2xl mx-auto leading-relaxed">
          Experience our intelligent Service Desk Platform. Our LangGraph-powered AI agent routes tickets, searches knowledge bases, and provides instant resolutions.
        </p>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 text-left">
          <div className="glass-panel p-6 rounded-2xl hover:-translate-y-1 transition-transform cursor-default">
            <Bot className="w-8 h-8 text-primary mb-4" />
            <h3 className="text-lg font-semibold text-white mb-2">Smart Routing</h3>
            <p className="text-gray-400 text-sm">Automatically classifies intents and assigns to the right department.</p>
          </div>
          <div className="glass-panel p-6 rounded-2xl hover:-translate-y-1 transition-transform cursor-default">
            <Cloud className="w-8 h-8 text-primary mb-4" />
            <h3 className="text-lg font-semibold text-white mb-2">Cloud Optimized</h3>
            <p className="text-gray-400 text-sm">Semantic caching reduces LLM calls by up to 90% for duplicate issues.</p>
          </div>
          <div className="glass-panel p-6 rounded-2xl hover:-translate-y-1 transition-transform cursor-default">
            <Shield className="w-8 h-8 text-primary mb-4" />
            <h3 className="text-lg font-semibold text-white mb-2">Instant Ticketing</h3>
            <p className="text-gray-400 text-sm">Generates actionable tickets internally while you chat.</p>
          </div>
        </div>
      </div>

      <ChatWidget />
    </div>
  );
}
