import random

options= ("piedra", "papel", "tijera")

def choose_options():
  user_option= input("piedra, papel o tijera: ")
  user_option= user_option.lower()

  if not user_option in options:
    print("No es una opcion valida")
    return None, None 

  computer_option= random.choice(options)

  print(f"El usuario eligio {user_option}")
  print(f"La computadora eligio {computer_option}")
  return user_option, computer_option 

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Es un empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("El usuario gana")
      user_wins+=1
    else:
      print("El computador gana")
      user_wins+=1

  elif user_option == "papel":
    if computer_option == "piedra":
      print("El usuario gana")
      user_wins +=1
    else:
      print("El computador gana")
      computer_wins +=1

  elif user_option == "tijera":
    if computer_option == "papel":
      print("El usuario gana")
      user_wins +=1
    else:
      print("El computador gana")
      computer_wins +=1
    
  return user_wins, computer_wins

def run_games():
  computer_wins=0
  user_wins=0
  rounds= 1


  while True:
    print("*"*7)
    print("Round", rounds)
    print("*"*7)
  
    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
  
    rounds += 1 
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins= check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 3:
      print("La computadora gana 3 veces seguidas")
      break
    elif user_wins == 3:
      print("El usuario gana 3 veces seguidas")
      break

run_games()