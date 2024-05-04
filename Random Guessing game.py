import random

def guess_number(starting_number = 1, ending_number = 100): # Making the range of numbers configurable 
    random_number = random.randint(starting_number,ending_number) 
    guess_list = []
    while True:
        try:
            human_guess = int(input(f"Enter a number between {starting_number} and {ending_number} as a guess -->  "))
            difference_large  = 'Way larger' if human_guess - random_number > (ending_number//4) else "Slightly larger" # Scalable Threshold 
            difference_lower  = 'Way lower' if random_number - human_guess > (ending_number//4) else "Slightly lower"   
            guess_list.append(human_guess)
            if human_guess>random_number:
                print(f"You went {difference_large} than the number, try a lower guess!")
                continue
            elif human_guess<random_number:
                print(f"You went {difference_lower} than the number, try a higher guess!")
                continue
            else:
                print(f"Congrats you have guessed the number --> {random_number}")
                print(f"path taken: {guess_list}")
                break
        except ValueError:
            print("Please enter a valid number")


guess_number()


