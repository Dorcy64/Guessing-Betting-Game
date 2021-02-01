import random 
from art import logo
from replit import clear
import math

BET = 0
BALANCE = 2500
ROUNDS = 0

def start():
	global ROUNDS
	global BET
	global CASHMORE

	print(logo)
	print(f"Your current balance is ${BALANCE}, in order to check out you need to $10,000")
	BET = int(input("How much do you want to bet? : $"))
	pick = int(input("Pick a number between 1 and 5 : "))
	ROUNDS += 1
	return pick

def game():
	global BET
	global BALANCE
	global ROUNDS

	choice = random.randint(0, 5)
	number_chosen = start()

	if choice == number_chosen:
		print(f"You win the correct number was {choice}")
		BALANCE += BET
		print(f"\nCurrent balance is ${BALANCE}\n")

	elif choice != number_chosen:
		print(f"One more attempt")
		new_number = int(input(f"Pick one more number between 1 and 5 : "))
		ROUNDS += 1

		if new_number == choice:
			print(f"You win the correct number was {choice}")
			BALANCE += BET
			print(f"\nCurrent balance is ${BALANCE}\n")

		else:
			print(f"You lose the correct number was {choice}")
			BALANCE -= BET
			print(f"\nCurrent balance is ${BALANCE}\n")

	while BALANCE < 10000 and BALANCE > 0:
		go_again = input("Press return or enter to Contiue ") 
		clear()
		game()
	
	while BALANCE >= 10000:
		do_checkout = input(f"Do you want to check out current balance is ${BALANCE}? 'y' to check out / 'n' to contiune : ")
		while do_checkout != "y":
			clear()
			game()
  
	while BALANCE <= 0:
		tries = float(f"{0.}{ROUNDS}")
		go_again = input(f"You guessed a total of {ROUNDS} tries and lost $2500, \npress Enter or Return to try again") 

		BALANCE = 2500
		ROUNDS = 0
		clear()
		game()


	



game()



