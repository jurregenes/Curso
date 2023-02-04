sairExercicio = False

while sairExercicio == False:

    print("Exercicio 1: Faca um Programa que mostre a mensagem 'Ola Mundo' na tela")
    print("Exercicio 2: Faca um programa que peca um numero e entao mostre a mensagem. O numero informado foi numero")
    print("Exercicio 3: Faca um programa que peca dois numeros e imprima a soma")
    print("Exercicio 4: Faca um programa que peca as 4 notas bimestrais e mostre a media")

    exercicios = input("Digite o numero do exercicio: (1 - Exercicio 1, 2 - Exercicio 2, 3 - Exercicio 3, 4 - Exercicio 4)")
    exercicios = int(exercicios)

    if exercicios == 1: 
        print("Ola Mundo!") 

    if exercicios == 2:
        numero =  input("Digite um numero: ")
        numero2 = int(numero)
        print("O numero digitado foi: ", numero2) 

    if exercicios == 3:

        print("calculadora")

        sair = False

        while sair == False:
            valor1 = input("Digite o primeiro numero: ")
            valor1 = int(valor1)
            operador = input("Digite o operador (+-/*): ")
            valor2 = input("Digite o segundo numero: ")
            valor2 = int(valor2)

            #soma   
            if operador == "+":
                operacao = valor1 + valor2

            #subtracao       
            if operador == "-":
                operacao = valor1 - valor2

            #divisao           
            if operador == "/":
                operacao = valor1 / valor2

            #multiplicacao           
            if operador == "*":
                operacao = valor1 * valor2

            print("resultado: ")
            print(operacao)

            teste = input("Deseja sair (n/s): ")
            if teste == "s":
                sair = True

    if exercicios == 4:
        nota1 = input("informe a primeira nota: ")
        nota1 = int(nota1)
        nota2 = input("informe a segunda nota: ")
        nota2 = int(nota2)
        nota3 = input("informe a terceira nota: ")
        nota3 = int(nota3)
        nota4 = input("informe a quarta nota: ")
        nota4 = int(nota4)

        media = (nota1 + nota2 + nota3 + nota4) /4
        print("Sua media final e: ", media) 

    sairExercicio2 = input("Deseja sair (s/n): ")
    if sairExercicio2  == "s":
        sairExercicio = True