import { useEffect, useRef } from 'react';
import { useAuctionStore } from '../store/auctionStore';

export function useAuctionSocket(url: string) {
  const ws = useRef<WebSocket | null>(null);
  const addLogEvent = useAuctionStore((state) => state.addLogEvent);

  useEffect(() => {
    ws.current = new WebSocket(url);

    ws.current.onopen = () => {
      console.log('Connected to Auction WebSocket');
    };

    ws.current.onmessage = (event) => {
      // Parse incoming auction events (bids, player sold, etc)
      const data = event.data;
      addLogEvent(`[Live] ${data}`);
    };

    ws.current.onclose = () => {
      console.log('Disconnected from Auction WebSocket');
    };

    return () => {
      ws.current?.close();
    };
  }, [url, addLogEvent]);

  const sendBid = (amount: number) => {
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      ws.current.send(JSON.stringify({ type: 'bid', amount }));
    }
  };

  return { sendBid };
}
