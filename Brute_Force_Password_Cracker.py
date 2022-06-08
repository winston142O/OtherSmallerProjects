import random
from random import *
import pyautogui
import os
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','A',
            'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z','!','_']

guess = ""
password = guess

password = pyautogui.password("Enter a password: ")

while guess != password:
    guess = ""
    for letter in range(len(password)):
        guess_letter = letters[randint(0, 62)]
        guess = str(guess_letter) + str(guess)
    print("=========="+ guess +"==========")

if guess == password:
    print("========== La contrsseña es "+ guess +"==========")

print("La contraseña es: ", guess)


