import Link from 'next/link';
import { Leaf } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="fixed top-0 w-full z-50 glass-panel border-b border-white/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-2">
            <Leaf className="h-6 w-6 text-primary" />
            <Link href="/">
              <span className="font-bold text-xl tracking-tight text-white glow-text">TrNu Tech</span>
            </Link>
          </div>
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-8">
              <Link href="/" className="text-gray-300 hover:text-primary transition-colors px-3 py-2 rounded-md text-sm font-medium">Home</Link>
              <Link href="/dashboard" className="text-gray-300 hover:text-primary transition-colors px-3 py-2 rounded-md text-sm font-medium">Dashboard</Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}
