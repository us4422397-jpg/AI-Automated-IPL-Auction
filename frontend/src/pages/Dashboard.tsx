import { Activity, Shield, Users, Gavel } from 'lucide-react';

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard title="Remaining Budget" value="₹100 Cr" icon={Activity} trend="+0% from start" />
        <StatCard title="Squad Size" value="0 / 25" icon={Users} trend="Need 18 minimum" />
        <StatCard title="Team Strength" value="-- / 100" icon={Shield} trend="Awaiting players" />
        <StatCard title="Auction Round" value="Pre-Auction" icon={Gavel} trend="Starts in 2h 15m" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 glass-panel p-6 min-h-[400px]">
          <h2 className="text-lg font-semibold mb-4">Live Bidding Timeline</h2>
          <div className="flex items-center justify-center h-[300px] text-muted border border-white/5 rounded-lg bg-black/20">
            [Chart Area: Bidding Timeline]
          </div>
        </div>
        
        <div className="glass-panel p-6 min-h-[400px]">
          <h2 className="text-lg font-semibold mb-4">Team Balance Heatmap</h2>
          <div className="flex items-center justify-center h-[300px] text-muted border border-white/5 rounded-lg bg-black/20">
            [Chart Area: Heatmap]
          </div>
        </div>
      </div>
    </div>
  );
}

function StatCard({ title, value, icon: Icon, trend }: { title: string, value: string, icon: any, trend: string }) {
  return (
    <div className="glass-panel p-6">
      <div className="flex justify-between items-start">
        <div>
          <p className="text-sm font-medium text-muted">{title}</p>
          <p className="text-3xl font-bold mt-2 text-white">{value}</p>
        </div>
        <div className="p-3 bg-primary/10 rounded-lg">
          <Icon className="w-5 h-5 text-primary" />
        </div>
      </div>
      <div className="mt-4 flex items-center text-sm">
        <span className="text-secondary bg-secondary/10 px-2 py-0.5 rounded text-xs font-medium">{trend}</span>
      </div>
    </div>
  );
}
