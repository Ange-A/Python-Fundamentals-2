from itertools import combinations

def pick_best_hand(poker_hands):
    hand_rankings = [
        "High Card",
        "One Pair",
        "Two Pair",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
        "Royal Flush"
    ]
    
    best_hand_ranking = -1
    best_hand = None
    
    for hand in poker_hands:
        
        combinations_of_5 = combinations(hand, 5)
        
        for combination in combinations_of_5:
            
            current_ranking = determine_hand_ranking(combination)
            

            if current_ranking > best_hand_ranking:
                best_hand_ranking = current_ranking
                best_hand = combination
    
    return best_hand

def determine_hand_ranking(hand):
  
    hand_rank = evaluate_hand(hand)
    
    return hand_rank
