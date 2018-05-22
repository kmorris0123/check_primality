import os


os.system('clear')
print("This will check all numbers up to the one inputed to see if they are prime numbers or not.")


def get_number():
	print("")
	return int(input("Input a number: "))



def prime(number):
	if number > 1:
		for i in range(2,number+1):
			if (number % i) == 0:
				print(str(i)+" is not a prime number")

			else:
				print(str(i) + " is a prime number")

def main():
	play = True

	while play == True:

		num = get_number()
		prime(num)

		play_again = input('Do you want to enter another number? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False





if __name__ == '__main__':
	main()