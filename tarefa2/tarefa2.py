sairExercicio = False

while sairExercicio == False:

    print("Exercicio 1: Faca uma lista")
    print("Exercicio 2: Faca um indice")
    print("Exercicio 3: Acesse os itens atraves da posicao negativa")
    print("Exercicio 4: Alterando itens")
    print("Exercicio 5: Acrescentando itens")
    print("Exercicio 6: Inseriendo na lista")
    print("Exercicio 7: Removendo itens")
    print("Exercicio 8: Remove")
    print("Exercicio 9: Sort")
    print("Exercicio 10: Sorted")
    print("Exercicio 12: Reverse")
    print("Exercicio 13: Exibir o tamanho de uma lista")
    print("Exercicio 14: Criar uma lista de numero")
    print("Exercicio 15: Menor Valor")
    print("Exercicio 16: Maior valor")
    print("Exercicio 17: Fatia de uma lista")
    print("Exercicio 18: Parar uma lista")

    
    exercicios = input("Digite o numero do exercicio: (1 - Exercicio 1, 2 - Exercicio 2, 3 - Exercicio 3, 4 - Exercicio 4, 5 - Exercicio 5, 6 - Exercicio 6, 7 - Exercicio 7, 8 - Exercicio 8, 9 - Exercicio 9, 10 - Exercicio 10, 11 - Exercicio 11, 12 - Exercicio 12, 13 - Exercicio 13, 14 - Exercicio 14, 15 - Exercicio 15, 16 - Exercicio 16, 17 - Exercicio 17, 18 - Exercicio 18,)")
    exercicios = int(exercicios)

    if exercicios == 1: 
        convidados = ["Joao","Maria","Julia"]
        print(convidados)


    if exercicios == 2: 
        convidados = ["Joao","Maria","Julia"]
        print("Primeiro convidado da festa: + convidados [1] ")

    if exercicios == 3: 
        convidados = ["Joao","Maria","Julia"]
        print("Primeiro convidado da festa: + convidados [-2] ")

        

    if exercicios == 4: 
        convidados = ["Joao","Maria","Julia"]
        convidados [0] = "Isabela"  
        print("convidados")      

    if exercicios == 5: 
        convidados = ["Joao","Maria","julia"]
        convidados.append ("joaquim")
        print("conviados")
    

    if exercicios == 6: 
        convidados = ["Joao","Maria","Julia"]
        convidados.insert (0,"Zaida")
        print("convidados")
        


    if exercicios == 7: 
        convidados = ["Joao","Maria","julia"]
        convidadosremovidos = convidados.pop (0)
        print(convidadosremovidos)

        

    if exercicios == 8: 
        convidado = ["Joao","Maria","Julia"]
        viajando = "Joao"
        convidado.remove (viajando)
        print("convidado")
        

    if exercicios == 9: 
        

    if exercicios == 10: 
        

    if exercicios == 11: 
        

    if exercicios == 12: 
        

    if exercicios == 13: 
        

    if exercicios == 14: 
        

    if exercicios == 15: 
        

    if exercicios == 16: 
        

    if exercicios == 17: 
        

    if exercicios == 18: 
        


    sairExercicio2 = input("Deseja sair (s/n): ")
    if sairExercicio2  == "s":
        sairExercicio = True
