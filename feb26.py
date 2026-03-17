edad = input("Edad: ")
edad = int(edad) 
while edad < 0:
    print("Edad no valida")
    edad = input("Edad: ")
    edad = int(edad)
if edad < 3:
    print("Bebe")
elif edad>= 26 and edad<60:
    print("Adulto")
elif edad>= 3 and edad<13:
    print("Niño")
elif edad>= 13 and edad<26:
    print("Joven")

else:
    print("Anciano")

# a = input("Ingrese un numero: ")
# a = float(a)  
# b = input("Ingrese un numero: ")
# b = float(b)  
# if a > b:
#     print(f"{a} es mayor que {b}")
# else:
#     print(f"{b} es mayor que {a}")


# lista =[-2 ,-1 ,0 ,1 ,2]
# print(f"lista: {lista}")
# for elemento in lista:
#     print(f"Inicio de Iteracion")
#     if elemento < 0:
#         print("El elemento es negativo")
#     elif elemento > 0:
#         print("El elemento es positivo")
#     else:
#         print("El elemento es cero")
#     print(f"Elemento: {elemento}")
#     print(f"Elemento al cuadrado: {elemento ** 2}")
#     print(f"Fin de Iteracion")