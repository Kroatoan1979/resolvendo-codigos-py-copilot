"""
Prompts the user to input a string and an integer, then prints the string followed by a newline character repeated the number of times specified by the integer.

Parameters:
- string (str): The input string provided by the user.
- numero (int): The integer input provided by the user.

Returns:
- None
"""

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print((string + "\n")* numero)