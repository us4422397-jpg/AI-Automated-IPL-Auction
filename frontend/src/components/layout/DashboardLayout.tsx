import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';

export default function DashboardLayout() {
  return (
    <div className="flex h-screen bg-background overflow-hidden">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0 overflow-y-auto">
        <header className="h-16 glass-panel border-b border-white/5 border-l-0 rounded-none flex items-center px-6 sticky top-0 z-10">
          <h1 className="text-xl font-semibold text-white">IPL AI Mastermind</h1>
          <div className="ml-auto flex items-center space-x-4">
            <div className="text-sm text-muted">Budget: <span className="text-secondary font-mono">₹100 Cr</span></div>
            <div className="h-8 w-8 rounded-full bg-primary/20 flex items-center justify-center border border-primary/50 text-primary font-bold">
              CSK
            </div>
          </div>
        </header>
        <main className="flex-1 p-6 max-w-7xl mx-auto w-full">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
