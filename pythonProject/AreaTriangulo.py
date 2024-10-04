#Ejemplo para calcular el ara del triangulo

# Entradas
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))

# Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    #print("El area del triangulo es: ",area)
    return area

calcularAreaTriangulo(base,altura)
resultado = calcularAreaTriangulo(base,altura)
print(f"El area del triangulo es: {resultado}")
