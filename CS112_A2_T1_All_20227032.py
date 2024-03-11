# File: CS112_A2_T1_All_20227032.py
# Purpose: 100 game. Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Hossam Anwar Alsayed Mahmoud
#ID: 20227032

def display_game_status(sum):
    print("Current sum:", sum)

def check_valid_play(num, sum):
    if num < 1 or num > 10:
        return False
    if sum + num > 100:
        return False
    return True

def check_game_over(sum):
    if sum == 100:
        return True
    return False

def play_game():
    sum = 0
    display_game_status(sum)

    while True:
        # First player plays
        num = int(input("Player 1, enter a number from 1 to 10: "))
        while not check_valid_play(num, sum):
            print("Invalid play. Try again.")
            num = int(input("Player 1, enter a number from 1 to 10: "))
        sum += num
        display_game_status(sum)
        if check_game_over(sum):
            print("Player 1 wins!")
            break

        # Second player plays
        num = int(input("Player 2, enter a number from 1 to 10: "))
        while not check_valid_play(num, sum):
            print("Invalid play. Try again.")
            num = int(input("Player 2, enter a number from 1 to 10: "))
        sum += num
        display_game_status(sum)
        if check_game_over(sum):
            print("Player 2 wins!")
            break

play_game()