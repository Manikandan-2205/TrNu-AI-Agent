"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import { 
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Legend,
  PieChart, Pie, Cell
} from "recharts";
import { Activity, LayoutDashboard, Users, Zap } from "lucide-react";

const COLORS = ['#10B981', '#34D399', '#059669', '#047857'];

export default function Dashboard() {
  const [timeframe, setTimeframe] = useState<"week" | "month">("week");
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const res = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'}/dashboard/metrics?timeframe=${timeframe}`);
        setData(res.data);
      } catch (err) {
        console.error("Error fetching metrics", err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [timeframe]);

  if (loading || !data) {
    return (
      <div className="flex items-center justify-center min-h-[calc(100vh-4rem)]">
        <div className="w-12 h-12 border-4 border-primary border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <div>
          <h1 className="text-3xl font-bold text-white flex items-center gap-2">
            <LayoutDashboard className="text-primary" /> AI Agent Metrics
          </h1>
          <p className="text-gray-400 mt-1">Monitor your service desk performance and AI efficiency.</p>
        </div>

        {/* The Two Interactive Buttons */}
        <div className="glass-panel p-1 rounded-xl inline-flex">
          <button 
            onClick={() => setTimeframe("week")}
            className={`px-6 py-2 rounded-lg text-sm font-medium transition-all ${timeframe === 'week' ? 'bg-primary text-white shadow-lg glow-text' : 'text-gray-400 hover:text-white'}`}
          >
            This Week
          </button>
          <button 
            onClick={() => setTimeframe("month")}
            className={`px-6 py-2 rounded-lg text-sm font-medium transition-all ${timeframe === 'month' ? 'bg-primary text-white shadow-lg glow-text' : 'text-gray-400 hover:text-white'}`}
          >
            This Month
          </button>
        </div>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="glass-panel p-6 rounded-2xl border-l-4 border-l-primary">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-400 mb-1">New Client Visits</p>
              <h3 className="text-4xl font-bold text-white">{data.new_clients}</h3>
            </div>
            <div className="p-3 bg-primary/10 rounded-xl text-primary">
              <Users className="w-6 h-6" />
            </div>
          </div>
        </div>
        
        <div className="glass-panel p-6 rounded-2xl border-l-4 border-l-emerald-400">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-400 mb-1">AI Caching Savings</p>
              <h3 className="text-4xl font-bold text-white">{data.tokens_saved.toLocaleString()}</h3>
              <p className="text-xs text-emerald-400 mt-1">Tokens saved from hitting LLM</p>
            </div>
            <div className="p-3 bg-emerald-500/10 rounded-xl text-emerald-400">
              <Zap className="w-6 h-6" />
            </div>
          </div>
        </div>

        <div className="glass-panel p-6 rounded-2xl border-l-4 border-l-teal-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-400 mb-1">Total Issues Handled</p>
              <h3 className="text-4xl font-bold text-white">
                {data.department_issues.reduce((acc: any, curr: any) => acc + curr.value, 0)}
              </h3>
            </div>
            <div className="p-3 bg-teal-500/10 rounded-xl text-teal-500">
              <Activity className="w-6 h-6" />
            </div>
          </div>
        </div>
      </div>

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Agent Activity Bar Chart */}
        <div className="glass-panel p-6 rounded-2xl">
          <h3 className="text-lg font-semibold text-white mb-6">AI Agent Resolution Activity</h3>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={data.agent_activity}>
                <CartesianGrid strokeDasharray="3 3" stroke="#ffffff10" vertical={false} />
                <XAxis dataKey="name" stroke="#ffffff50" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#ffffff50" fontSize={12} tickLine={false} axisLine={false} />
                <Tooltip 
                  cursor={{ fill: '#ffffff05' }}
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#ffffff10', borderRadius: '8px' }}
                />
                <Legend />
                <Bar dataKey="resolved" name="Auto-Resolved" fill="#10B981" radius={[4, 4, 0, 0]} />
                <Bar dataKey="escalated" name="Escalated to Human" fill="#047857" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Department Issues Pie Chart */}
        <div className="glass-panel p-6 rounded-2xl">
          <h3 className="text-lg font-semibold text-white mb-6">Issues by Department</h3>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={data.department_issues}
                  cx="50%"
                  cy="50%"
                  innerRadius={80}
                  outerRadius={120}
                  paddingAngle={5}
                  dataKey="value"
                  stroke="none"
                >
                  {data.department_issues.map((entry: any, index: number) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip 
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#ffffff10', borderRadius: '8px' }}
                />
                <Legend verticalAlign="bottom" height={36} iconType="circle" />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
