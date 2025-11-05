numero, maximo = 1, 1000
while numero <= maximo:
    if (numero % 3 == 0) and (numero % 5 == 0):
        print("Fizzbuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero += 1