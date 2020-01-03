#------------------------------
#Fucntions
# def hello(name):
#     print('Howdy!' + name)
#     print('Howdy!!!' + name)
#     print('Hello, ' + name)
# hello('Javi') 
#-------------------------------

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)
        return number

print('Enter number')
number = int(input())
while(number != 1):
    number = collatz(number)