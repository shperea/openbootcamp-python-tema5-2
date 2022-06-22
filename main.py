contador = 0 #contador de divisores, comienza siendo cero

def es_primo(numero):
    global contador  ## para poder usar la variable contador en la funcion
    for divisores in range(1, numero+1):
        if numero % divisores == 0:
            contador += 1
    return contador

es_primo(int(input("Escribe un número entero: ")))

if contador == 1:
    print("Tu número tiene", contador, "divisor. Es primo.")
elif contador == 2:
    print("Tu número tiene", contador, "divisores. Es primo.")
else:
    print("Tu número tiene", contador, "divisores. No es primo.")