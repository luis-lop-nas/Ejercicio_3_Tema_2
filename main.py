from lanzador import main
from magia_numerica import magia_numerica

if __name__ == "__main__":
    numeros = main()  # Recoger la lista de números desde lanzador.main()
    if numeros:  # Verificar si la lista no está vacía
        resultado = magia_numerica(numeros)  # Pasar la lista a magia_numerica
        print(f"El resultado de la magia numérica es: {resultado}")
    else:
        print("No se introdujeron números. No hay nada que procesar.")