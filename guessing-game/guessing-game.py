import random

# helper functions

def random_number():
    numb = random.randint(1,100)
    return numb 

def checker(guess,numb):
        
        if guess == numb:
            return "holy fuck cunt! you guessed it right!"
        elif guess > numb:
            return "nah mate, try below"
        else:
            return "oi! ur so low, guess higher"

def main():
    number = random_number()
    attempts = 0
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty == "easy":
        max_attempts = 10
    else:
        max_attempts = 5

    while attempts < max_attempts:
           guess = int(input("enter ur guess: "))
           result = checker(guess, number)
           print(result)
           attempts += 1
           if guess != number:
                print(f"You have {max_attempts - attempts} tries left.")
           if guess == number:
              break
    if guess != number:
         print(f"Out of tries! The number was {number}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
       main()
    else:
       print("Thanks for playing!")


if __name__ == "__main__":
    main()