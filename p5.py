import pyttsx3

def mostrar_menu():
    print("¡Bienvenido/a/e al programa de asistencia para personas con discapacidad!")
    print("***LEYES, CUD, TRANSPORTE***")
    print("1. Leyes vigentes en Argentina")
    print("2. Pasos para obtener el C.U.D.")
    print("3. Beneficios en el transporte")
    print("***INTERACCIÓN***")
    print("4. Convertir texto a voz")
    print("5. Realizar operación matemática sencilla")
    print("6. Juego de adivinanzas simple")
    print("7. Calcular el promedio de una lista de números")
    print("8. Salir")

def mostrar_leyes_vigentes():
    print("Leyes vigentes para personas con discapacidad en Argentina:")
    print("- Ley Nacional de Salud Mental (N° 26.657)")
    print("- Ley Nacional de Discapacidad (N° 22.431), sancionada en 1981, dando cuenta de una concepción de la discapacidad con anclaje proteccionista y asistencialista, sin otorgar algun lugar al de sujeto de derecho)")
    print("- Ley de Educación Nacional (N° 26.378)")
    print("- Ley de Empleo para Personas con Discapacidad (N° 22.431)")
    print("- Ley de Accesibilidad (N° 24.314)")
    print("- Ley de Teletrabajo (N° 27.555)")
    print("La Nueva Ley de Discapacidad será una Ley de Derechos Humanos, con perspectiva de género, interseccional e intercultural, que se ampare en los lineamientos del Modelo Social que entiende a la persona primero como persona en el reconocimiento de sus derechos humanos, civiles, políticos y de libertades fundamentales. Fuente:www.https://www.argentina.gob.ar/andis/nueva-ley")



def obtener_cud():
    print("El CUD es un documento público válido en todo el país que\n permite ejercer los derechos y acceder a las prestaciones previstas en las leyes nacionales 22431 y 24901. La evaluación es realizada por una Junta Evaluadora interdisciplinaria que determina si corresponde la emisión del Certificado Único de Discapacidad. Su tramitación es voluntaria y gratuita.")
    print("Para obtener el Certificado Único de Discapacidad (CUD) en Argentina, debes seguir estos pasos:")
    print("1. Solicitar un turno en el Centro de Salud más cercano, puede ser en una salita barrial, hospital o llamndo a un 0 800.")
    print("Más fácil desde la web: https://www.argentina.gob.ar/servicio/como-obtener-el-certificado-unico-de-discapacidad-cud")
    print("2. Presentarte con un mayor de 18 años en la fecha y hora asignadas para realizar la evaluación médica.")
    print("3. Llevar toda la documentación médica necesaria, como informes, estudios, etc.")
    print("4. Completar los formularios requeridos y firmarlos.")
    print("5. Esperar la resolución y retira el CUD en el Centro de Salud.")



def beneficios_transporte():
    print("Los beneficios de transporte para personas con discapacidad en Argentina incluyen:")
    print("- Gratuidad o descuentos en el transporte público (subte, colectivos, trenes) y también espectáculos.")
    print("- Tarifa diferencial en peajes.")
    print("- Estacionamiento preferencial en lugares designados.")
    print("- Transporte adaptado y accesible para personas con movilidad reducida.")
    


def convertir_texto_a_voz():
    texto = input("Ingrese el texto que desea convertir a voz: ")
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def realizar_operacion_matematica():
    print("¡Bienvenido/a/e a la calculadora matemática!")
    print("Ingrese 'salir' para salir de la calculadora.")
    
    while True:
        operacion = input("Ingrese la operación matemática que desea realizar (+, -, *, /): ")
        if operacion.lower() == "salir":
            print("¡Gracias por utilizar la calculadora!")
            break
        elif operacion not in ["+", "-", "*", "/"]:
            print("Operación inválida. Por favor, intente nuevamente.")
            continue
        else:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
            
            if operacion == "+":
                resultado = numero1 + numero2
                print(f"La suma de {numero1} y {numero2} es: {resultado}")
            elif operacion == "-":
                resultado = numero1 - numero2
                print(f"La resta de {numero1} y {numero2} es: {resultado}")
            elif operacion == "*":
                resultado = numero1 * numero2
                print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
            elif operacion == "/":
                if numero2 != 0:
                    resultado = numero1 / numero2
                    print(f"La división de {numero1} entre {numero2} es: {resultado}")
                else:
                    print("Error: No se puede dividir entre cero.")
            
    
def jugar_adivinanzas():
    print("¡Bienvenido/a/e al juego de adivinanzas!")
    print("Tratá de adivinar la respuesta correcta. Ingresa 'salir' para salir del juego.")
    adivinanza = "¿Cual es el animal del fin?"
    respuesta_correcta = "el delfin"
    intentos = 0
    while True:
        respuesta = input("Adivinanza: " + adivinanza + "\nTu respuesta: ")
        intentos += 1
        if respuesta.lower() == respuesta_correcta:
            print("¡Respuesta correcta! ¡Has ganado en", intentos, "intentos!")
            break
        elif respuesta.lower() == "salir":
            print("¡Gracias por jugar!")
            break
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")

def calcular_promedio():
    numeros = []
    cantidad = int(input("Ingrese la cantidad de números: "))
    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)
    promedio = sum(numeros) / cantidad
    print(f"El promedio de los números ingresados es: {promedio}")


def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción que desea ejecutar: "))
        if opcion == 1:
            mostrar_leyes_vigentes()
        elif opcion == 2:
            obtener_cud()
        elif opcion == 3:
            beneficios_transporte()
        elif opcion == 4:
            convertir_texto_a_voz()
        elif opcion == 5:
            realizar_operacion_matematica()
        elif opcion == 6:
            jugar_adivinanzas()
        elif opcion == 7:
            calcular_promedio()
        elif opcion == 8:
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


ejecutar_programa()