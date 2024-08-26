#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print (f'{i}')
        i -= 1
    else:
        print ("Happy New Year!") 

def square_integers(int_list):
    squares = [integer * integer for integer in int_list]
    return squares

def fizzbuzz():
    i = 1
    while i < 101:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

fizzbuzz()
    
