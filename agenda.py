# Programa: Agenda de contactos

# 1. Crear diccionario
contactos = {}

# 2. Agregar datos
contactos["Ana"] = "0991234567"
contactos["Luis"] = "0987654321"
contactos["Carlos"] = "0971112233"

# 3. Mostrar todos los contactos
print("Lista de contactos:")
for nombre, numero in contactos.items():
    print(nombre, ":", numero)

# 4. Buscar un contacto
buscar = "Ana"
print("\nBuscando contacto:", buscar)
print("Número:", contactos.get(buscar))

# 5. Eliminar un contacto
eliminar = "Luis"
contactos.pop(eliminar)

print("\nContactos después de eliminar:")
for nombre, numero in contactos.items():
    print(nombre, ":", numero)
