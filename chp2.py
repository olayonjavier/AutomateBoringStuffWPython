#------------------------------------------------------------------------------------
#While loops, continues, and breaks
#while True:
#    print("Who are you?")
#    name = input()
#    if name != 'Joe':
#        continue
#    print("Hello Joe. What is the password? (it is a fish)")
#    password = input()
#    if password == 'swordfish':
#        break
#print('Acess granted.')
#------------------------------------------------------------------------------------
#Truthsy falsesy
# name = ''
# while not name:
#     print('Enter your name')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room')
# print('Done') 
#------------------------------------------------------------------------------------
#imports
# from random import *
# for i in range(5): 
#     print(randint(1, 10))
#------------------------------------------------------------------------------------
#Guess the number game
# import random
# target = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20')
# print('Take a guess')
# guess = int(input())
# counter = 1
# while guess != target:
#     if guess < target:
#         print('Your guess is too low')
#     elif guess > target:
#         print("Your guess is too high")
#     print('Take a guess')
#     guess = int(input())
#     counter = counter + 1
# print('Good job, you guessed the number in ' + str(counter) + ' guess!')
#------------------------------------------------------------------------------------
#Rock Paper Scissors
#import random
#while True: