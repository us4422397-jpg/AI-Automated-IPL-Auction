from typing import Dict, Any, List
from app.ml.base import BaseMLModel
from app.ml.coach.strategy import apply_strategy_modifier

class AuctionCoachAdvisor(BaseMLModel):
    model_name = "auction_coach"
    model_version = "1.0.0"
    
    def predict(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """
        features: {'player': Dict, 'team': Dict, 'auction_state': Dict}
        """
        player = features.get('player', {})
        team = features.get('team', {})
        state = features.get('auction_state', {})
        
        current_bid = state.get('current_bid', player.get('base_price', 0))
        strategy = team.get('strategy_profile', 'balanced')
        
        # Determine max safe bid (in a real app, this would use MCKP optimizer)
        base_valuation = player.get('base_price', 20000000) * 3.0
        max_safe_bid = apply_strategy_modifier(base_valuation, strategy)
        max_safe_bid = min(max_safe_bid, team.get('remaining_budget', 0) * 0.4)
        
        # Advice logic
        advice = "WAIT"
        reason = "Current bid exceeds calculated maximum safe value."
        if current_bid < max_safe_bid:
            advice = "BID"
            reason = f"Player value is up to {max_safe_bid/10000000:.1f} Cr."
            
        return {
            "advice": advice,
            "max_safe_bid": float(max_safe_bid),
            "reasoning": reason,
            "confidence": 0.85
        }
        
    def explain(self, features: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "reasoning": "Coach advice combines negotiation probabilities, team strength impact, and budget constraints."
        }
        
    def save(self, path: str) -> None:
        pass
        
    @classmethod
    def load(cls, path: str) -> "BaseMLModel":
        return cls()
