import random
import time
from game import SpaceRocks

maps = {
        1: {"strefa": "1",
            "kierunek": {"lewo": 4, "dół": 2},
            "items": {"H": 12,
                      "J": 7}}
    ,
        2: {"strefa": "2",
            "kierunek": {"lewo": 3},
            "items": {"F": 10,
                      "G": -2}},
        3: {"strefa": "3",
            "kierunek": {"ukos": 1},
            "items": {"E": 8,
                      "D": 6}},
        4: {"strefa": "4",
            "kierunek": {"dół": 3, "prawo": 1},
            "items": {"C": 7,
                      "B": -5,
                      "A": 3}}
        }

ruchy = {1: {"broni się chwytakiem": "80",
            "broni się manipulatorem": "130",
            "broni się kołem": "230"},

        2: {"atakuje laserem": "-200",
            "atakuje chwytakiem": "-100",
            "atakuje kołem": "-150"}
         }

class Team():
    def __init__(self,name,base_retrival_points):
        self.name = name
        self.base_retrival_points = base_retrival_points

def move_count(move):
    if 4 - move > 1:
        print(f"\nZostały ci {4 - move} ruchy")
    elif move == 1:
        print(f"\nZostał ci {4 - move} ruch")

def ending(move):
    if move == 5:
        print("\nNie masz już ruchów do wykonania. Koniec zadania")
        print("Twój wynik to " + str(retrival_points) + " pkt\n" )
    else:
        pass

def things(starting_place):
    a = 0
    l = []
    if "items" in maps[starting_place]:
        for key in maps[starting_place]["items"].keys():
            a += 1
            l.append(key)
        if a == 1:
            print(f"\nNamierzono {a} przedmiot")
        else:
            print(f"\nNamierzono {a} przedmioty: ")
        while a > 0:
            a = a - 1
            print(f"> przedmiot {l[a]}")
        print(f"\nWybierz przedmiot, który weźmiesz")
        decision = input("Wybieram >> ").upper().split()
        new_retrival_points = maps[starting_place]["items"].get(decision[0])
        print(f"\nZdobyto {new_retrival_points} pkt.")
        global retrival_points
        retrival_points += int(new_retrival_points)
        print(f"Obecnie masz {retrival_points} pkt")
        x = maps[starting_place]["items"].pop(decision[0])

def strefy(starting_place, move):
    while move < 5:
        print("\nJesteś w Strefie " + maps[starting_place]["strefa"])
        things(starting_place)
        print("\nMożesz jechać do: ")
        for key in maps[starting_place]["kierunek"].keys():
            k = key
            z = maps[starting_place]["kierunek"].get(k)
            print(f"Strefy {z}")
        choice = input("\n>> Jadę do Strefy ")
        move_count(move)
        starting_place = int(choice)
        move += 1
        ending(move)

def move_count2(move):
    if 5 - move > 2:
        print(f"\nZostały ci {4 - move} rundy")
    elif move == 3:
        print(f"\nZostała ci {4 - move} runda")
    elif move == 4:
        print("\nKoniec walki")

def attack(a):
    k = 0
    if a == "e":
        attack_list = list(ruchy[2].keys())
        w = random.randint(0, 2)
        attack_move = attack_list[w]
        print(f"\n{enemy.name} {attack_list[w]}")
        k = ruchy[2].get(attack_move)
        global your_retrival_points
        your_retrival_points += int(k)
    elif a == "k":
        attack_list = list(ruchy[2].keys())
        w = random.randint(0, 2)
        attack_move = attack_list[w]
        print(f"\nKalman {attack_list[w]}")
        k = ruchy[2].get(attack_move)
        global enemy_retrival_points
        enemy_retrival_points += int(k)

def obrona(a):
    if a == "e":
        obrona_list = list(ruchy[1].keys())
        w = random.randint(0,2)
        obrona_move = obrona_list[w]
        print(f"\n{enemy.name} {obrona_list[w]}")
        k = ruchy[1].get(obrona_move)
        global enemy_retrival_points
        enemy_retrival_points += int(k)
    elif a == "k":
        obrona_list = list(ruchy[1].keys())
        w = random.randint(0,2)
        obrona_move = obrona_list[w]
        print(f"\nKalman {obrona_list[w]}")
        k = ruchy[1].get(obrona_move)
        global your_retrival_points
        your_retrival_points += int(k)

def result(your_retrival_points,enemy_retrival_points):
    if your_retrival_points > enemy_retrival_points:
        print("\nGratulacje, lecisz na Marsa!")
        space_rocks = SpaceRocks() #zmienna space_rocks przechowuje obiekt klasy, zdefiniowane w  klasie SpaceRocks
        space_rocks.main_loop()
    else:
        print("\nNiestety przegrałeś.")


#początek, czyta plik
x = open("intro","r", encoding="utf-8")
y = x.readlines()
for line in y:
    print(line)
z = time.sleep(3)

bonus = input("Bonus!\n"
              "Jeśli wpiszesz KALMAN, możesz od razu przejść do gry w Asteroidy\n"
              "Jeśli nie chcesz, wciśnij ENTER\n"
              "Wybieram >> ")

if bonus == "KALMAN":
    space_rocks = SpaceRocks()
    space_rocks.main_loop()
else:
    z = time.sleep(1)

    new = input("Gotowy na kosmiczną przygodę?\n"
          "Jeśli tak, wciśnij ENTER\n"
          "Jeśli chcesz zakończyć grę, wpisz EXIT\n")

    if new == "EXIT":
        q = quit()
    else:
        pass

    x = random.randrange(35,70)

    #krotki + wybór przeciwnika
    k_1 = ("Monash Nova Rover","Impuls Mars Rover","ITU Rover Team")
    k_2 = ("A","B","C")
    print(f"\nWybierz przeciwnka, z którym chcesz się zmierzyć.\nDo wyboru masz:"
          f"\nJeśli chcesz zakończyć grę, wpisz EXIT")
    l = 0
    while l < 3:
        for team in k_1:
            print(f"> {k_1[l]}: wpisz {k_2[l]}")
            l += 1

    a = True
    while a == True:
        choice = input("\nWybieram >> ").upper()
        if choice == "A":
            enemy = Team("Monash Rover Team",x)
            break
        elif choice == "B":
            enemy = Team("Impuls Mars Rover",x)
            break
        elif choice == "C":
            enemy = Team("ITU Rover Team",x)
            break
        elif choice == "EXIT":
            q = quit()
        else:
            print("Wybrano złą opcję. Wybierz jeszcze raz.\n"
                  "Wpisz A, B lub C")
            a = True


    you = Team("Kalman",random.randint(35,70))

    #wybierz członka załogi
    #lista
    crew_list = ["Adrian", "Jan", "Wiktoria"]
    print(f"\nWybierz członka załogi: \n"
          f"Do wyboru masz: \n"
          f"Jeśli chcesz zakończyć grę, wpisz EXIT")

    a = True
    while True:
        l = 0

        while l < 3:
            for crew in crew_list:
                print(f"> {crew_list[l]}: wpisz {crew_list[l]}")
                l += 1

        choice = input("\nWybieram: >> ")
        if choice == crew_list[0]:
            print("\nGratulację! Wybrałeś Adriana jako operatora Kalmana")
            break
        elif choice == crew_list[1]:
            print("\nGratulację! Wybrałeś Jana jako operatora Kalmana")
            break
        elif choice == crew_list[2]:
            print("\nGratulację! Wybrałeś Wiktorię jako operatora Kalmana")
            break
        elif choice == "EXIT":
            q = quit()
        else:
            print("\nWybrano złą opcję. Wybierz jeszcze raz: ")
            choice = input("\nWybieram: ")
            a = True

    your_crew = Team(choice,random.randint(-5,15))
    your_retrival_points = you.base_retrival_points - your_crew.base_retrival_points
    enemy_retrival_points = enemy.base_retrival_points - random.randint(-5,15)

    new = input("\nGotowy na rozpoczęcie Retrival Task?\n"
          "Jeśli tak, wciśnij ENTER\n"
          "Jeśli chcesz zakończyć grę, wpisz EXIT")

    if new == "EXIT":
        q = quit()
    else:
        pass

    print("\nRozpoczynasz Extreme Retrival Task")
    x = open("navigation","r", encoding="utf-8")
    y = x.readlines()
    for line in y:
        print(line)

    #retrival task
    starting_place = 1
    move = 0
    retrival_points = 0

    strefy(starting_place,move)
    your_retrival_points += retrival_points*50
    enemy_retrival_points += random.randint(-10,20)*50

    #walka
    print(f"Możesz teraz wybrać dwie opcje: \n"
          f"\n> możesz porównać swoją liczbę punktów zdobytą przez Kalmana i twojego rywala, {enemy.name}\n"
          f"Jeśli masz więcej punktów - wygrywasz bez walki i od razu możesz lecieć na Marsa!\n"
          f"Jeśli masz mniej punktów - przegrywasz całą grę.")
    z = time.sleep(2)
    print(f"\nBy wybrać, wpisz >> Check\n"
          f"\n> możesz przejść od razu do walki z {enemy.name}.\n"
          f"Zwycięsca poleci na Marsa przez pas asteroid. \n"
          f"\nBy wybrać, wpisz >> Walka\n")
    z = time.sleep(2)
    print(f"Jeśli chcesz zakończyć grę, wpisz EXIT")

    a = True
    while a == True:
        fight = input("\nWybieram:\n"">> ").upper()
        if fight == "WALKA":
            print("\n Obecne wyniki to: ")
            print(f"Kalman: {your_retrival_points} pkt")
            print(f"{enemy.name}: {enemy_retrival_points} pkt")
            print("\nCzas na walkę!")

            move = 0
            # enemy
            a = "e"
            attack(a)

            while move < 5:
                k = True
                while k == True:
                    # kalman
                    a = "k"
                    print(f"\nJeśli wybierasz atak, wpisz a\n"
                          f"Jeśli wybierasz obronę, wpisz o\n"
                          f"Jeśli wybierzesz niewłaściwy ruch to stracisz rundę!\n")
                    choice = input(">> ").lower()
                    if choice == "a":
                        attack(a)
                    elif choice == "o":
                        obrona(a)
                    else:
                        print("Wybrałeś niewłaściwy ruch")
                        k = True

                    # enemy
                    a = "e"
                    s = random.randint(1, 2)
                    if s == 1:
                        obrona(a)
                    elif s == 2:
                        attack(a)

                    print(f"\nKalman: {your_retrival_points} pkt")
                    print(f"{enemy.name}: {enemy_retrival_points} pkt")
                    move_count2(move)
                    move += 1
                    if move == 5:
                        k = False
                    else:
                        pass
                result(your_retrival_points, enemy_retrival_points)
            break

        elif fight == "CHECK":
            print("\nWyniki to: ")
            print(f"Kalman: {your_retrival_points} pkt")
            print(f"{enemy.name}: {enemy_retrival_points} pkt")
            result(your_retrival_points, enemy_retrival_points)
            break
        elif fight == "EXIT":
            q = quit()
        else:
            print("Wybrano złą opcję.\n"
                  "Wpisz >> Check jeśli chcesz sprawdzić wyniki.\n"
                  "Wpisz >> Walka jeśli chcesz przejść do walki")
            a = True


