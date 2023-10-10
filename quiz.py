print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")

print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Respostas: ")

if answer_1 =="A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl John \n (C) Carlos Jaqueline \n (D) Carlos Johnson \n")
answer_2 = input("Respostas: ")

if answer_2 =="B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print(f"Quiz acabou...  Portuação: {score}/2")