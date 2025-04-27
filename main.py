import random
wylosowanaLiczba = random.randint(0,100);
liczbaUzytkownika = int(input("Wprowadź liczbe: "));
proba = 0
while wylosowanaLiczba != liczbaUzytkownika:
    if wylosowanaLiczba > liczbaUzytkownika:
        print("Więcej");
    else:
        print("Mniej");
    liczbaUzytkownika = int(input("Wprowadź jeszcze raz: "));
    proba += 1
    if proba == 5:
        print("Nie tym razem");
        break;
    elif wylosowanaLiczba == liczbaUzytkownika:
        print("Gratulacje!");
        break;
else:
    print("Zgadłeś za pierwszym razem");