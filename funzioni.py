import csv
from utente import Paziente
from CheckUp import CheckUp
from datetime import datetime
import os

# lista globale dei pazienti
pazienti = []

# --- gestione pazienti ---

def carica_pazienti_da_file():
    """Carica i pazienti dal file CSV nella lista globale."""
    if not os.path.exists("pazienti.csv"):
        return
    with open("pazienti.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Paziente(
                row["Nome"],
                row["Cognome"],
                row["CF"],
                row["Data Nascita"],
                row["Email"] if row["Email"] else None
            )
            pazienti.append(p)

def salva_paziente_su_file(p: Paziente):
    """Salva un paziente nel CSV."""
    file_exists = os.path.exists("pazienti.csv")
    with open("pazienti.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nome","Cognome","CF","Data Nascita","Email"])
        writer.writerow([p.name, p.surname, p.get_cf(), p.get_data_nascita(), p.get_email() or ""])

def mostra_pazienti():
    """Stampa tutti i pazienti registrati."""
    if not pazienti:
        print("Nessun paziente registrato.")
        return
    for idx, p in enumerate(pazienti, 1):
        print(f"{idx}. {p.info_completa()}")

def seleziona_paziente():
    """Seleziona un paziente dalla lista."""
    mostra_pazienti()
    if not pazienti:
        return None
    scelta = input("Seleziona il paziente (numero): ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(pazienti):
        print("Scelta non valida.")
        return None
    return pazienti[int(scelta)-1]

def crea_paziente():
    """Crea un nuovo paziente e lo salva su file."""
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    cf = input("Codice fiscale: ")
    data_nascita = input("Data di nascita (GG/MM/AAAA): ")
    email = input("Email (opzionale): ").strip() or None
    p = Paziente(nome, cognome, cf, data_nascita, email)
    pazienti.append(p)
    salva_paziente_su_file(p)
    print("Paziente creato con successo!")

# --- gestione check-up ---

def aggiungi_checkup():
    """Crea un nuovo check-up per un paziente selezionato."""
    p = seleziona_paziente()
    if not p:
        return
    data_str = input("Data e ora check-up (AAAA-MM-GG HH:MM): ")
    tipo = input("Tipo visita: ")
    note = input("Note (opzionale): ")
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato data non valido.")
        return

    # crea e registra il check-up direttamente nel file CSV
    CheckUp(data, f"{tipo}: {note}", p)
    print("Check-up aggiunto e registrato su file.")

def accetta_checkup():
    """Accetta un check-up non ancora approvato di un paziente."""
    p = seleziona_paziente()
    if not p:
        return
    # leggere tutti i check-up dal file
    filename = f"{p.name}_{p.surname}_{p.get_cf()}.csv"
    if not os.path.exists(filename):
        print("Nessun check-up registrato per questo paziente.")
        return

    # raccoglie i check-up non accettati
    checkups = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)  # salta intestazione
        for row in reader:
            date_str, notes, accepted = row
            if accepted.lower() == "no":
                checkups.append((date_str, notes))

    if not checkups:
        print("Nessun check-up da accettare.")
        return

    # mostra i check-up non accettati
    for idx, (date_str, notes) in enumerate(checkups, 1):
        print(f"{idx}. {date_str} | {notes}")
    scelta = input("Seleziona check-up da accettare: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(checkups):
        print("Scelta non valida.")
        return

    # aggiorna il file CSV
    selected = checkups[int(scelta)-1]
    rows = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == selected[0] and row[1] == selected[1]:
                row[2] = "Yes"
            rows.append(row)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Check-up accettato!")

def mostra_visite_paziente():
    """Mostra tutte le visite di un paziente selezionato dal file CSV."""
    p = seleziona_paziente()
    if not p:
        return
    CheckUp.print_by_patience(p)
