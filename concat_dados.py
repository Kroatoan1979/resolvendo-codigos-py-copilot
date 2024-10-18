"""
Concatenates two input strings and prints the result.

Prompts the user to enter two pieces of information, concatenates them with a space in between, and displays the concatenated string.

Inputs:
- info1: string, the first piece of information entered by the user.
- info2: string, the second piece of information entered by the user.

Output:
- Concatenated string of info1 and info2.
"""

info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")

info_concatenada = info1 + " " + info2

print("As informações concatenadas são: ", info_concatenada)
