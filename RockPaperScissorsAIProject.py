import random

def get_ai_move(player_history):
    """Predicts the player's next move based on their history and returns the AI's move."""
    choices = ["rock", "paper", "scissors"]
    
    if not player_history:
        return random.choice(choices)
    
    last_player_move = player_history[-1]
    
    if last_player_move == "rock":
        predicted_player_move = "paper"
    elif last_player_move == "paper":
        predicted_player_move = "scissors"
    else:
        predicted_player_move = "rock"
        
    winning_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return winning_moves[predicted_player_move]

def determine_winner(player, ai):
    """Determines the winner of the round."""
    if player == ai:
        return "tie"
    
    winning_combinations = {
        ("rock", "scissors"): "player",
        ("scissors", "paper"): "player",
        ("paper", "rock"): "player"
    }
    
    return winning_combinations.get((player, ai), "ai")

def play_game():
    print("====================================")
    print("  Welcome to Rock Paper Scissors!  ")
    print("====================================")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.\n")
    
    player_history = []
    scores = {"player": 0, "ai": 0, "ties": 0}
    valid_moves = ["rock", "paper", "scissors"]
    
    while True:
        player_move = input("Your move: ").strip().lower()
        
        if player_move == "quit":
            print("\nThanks for playing!")
            print(f"Final Score -> You: {scores['player']} | AI: {scores['ai']} | Ties: {scores['ties']}")
            break
            
        if player_move not in valid_moves:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue
            
        ai_move = get_ai_move(player_history)
        player_history.append(player_move)
        print(f"AI chose: {ai_move}")
        
        result = determine_winner(player_move, ai_move)
        
        if result == "tie":
            print("It's a tie!")
            scores["ties"] += 1
        elif result == "player":
            print("You win this round!")
            scores["player"] += 1
        else:
            print("AI wins this round!")
            scores["ai"] += 1
            
        print(f"Score -> You: {scores['player']} | AI: {scores['ai']}\n")

if __name__ == "__main__":
    play_game()
