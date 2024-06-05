#while
sumatoria_guaguas=0.0
contador_mora=0
contador_guaguas=0

print("--------LA UNION----------")
num_guaguas= int(input("ingrese el numero de guaguas de pan que desea: "))

while contador_guaguas<num_guaguas:
    precio_guagua=float(input(f"ingresa el precio de la guagua {contador_guaguas+1}: "))
    sumatoria_guaguas += precio_guagua
    print("la guagua es de mora")
    tipo_guagua= input("si o no: ")

    if tipo_guagua == "si":
        contador_mora += 1
    contador_guaguas += 1

print("el pago a realizar...")
print(f"el total de guaguas es {num_guaguas}")
print(f"el precio final de guaguas es {sumatoria_guaguas}")
print(f"las guaguas de mora son {contador_mora}")
print("-----------GRACIAS POR SU COMPRA------------")