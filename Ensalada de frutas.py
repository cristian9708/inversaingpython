# Lista para almacenar las frutas
frutas = []

# Ingreso de las 10 frutas
print("Ingrese los datos de 10 frutas:")
for i in range(10):
    nombre = input(f"Ingrese el nombre de la fruta #{i+1}: ")
    while True:
        try:
            precio = float(input(f"Ingrese el precio de la fruta #{i+1}: "))
            break
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    
    # Crear un diccionario con los datos de la fruta y añadirlo a la lista
    fruta = {"nombre": nombre, "precio": precio}
    frutas.append(fruta)

# Ordenamiento por precio (de mayor a menor) usando el método de burbuja
n = len(frutas)
for i in range(n - 1):
    for j in range(n - i - 1):
        if frutas[j]["precio"] < frutas[j + 1]["precio"]:
            # Intercambiar las posiciones si no están en el orden correcto
            frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]

# Mostrar las frutas ordenadas
print("\nFrutas ordenadas por precio (de mayor a menor):")
for fruta in frutas:
    print(f"Nombre: {fruta['nombre']}, Precio: ${fruta['precio']}")
