from funzioni import *

if __name__ == "__main__":
    # Carica i pazienti esistenti
    carica_pazienti_da_file()

    while True:
        print("\n--- Menu Gestione Pazienti ---")
        print("1. Crea nuovo paziente")
        print("2. Aggiungi check-up/visita")
        print("3. Accetta check-up")
        print("4. Mostra pazienti")
        print("5. Mostra visite paziente")
        print("6. Esci")
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
            p = seleziona_paziente()
            if p:
                print(f"\nVisite di {p.name} {p.surname}:")
                CheckUp.print_by_patience(p)
        elif scelta == "6":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")
