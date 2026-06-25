import random
def jugar_adivina_el_numero():
  print("=================================================")
  print("¡Bienvenido al juego: Adivina el Número Secreto!")
  print("=================================================")
  numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("Ya he pensado en un número entre 1 y 100. ¿Podrás adivinarlo?\n")

while True:
  intento_usuario = int(input("Introduce tu número: "))

intentos = intentos + 1
        
        if intento_usuario == numero_secreto:
            print(f"\n🎉 ¡Felicidades! Has adivinado el número secreto.")
            print(f"Te tomó un total de {intentos} intentos.")
            print("\n[ FIN DEL JUEGO ]")
            break
        else:
            if intento_usuario > numero_secreto:
                print("❌ El número secreto es MENOR. ¡Inténtalo de nuevo!")
            else:
                print("❌ El número secreto es MAYOR. ¡Inténtalo de nuevo!")  

if __name__ == "__main__":
    jugar_adivina_el_numero()
