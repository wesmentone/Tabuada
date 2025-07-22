num = int(input("digite um número (de 1 a 10):\n"))
if num >= 10:
    print ("número inválido, digite um número de 1 a 10.")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
