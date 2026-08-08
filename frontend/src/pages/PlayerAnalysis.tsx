export default function PlayerAnalysis() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Player Analysis Engine</h1>
        <div className="flex gap-2">
          <input type="text" placeholder="Search players..." className="input-field w-64" />
          <button className="btn-primary">Filter</button>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-0">
        <div className="lg:col-span-1 glass-panel p-4 flex flex-col min-h-0">
          <div className="flex-1 overflow-y-auto pr-2 space-y-2">
            {[1,2,3,4,5,6].map(i => (
              <div key={i} className="p-3 rounded-lg border border-white/5 bg-white/5 hover:bg-white/10 cursor-pointer transition-colors flex justify-between items-center">
                <div>
                  <p className="font-semibold text-sm">Player Name {i}</p>
                  <p className="text-xs text-muted">Batsman • ₹2.00 Cr</p>
                </div>
                <div className="text-right">
                  <div className="text-xs text-secondary font-medium">92% Match</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="lg:col-span-2 glass-panel p-6 flex flex-col min-h-0">
          <div className="border-b border-white/10 pb-4 mb-4 flex justify-between items-start">
            <div>
              <h2 className="text-2xl font-bold">Selected Player</h2>
              <p className="text-muted">Detailed analytics and AI projections</p>
            </div>
            <button className="btn-primary">Add to Shortlist</button>
          </div>
          
          <div className="flex-1 grid grid-cols-2 gap-4">
            <div className="border border-white/5 rounded-lg bg-black/20 flex items-center justify-center text-muted">
              [Performance Radar Chart]
            </div>
            <div className="border border-white/5 rounded-lg bg-black/20 flex items-center justify-center text-muted">
              [Predicted Value & Risk Analysis]
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
