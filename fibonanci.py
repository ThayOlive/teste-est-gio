


n = int(input("Informe o número:"))
a = 0
b = 1


if (n==0) or (n==1):
        print("Esse número pertence a sequência")
else:
        for count in range(2,n):
            number = a + b
            b = a
            a = number
            print(number)
if number == n :
    print("Esse numero pertence a sequencia")
else:
    print("Esse numero não pertence a sequencia")
        