#!/usr/bin/env python3
from random import randint
from replit import clear

from rich import print
from rich.console import Console

def guessANumber():
    clear()
    console = Console()
    answer = intro() 
    attempts = chooseDifficulty()

    while True:
        print(f"You have [blue]{attempts}[/] attempts")
        guess = guessNumber()
        attempts = compare(guess, answer, attempts)
        if attempts == 0:
            print("[blue] Right answer is: ", answer)
            print("[red]You limit attempts")
            break
        elif attempts == 'win':
            print("[green]You win")
            break

    try_again = console.input("[green]Do you want to try again? y/n: ")
    if try_again == 'y':
        guessANumber()
    else:
        exit()


def intro():
    print("[green]Welcome to the Number Guessing Game!")
    print("[blue]I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"[red] Pssss, answer is {answer}")
    return answer

def chooseDifficulty():
    console = Console()
    print("Choose a difficulty. Type '[green]easy[/]' or '[blue]hard[/]': ")
    difficulty = console.input("")
    if difficulty == 'easy':
        return 10
    else:
        return 5

def guessNumber():
    return int(input("Make a guess: "))

def compare(guess, answer, attempts):
    attempts = attempts - 1
    if guess > answer:
        print("[yellow]Too hight")
        return attempts
    elif guess < answer: 
        print("[blue]Too low")
        return attempts
    elif guess == answer:
        return 'win'

guessANumber()
