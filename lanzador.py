from magia_numerica import magia_numerica

def main():
    print("Bienvenido al programa de magia numérica.")
    print("Escribe 'break' para dejar de introducir números.")
    numeros = []  # Lista para almacenar los números introducidos

    while True:
        entrada = input("Por favor, introduce un número entero: ")
        if entrada.lower() == "break":
            print("Has terminado de introducir números.")
            break
        try:
            numero = int(entrada)
            numeros.append(numero)  # Añadir el número a la lista
        except ValueError:
            print("Error: Debes introducir un número entero válido o 'break' para salir.")

    return numeros  # Devolver la lista de números
