export default function AuctionRoom() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-red-500 animate-pulse shadow-[0_0_10px_rgba(239,68,68,0.7)]" />
          <h1 className="text-2xl font-bold">Live Auction Room</h1>
        </div>
        <div className="bg-surface px-4 py-2 rounded-lg border border-white/10 font-mono text-xl">
          Set 1: Marquee Players
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-0">
        <div className="lg:col-span-2 flex flex-col gap-6">
          <div className="glass-panel p-8 flex-1 flex flex-col items-center justify-center relative overflow-hidden">
            <div className="absolute inset-0 bg-gradient-to-b from-primary/5 to-transparent pointer-events-none" />
            
            <div className="text-center z-10">
              <h2 className="text-4xl font-bold mb-2">Virat Kohli</h2>
              <p className="text-xl text-muted mb-8">Right-hand Bat • Base: ₹2.00 Cr</p>
              
              <div className="text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-yellow-600 mb-8 font-mono">
                ₹15.50 Cr
              </div>
              
              <div className="flex gap-4 justify-center">
                <button className="px-8 py-4 bg-red-500/20 text-red-500 border border-red-500/50 rounded-xl font-bold text-lg hover:bg-red-500/30 transition-colors">
                  Withdraw
                </button>
                <button className="px-8 py-4 bg-primary text-white shadow-[0_0_20px_rgba(59,130,246,0.5)] rounded-xl font-bold text-lg hover:bg-primary/90 transition-all hover:scale-105">
                  Bid ₹15.75 Cr
                </button>
              </div>
            </div>
          </div>
          
          <div className="glass-panel p-6 h-48 overflow-y-auto">
            <h3 className="font-semibold mb-3 text-muted">Auction Log</h3>
            <div className="space-y-2 text-sm font-mono">
              <p><span className="text-secondary">00:00:15</span> RCB bid ₹15.50 Cr</p>
              <p><span className="text-secondary">00:00:12</span> MI bid ₹15.25 Cr</p>
              <p><span className="text-secondary">00:00:08</span> RCB bid ₹15.00 Cr</p>
            </div>
          </div>
        </div>

        <div className="glass-panel p-6 flex flex-col gap-6">
          <div className="border border-primary/30 bg-primary/5 rounded-xl p-5 relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary to-accent" />
            <h3 className="font-bold text-primary mb-3 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-primary animate-ping" />
              AI Auction Coach
            </h3>
            
            <div className="text-3xl font-bold text-white mb-2">BID NOW</div>
            <p className="text-sm text-white/80 mb-4">Max safe value calculated at ₹16.20 Cr based on your current squad gaps and remaining budget.</p>
            
            <button className="text-xs text-primary underline underline-offset-2 hover:text-white transition-colors">View AI Explanation (SHAP)</button>
          </div>
          
          <div className="flex-1 border border-white/5 rounded-xl bg-black/20 p-4">
            <h4 className="text-sm font-medium text-muted mb-3">Predicted Opponent Limits</h4>
            <div className="space-y-3">
              <div className="flex justify-between items-center text-sm">
                <span>MI</span>
                <span className="font-mono text-red-400">~₹15.80 Cr</span>
              </div>
              <div className="flex justify-between items-center text-sm">
                <span>PBKS</span>
                <span className="font-mono text-secondary">~₹18.00 Cr</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
