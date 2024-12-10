import random
import diceRoll
import tupleOut
import fixedDice

# [peer edit (nakshatra)]: at the bottom of each function, don't forget to run a test calling the function and comment it out. 
def player_turn(player, scores):
    print(f"\nPlayer {player + 1}'s turn ==============================================================================================")
    roll = diceRoll.dice_roll()
    if_fixed = fixedDice.fixed_dice(roll)

    while True:
        print(f"Dice rolled: {roll}")

        if tupleOut.tuple_out(roll):
            print("You tupled out! Your score for this round is 0 :(")
            return 0
        if if_fixed:
            print(f"{[roll[i] for i in if_fixed]}")
        reroll_chance = input("\nDo you want to reroll? (yes/no): ").strip().lower()
        if reroll_chance == 'no':
            total_score = sum(roll)
            print(f"Scored {total_score} points")
            return total_score
        
        for i in range(3):
            if i not in if_fixed:
                roll[i] = random.randint(1, 6)
        if_fixed = fixedDice.fixed_dice(roll)
        # add tests here and comment them out to meet requirements for final submission

def game(target_score):
    scores = [0, 0]
    current_player = 0

    while all(score < target_score for score in scores):
        print(f"\nScores: \nPlayer 1 = {scores[0]}, Player 2 = {scores[1]}")
        turn_score = player_turn(current_player, scores)
        scores[current_player] += turn_score
        current_player = 1 - current_player

    if scores[0] >= target_score:
        winner = 1
    else:
        winner = 2 
    # add test for game function
    
    print(f"\nFinal Scores: Player 1 = {scores[0]}, Player 2 = {scores[1]}")
    print(f"Player {winner} wins!")

game(target_score = 50)