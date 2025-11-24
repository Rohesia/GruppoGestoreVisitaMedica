# funzioni.py

import csv
import os
from datetime import datetime
from utente import Paziente
from CheckUp import CheckUp

# lista pazienti
pazienti = []

# carica pazienti dal file
def carica_pazienti_da_file():
    if not os.path.exists("pazienti.csv"):
        return
    with open("pazienti.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Paziente(
                row["Nome"], row["Cognome"], row["CF"],
                row["Data Nascita"], row["Email"]
            )
            pazienti.append(p)

# salva un paziente su file
def salva_paziente_su_file(p: Paziente):
    file_exists = os.path.exists("pazienti.csv")
    with open("pazienti.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nome", "Cognome", "CF", "Data Nascita", "Email"])
        writer.writerow([p.name, p.surname, p.code, p.birth, p.email or ""])

# mostra lista pazienti
def mostra_pazienti():
    if not pazienti:
        print("Nessun paziente registrato.")
        return
    for i, p in enumerate(pazienti, 1):
        print(f"{i}. {p.info_completa()}")

# seleziona paziente
def seleziona_paziente():
    mostra_pazienti()
    if not pazienti:
        return None

    s = input("Seleziona numero paziente: ").strip()
    if not s.isdigit() or not (1 <= int(s) <= len(pazienti)):
        print("Scelta non valida.")
        return None

    return pazienti[int(s)-1]

# crea nuovo paziente
def crea_paziente():
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    cf = input("Codice fiscale: ")
    nascita = input("Data di nascita (GG/MM/AAAA): ")
    email = input("Email: ").strip() or None

    # crea oggetto
    p = Paziente(nome, cognome, cf, nascita, email)
    pazienti.append(p)
    salva_paziente_su_file(p)

    # prima visita
    print("\n--- Prima visita ---")
    data_str = input("Data (AAAA-MM-GG HH:MM): ")
    tipo = input("Tipo visita: ")
    note = input("Note: ")
    acc = input("Accettata? (s/n): ").lower()

    try:
        d = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato data errato.")
        return
    
    # crea check-up
    check = CheckUp(d, f"{tipo}: {note}", p)
    if acc == "s":
        check.accept()

    print("Paziente creato + prima visita registrata.")

# aggiunge un checkup
def aggiungi_checkup():
    p = seleziona_paziente()
    if not p:
        return

    data_str = input("Data (AAAA-MM-GG HH:MM): ")
    tipo = input("Tipo: ")
    note = input("Note: ")
    acc = input("Accettata? (s/n): ").lower()

    try:
        d = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Data errata.")
        return

    # crea check-up
    check = CheckUp(d, f"{tipo}: {note}", p)
    if acc == "s":
        check.accept()

    print("Check-up aggiunto.")

# mostra visite di un paziente
def mostra_visite_paziente():
    p = seleziona_paziente()
    if not p:
        return

    choice:int = int(input("Vuoi vederle tutte(1), solo quelle accettate(2) o solo quelle rifiutate(3)?: "))

    match(choice):
        case 1: print_checkup(p, CheckUp.print_all_by_patience)
        case 2: print_checkup(p, CheckUp.print_accepted_by_patience)
        case 3: print_checkup(p, CheckUp.print_not_accepted_by_patience)
        case _: print("Wrong input")

def print_checkup(p, func):
    print(f"\n--- Visite di {p.name} {p.surname} ---")
    func(p)