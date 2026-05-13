print("Digite qualquer número natural que matemáticamente vou levar ele a ser igual a 1 , segundo a conjectura de Collatz ")
num = float(input("Digite um número(número natural):"))

while num <= 0:
    num = float(input("Digite um número maior e diferente de zero:"))

passo = 0
while num != 1:
    passo += 1
    anterior = num
    if (num % 2) == 0:
        num = num // 2
        print(f"Passo {passo}: {int(anterior)} ÷ 2 = {int(num)}")
    else:
        num = (num * 3 + 1)
        print(f"Passo {passo}: {int(anterior)} x 3 + 1 = {int(num)}")

print(f"\n Chegou a 1 após {passo} passos!")
