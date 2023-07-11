import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
        try:
            players = int(input("Number of players (2 - 4): "))
            if 2 <= players <= 4:
                break
        except ValueError:
             print("Must be numeric")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"Player number {player_idx + 1} turn has just started!")
        #print("\nPlayer", player_idx + 1, "turn has just started!")
        print(f"Total score is: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("Rolled 1! Turd done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Rolled: {value}")

            print(f"Score is {current_score}")
        
        player_scores[player_idx] += current_score
        print(f"Your score: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player number {winning_idx + 1} is the winner with a score of: {max_score} bebra")