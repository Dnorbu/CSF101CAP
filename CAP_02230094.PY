# Dorji Norbu
# 1st ECE
# 02230094

# REFERENCES
# @CHAT_GPT
# @DQ-Logo

# SOLUTION
# Your Solution Score: 49524
# trauma/input_4_cap1.txt(49524)

# Read the input.txt file
def read_input(Input_your_file_name):
    x = []
    with open(Input_your_file_name, 'r') as files:
        for y in files:
            opponent_choice, outcome = y.split()
            x.append((opponent_choice, outcome))
    return x

# Calculate the score for each round
def calculate_score(Total_Number_of_rounds):
    Score = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  #In order to lose
            if opponent_choice == 'A':
                Score += 3  # if Rock defeats scissors
            elif opponent_choice == 'B':
                Score += 1  # if paper defeats rock
            elif opponent_choice == 'C':
                Score += 2  # if scissprs defeats paper
        elif outcome == 'Y':  # In order to draw
            if opponent_choice == 'A':
                Score += 4  # if Rock draws with Rock
            elif opponent_choice == 'B':
                Score += 5  # if Paper draws with Paper
            elif opponent_choice == 'C':
                Score += 6  # if Scissors draws with Scissors
        elif outcome == 'Z':  #In order to win
            if opponent_choice == 'A':
                Score += 8  # if rock loses to paper
            elif opponent_choice == 'B':
                Score += 9  # if paper loses to scissors
            elif opponent_choice == 'C':
                Score += 7  # if Scissors loses to rocl
    print(f"The total score is:{Score}")

# To run a program
Input_your_file_name = "CSF101CAP/input_4_cap1 (1).txt"  # Change this according to your student number
calculate_score(read_input(Input_your_file_name))