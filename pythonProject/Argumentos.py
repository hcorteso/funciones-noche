# Ejemplo de argumentos predeterminados

def my_function(country = "Colombia"):
    print("I a from " + country)

#Invocar la funcion
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: " + args[2])

mostrarEstudiantes("Emil", "Tobias", "Linus")

#Argumentos de palabras claves
def mostrarCarros(carro1, carro2, carro3):
    print("El carro es : " + carro2)

mostrarCarros(carro1 = "BMW", carro3= "Ferrari", carro2= "Ford")

# Argumento arbitrario
def mostrarClinete(**kwargs):
    print("Su apellido es: " + kwargs["apellido"])

mostrarClinete(nombre= "tobias", apellido= "Refsnes")