while True:
    try:
        num = int(input("Ingrese un número: "))
        inverso = 1 / num
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
    except ZeroDivisionError:
        print("No se puede calcular el inverso de cero. Por favor, ingrese un número diferente de cero.")
    except:
        print("Ocurrió un error inesperado. Por favor, intente nuevamente.")
print(f"El inverso de {num} es: {inverso}")

# while True:
#     try:
#         num = int(input("Ingrese un número: "))
#         break
#     except ValueError:
#         print("Por favor, ingrese un número entero válido.")
# for i in range(11):
#     print(f"{num} x {i} = {num * i}")