# Programa para planificar una dieta saludable

# Preguntar al usuario su altura en metros y peso en kilogramos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)
print("Su índice de masa corporal es de:", round(imc, 2))

# Aconsejar el objetivo de dieta en función del IMC
if imc < 18.5:
   print("Tu IMC indica que tienes bajo peso. Se recomienda ganar peso")
elif imc >= 18.5 and imc < 25:
    print("Tu IMC indica que tienes un peso saludable. Se recomienda mantener peso")
elif imc >= 25 and imc < 30:
    print("Tu IMC indica que tienes sobrepeso. Se recomienda perder peso")
else:
    print("Tu IMC indica que tienes obesidad. Se recomienda ver a un médico")


# Preguntar al usuario su objetivo de dieta
print("¿Cuál es su objetivo de dieta?")
objetivo = input("Ingrese 'perder', 'mantener' o 'ganar' peso: ")

# Definir las comidas saludables para cada objetivo de dieta
if objetivo == "perder":
    desayuno = "Tazón de avena con frutas y nueces"
    almuerzo = "Ensalada de pollo con verduras y aceite de oliva"
    cena = "Pescado a la parrilla con vegetales asados"
elif objetivo == "mantener":
    desayuno = "Huevos revueltos con aguacate y tostadas integrales"
    almuerzo = "Sándwich de pavo con lechuga y tomate"
    cena = "Pollo a la parrilla con arroz integral y brócoli al vapor"
elif objetivo == "ganar":
    desayuno = "Batido de proteínas con frutas y avena"
    almuerzo = "Arroz integral con frijoles negros y aguacate"
    cena = "Carne magra a la parrilla con batata y espárragos"

# Imprimir las comidas saludables sugeridas
print("\nSugerencias de comidas saludables:")
print("Desayuno: ", desayuno)
print("Almuerzo: ", almuerzo)
print("Cena: ", cena)