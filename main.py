contador = 0 #contador de divisores, comienza siendo cero

def es_primo(numero):
    global contador  ## para poder usar la variable contador en la funcion
    for divisores in range(1, numero+1):
        if numero % divisores == 0:
            contador += 1
    return contador

numero = int(input("Escribe un número entero: "))
es_primo(numero)

if contador == 1:
    print("El número", numero, "tiene", contador, "divisor. Es primo.")
elif contador == 2:
    print("El número", numero, "tiene", contador, "divisores. Es primo.")
else:
    print("El número", numero, "tiene", contador, "divisores. No es primo.")