# Importamos las librerías necesarias
import openai
import pyttsx3

# Preguntamos Por La Api De OpenAI
Api = input("\nIngrese su Api Key: ")

# Establecemos la clave de API para OpenAI
openai.api_key = Api

# Inicializamos el motor de texto a voz de pyttsx3
engine = pyttsx3.init()

# Iniciamos un bucle infinito que permite hacer múltiples preguntas y obtener respuestas
while True:
    # Pedimos al usuario que ingrese una pregunta
    pregunta = input("\nIngrese su pregunta: ")

    # Utilizamos OpenAI para completar la respuesta a la pregunta
    completado = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pregunta,
        max_tokens=2048
    )
    respuesta = (completado.choices[0].text)
    print(respuesta)

    # Preguntamos al usuario si desea escuchar la respuesta
    reproducir = input("\n¿Desea que se lea la respuesta?"+"\nDigite [SI] para aceptar\nDigite [NO] para cancelar\nIngrese opción: ")
    reproducir_lower = reproducir.lower()

    if reproducir_lower == "si":
        # Si el usuario desea escuchar la respuesta, utilizamos pyttsx3 para reproducirla
        engine.say(respuesta)
        engine.runAndWait()

        # Preguntamos al usuario si desea salir del programa
        salir = input("\n¿Desea salir?"+"\nDigite [SI] para aceptar\nDigite [NO] para cancelar\nIngrese opción: ")
        salir_lower = salir.lower()
        if salir_lower == "si":
            # Si el usuario desea salir, salimos del bucle y terminamos el programa
            break
        elif salir_lower == "no":
            # Si el usuario no desea salir, continuamos el bucle
            continue
        else:
            # Si el usuario ingresa una opción inválida, lo notificamos y continuamos el bucle
            print("\nOpción inválida")

    elif reproducir_lower == "no":
        # Si el usuario no desea escuchar la respuesta, lo notificamos y preguntamos si desea salir del programa
        salir = input("\n¿Desea salir?"+"\nDigite [SI] para aceptar\nDigite [NO] para cancelar\nIngrese opción: ")
        salir_lower = salir.lower()
        if salir_lower == "si":
            # Si el usuario desea salir, salimos del bucle y terminamos el programa
            print("\nGracias por usar el programa")
            break
        elif salir_lower == "no":
            # Si el usuario no desea salir, continuamos el bucle
            continue
        else:
            # Si el usuario ingresa una opción inválida, lo notificamos y continuamos el bucle
            print("\nOpción inválida")
            continue

    else:
        # Si el usuario ingresa una opción inválida, lo notificamos y preguntamos si desea salir del programa
        print("\nOpción inválida")
        salir = input("\n¿Desea salir?"+"\nDigite [SI] para aceptar\nDigite [NO] para cancelar\nIngrese opción: ")
        salir_lower = salir.lower()
        if salir_lower == "si":
            # Si el usuario desea salir, salimos del bucle y terminamos el programa
            print("\nGracias por usar el programa")
            break
        elif salir_lower == "no":
            # Si el usuario no desea salir, continuamos el bucle
            continue
        else:
            # Si el usuario ingresa una opción inválida, lo notificamos y continuamos el bucle
            print("\nOpción inválida")
            continue