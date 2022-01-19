import random

top_of_range = input(" type a number: ")

#making sure the input is integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('Please type a number greater then 0 next time ')
        quit()
else:
    print('Please type a number net time')
    quit()


random_number = (random.randint(0,top_of_range))
#print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please type a number next time')
        continue
    #print('after continue')
    if user_guess == random_number:
        print('You got it')
        break
    
    elif user_guess > random_number:
        print('you were above the number!')
    else:
        print('you were below the number!')
    


print('You got it in', guesses, 'guesses')