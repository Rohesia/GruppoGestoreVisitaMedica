from Utente import Paziente
from CheckUp import CheckUp
from funzioni import *
from datetime import datetime

def menu():
    while True:
        print("\n--- Menu Gestione Pazienti ---")
        print("1. Crea nuovo paziente")
        print("2. Aggiungi check-up/visita")
        print("3. Accetta check-up")
        print("4. Mostra pazienti")
        print("5. Mostra visite paziente (sessione)")
        print("6. Mostra visite paziente dal file")
        print("7. Esci")
        scelta = input("Seleziona un'opzione: ").strip()
        
        if scelta == "1":
            crea_paziente()
        elif scelta == "2":
            aggiungi_checkup()
        elif scelta == "3":
            accetta_checkup()
        elif scelta == "4":
            mostra_pazienti()
        elif scelta == "5":
            mostra_visite_paziente()
        elif scelta == "6":
            mostra_visite_da_file()
        elif scelta == "7":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu()