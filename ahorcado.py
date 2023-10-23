import random 
import os
def game():
    pala = []
    with open("./archivos/list_of_game.txt", 'r', encoding="utf-8") as f: #solicita el archivo de nombres
        for line in f:
            
            pala.append(str(line))

    # convertir el string en una lista de caracteres 
    word = random.choice((pala)) # elegi al azar un nombre de la lista
    word = word.upper() # convierte en mayuscula 
    word = word.replace(" ","") #elimina los espacios vacios
    word = word.replace("\n","") # elimina los saltos de linea
    word =list(word) #  LUZ = "L","U","Z"
   

    first_part = [ "      #=======|",
                   "              |",
                   "              |",
                   "              |",
                   "              |", 
                   "              |",
                   "              |",]
   
    second_part =[ "      #=======|",
                   "      O       |",                 
                   "     /|\      |",                 
                   "      !       |",                 
                   "     / \      |",
                   "              |",]
    
    word_used =[] # lista para guardar las letras ya usadas
    fall = 1
    guiones = [] #lista para guardar los guiones de la palabra

    for i in range(len(word)):
        guiones.append("_")

    while True:
        os.system('cls')
       
        print("|_|_|_|_|_|Welcome to Ahorcado|_|_|_|_|_|")
        print("\n")
       
        
        for i in range(fall):    # imprime la primera parte de second part  -----|
            print(second_part[i]) 
        for i in range(len(first_part)-fall): # imprime la lista first_part menos  la primera
            print(first_part[i + fall])
        
        print("\n")
        #
        
        for i in guiones:   # _ _ _ _ _ _ en la pantalla
            print(i, end=" ")
        
        # comprobacion si la palabra es correcta
        if guiones == word:
            print("####     WIN       ####")
            break 
        # conteo de fallos en el juego
        if fall > 5:
            print("  the word is ", "".join(word))
            print("##### GAME OVER ####")
            break

            # La estructura principal del juego  
        while True:
            word_user = input("Say any letter: ")
            word_user = word_user.upper()
            if len(word_user) != 1:
                print("please one letter")
            elif word_user in word_used:
                print(" That letter already has used ") 
            elif word_user not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                print("please one letter") 
            else:
                word_used.append(word_user)
                break

        # Comprobar la letra si esta en la palabra entoces se sustituye por el guion    
        
        for i in range(len(word)):
            if word[i] == word_user:
                guiones[i] = word_user

        if word_user not in word:
            fall += 1        

    print("\n")
    print("\n")

def files():
    os.system('cls')
    guarda = []
    for i in range(1,6):
        sss = input("inserta 5 nombres para jugar: ")
    
        print("el " + str(i) + " nombre" )
        guarda.append(sss)
        

    os.system('cls')

    

    with open('./archivos/list_of_game.txt', 'w' , encoding="utf-8") as f:
        for names in guarda:
            f.write(names)
            f.write('\n')


def run():
    print("          !!!!!! Ahorcado GAME!!!!!             ")

    print("      1- GAME PLAY   ")
    print("      2- CONFIG      ")
    print("      3- EXIT        ")
    
    
    option = (input("CHOOSE AN OPTION: "))
    if len(option) != 1:
        print("please one number" )
        os.system('cls')
        return run()
    elif option not in "1,2,3":
        print("choose a correct option")
        os.system('cls')
        return run()

    elif option == "1":
        game()
        os.system('cls')
        return run()
    elif option == "2":
        print("config" ) 
        files()
        os.system('cls')
        return run()
    elif option == "3":
        exit()


    


   # menu_game = {
    #1 : Inicio,
    #2 : Configuracion,
    #3 : salir

    #}


if __name__ == '__main__':
    run()