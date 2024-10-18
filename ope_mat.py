'''
This program allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. 
The user is prompted to choose an operation and input two numbers. 
The program then displays the result of the chosen operation. Division by zero is handled with an error message. 
'''

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero não é permitida"
    return x / y

def calcular():
    print("Escolhe a operação:")
    print("+ - Adição")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    
    escolha = input("Escolhe a operação | + | - | * | / |\n")

    if escolha in ['+', '-', '*', '/']:
        num1 = float(input("Introduz o primeiro número: "))
        num2 = float(input("Introduz o segundo número: "))
        
        if escolha == '+':
            print(f"O resultado é: {adicao(num1, num2)}")
        elif escolha == '-':
            print(f"O resultado é: {subtracao(num1, num2)}")
        elif escolha == '*':
            print(f"O resultado é: {multiplicacao(num1, num2)}")
        elif escolha == '/':
            print(f"O resultado é: {divisao(num1, num2)}")
    else:
        print("Escolha inválida!")

if __name__ == "__main__":
    calcular()
