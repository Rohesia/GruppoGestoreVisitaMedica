from funzioni import *

if __name__ == "__main__":

    # TODO: creare ogni paziente da pazienti.csv e inserirli nella lista "pazienti = []""

    # TODO: aggiungi_checkup dovrebbe CREARE un oggetto checkup

    # TODO: accetta checkup dovrebbe chiedere il paziente, mostrare la lista dei checkup NON accettati e accettare

    # TODO: mostra pazienti dovrebbe printare la lista "pazienti = []"

    # TODO: mostra visite paziente dovrebbe far scegliere il paziente e richiamare CheckUp.print_by_patience(p)

    # TODO: mostra visite da file lo toglierei

    # TODO: scelta 7 la toglierei, basta la 5

    while True:
        print("\n--- Menu Gestione Pazienti ---")
        print("1. Crea nuovo paziente")
        print("2. Aggiungi check-up/visita")
        print("3. Accetta check-up")
        print("4. Mostra pazienti")
        print("5. Mostra visite paziente (sessione)")
        print("6. Mostra visite paziente dal file")
        print("7. Esci e mostra tutti i file")
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
            print("\n--- Dati pazienti ---")
            mostra_pazienti()
            print("\n--- Visite da file ---")
            for p in pazienti:
                print(f"\nVisite di {p.name} {p.surname}:")
                mostra_visite_da_file_per_paziente(p)
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")