#for
contador_habitacion=0
for i in range(1,6):
    print(f"¿la luz de la habiatacion {i} se encuentra prendida o apagada?")
    estado_habitacion = input("si o no: ")
    if estado_habitacion == "si":
        contador_habitacion += 1 #contador_habitacion = contador_habitacion + 1

if contador_habitacion >= 2:
    print("alertar al usuario") 

#while
contador_habitacion_luz = 0
num_habiatciones = 1
while num_habiatciones <= 5:
    print(f"¿la luz de la habiatacion {num_habiatciones} se encuentra prendida o apagada?")
    estado_habitacion = input("si o no: ")
    if estado_habitacion == "si":
        contador_habitacion_luz += 1 #contador_habitacion = contador_habitacion + 1
    num_habiatciones += 1 #ojo con la ubicacion de ese algo

if contador_habitacion_luz >= 2:
    print("alertar al usuario")