# Programa para planificar una dieta saludable basado en el IMC

# Definir las comidas saludables para cada objetivo de dieta
comidas_saludables = {
    "perder": {
        "Desayuno": "Tazón de avena con frutas y nueces",
        "Almuerzo": "Ensalada de pollo con verduras y aceite de oliva",
        "Cena": "Pescado a la parrilla con vegetales asados"
    },
    "mantener": {
        "Desayuno": "Huevos revueltos con aguacate y tostadas integrales",
        "Almuerzo": "Sándwich de pavo con lechuga y tomate",
        "Cena": "Pollo a la parrilla con arroz integral y brócoli al vapor"
    },
    "ganar": {
        "Desayuno": "Batido de proteínas con frutas y avena",
        "Almuerzo": "Arroz integral con frijoles negros y aguacate",
        "Cena": "Carne magra a la parrilla con batata y espárragos"
    }
}

# Preguntar al usuario su altura en metros y peso en kilogramos
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)
print("Su índice de masa corporal es de:", round(imc, 2))

# Definir el objetivo de dieta en función del IMC
if imc < 18.5:
    objetivo = "ganar"
    print("Tu IMC indica que tienes bajo peso.")
elif imc >= 18.5 and imc < 25:
    objetivo = "mantener"
    print("Tu IMC indica que tienes un peso saludable.")
elif imc >= 25 and imc < 30:
    objetivo = "perder"
    print("Tu IMC indica que tienes sobrepeso.")
else:
    objetivo = "perder"
    print("Tu IMC indica que tienes obesidad.")

# Imprimir las comidas saludables sugeridas
print("\nSugerencias de comidas saludables para tu objetivo de dieta:")
print("Desayuno: ", comidas_saludables[objetivo]["Desayuno"])
print("Almuerzo: ", comidas_saludables[objetivo]["Almuerzo"])
print("Cena: ", comidas_saludables[objetivo]["Cena"])