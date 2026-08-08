export default function TeamBuilder() {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Squad Builder & Chemistry</h1>
        <button className="btn-primary">Run Scenario Simulation</button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <div className="lg:col-span-3 glass-panel p-6">
          <h2 className="text-lg font-semibold mb-4">Current Squad Layout</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {[...Array(11)].map((_, i) => (
              <div key={i} className="aspect-[3/4] rounded-lg border border-white/10 bg-gradient-to-b from-white/5 to-transparent p-4 flex flex-col items-center justify-center text-center relative overflow-hidden group hover:border-primary/50 transition-colors cursor-pointer">
                <div className="absolute inset-0 bg-primary/5 opacity-0 group-hover:opacity-100 transition-opacity" />
                <div className="w-12 h-12 rounded-full bg-white/10 mb-3" />
                <p className="text-sm font-medium text-muted">Empty Slot {i+1}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="space-y-6">
          <div className="glass-panel p-6">
            <h3 className="font-semibold mb-4">Chemistry Engine</h3>
            <div className="flex items-center justify-center h-32 border border-white/5 rounded-lg bg-black/20 text-muted text-sm">
              [Synergy Score]
            </div>
          </div>
          <div className="glass-panel p-6">
            <h3 className="font-semibold mb-4">Role Coverage</h3>
            <div className="space-y-3">
              <ProgressBar label="Top Order" value={0} />
              <ProgressBar label="Middle Order" value={0} />
              <ProgressBar label="Pace Attack" value={0} />
              <ProgressBar label="Spin Dept" value={0} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function ProgressBar({ label, value }: { label: string, value: number }) {
  return (
    <div>
      <div className="flex justify-between text-xs mb-1 text-muted">
        <span>{label}</span>
        <span>{value}%</span>
      </div>
      <div className="h-2 w-full bg-black/40 rounded-full overflow-hidden">
        <div className="h-full bg-primary" style={{ width: `${value}%` }} />
      </div>
    </div>
  );
}
