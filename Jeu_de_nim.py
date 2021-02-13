def display_welcome_message():
    print("///////////////////////////////////////")
    print("//////////// LE JEU DE NIM ////////////")
    print("///////////////////////////////////////")
    print("*         développé par : aroznie     *")
    print("///////////////////////////////////////")
    print("\n")
 
def game():
    playing = True
    baton = '|'
    ia = False
    player = False

    A = int(input("Combien d'allumettes désirez vous ?\n"))
    R = int(input("Donnez l'echelle d'allumettes pouvant etre retiré\n"))
    start = int(input("Qui va commencer? L'ordinateur : 0 , ou vous : 1\n"))

    if start == 0:
        ia = True
        print("très bien, l'ordinateur va donc commencer")
    elif start == 1:
        player = True
        print("très bien, vous allez donc commencer")
    else:
        print("Mauvaise entree dommage, recommencez")

    print(baton * A)

    while playing & (A > 1):
        if player:
            N = R + 1
            while N > R:
                N = int(input("Combien d'allumettes' voulez vous retirer?\n"))
                if N >= R and N < 0:
                    print("recommencez, mauvaise entrée")
            A -= N
            print("Il reste donc", A , "allumettes")
            print(baton * A)
            if A != 1:
                ia = True
                player = False
            print("\n ------------------------------------------------------------------")
        
        if ia:
            N = R
            while A % N != 0 and A > R:
                N -= 1
                if N == 1:
                    break
            if A <= R:
                N = A - 1
            print("La machine prend : ", N, "allumettes\nIl reste donc", A - N, "allumettes")
            A -= N
            print(baton * A)
            if A != 1:
                player = True
                ia = False
            print("\n ------------------------------------------------------------------")

    if player:
        print("Echec et mat, vous avez gagné")
    elif ia:
        print("Echec et mat, vous avez perdu")

def new_game():
    print("Voulez-vous faire une nouvelle partie du jeu de Nim ? (o/n)")
    c = input()
    while c != 'o' and c != 'n' :
        print("Saisissez 'o' pour oui et 'n' pour non")
        c = input()
    if c == 'o' :
        return True
    else :
        return False


def display_stop_message():
    print("\n")
    print("***************************************")
    print("    Merci d'avoir joué, à bientôt.     ")
    print("***************************************")

def main():
    display_welcome_message()
    game()
    while new_game():
        game()
    display_stop_message()

main()