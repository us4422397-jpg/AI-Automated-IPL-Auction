import { create } from 'zustand';

interface AuctionState {
  currentBudget: number;
  squadSize: number;
  currentBid: number;
  activePlayer: any | null;
  auctionLog: string[];
  setBudget: (budget: number) => void;
  placeBid: (amount: number) => void;
  addLogEvent: (event: string) => void;
}

export const useAuctionStore = create<AuctionState>((set) => ({
  currentBudget: 1000000000,
  squadSize: 0,
  currentBid: 0,
  activePlayer: null,
  auctionLog: [],
  
  setBudget: (budget) => set({ currentBudget: budget }),
  placeBid: (amount) => set({ currentBid: amount }),
  addLogEvent: (event) => set((state) => ({ auctionLog: [event, ...state.auctionLog] })),
}));
