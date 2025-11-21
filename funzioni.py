import csv
import os
from datetime import datetime
from utente import Paziente
from CheckUp import CheckUp

# lista globale dei pazienti in memoria
pazienti = []

# --- Gestione pazienti ---

def carica_pazienti_da_file():
    """Carica i pazienti dal file CSV nella lista globale"""
    if not os.path.exists("pazienti.csv"):
        return
    with open("pazienti.csv", "r", newline="") as f:
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
    """Salva un paziente nel CSV"""
    file_exists = os.path.exists("pazienti.csv")
    with open("pazienti.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nome", "Cognome", "CF", "Data Nascita", "Email"])
        writer.writerow([p.name, p.surname, p.get_cf(), p.get_data_nascita(), p.get_email() or ""])

def crea_paziente():
    """Crea un nuovo paziente e lo salva su file"""
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    cf = input("Codice fiscale: ").strip()
    data_nascita = input("Data di nascita (GG/MM/AAAA): ").strip()
    email = input("Email (opzionale): ").strip() or None
    p = Paziente(nome, cognome, cf, data_nascita, email)
    pazienti.append(p)
    salva_paziente_su_file(p)
    print(f"Paziente {nome} {cognome} creato con successo!")

def mostra_pazienti():
    """Mostra la lista dei pazienti in memoria"""
    if not pazienti:
        print("Nessun paziente registrato.")
        return
    for idx, p in enumerate(pazienti, 1):
        print(f"{idx}. {p.info_completa()}")

def seleziona_paziente():
    """Permette di selezionare un paziente dalla lista"""
    mostra_pazienti()
    if not pazienti:
        return None
    scelta = input("Seleziona il paziente (numero): ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(pazienti):
        print("Scelta non valida.")
        return None
    return pazienti[int(scelta) - 1]

# --- Gestione check-up/visite ---

def aggiungi_checkup():
    """Crea un check-up e lo salva subito su CSV"""
    p = seleziona_paziente()
    if not p:
        return
    data_str = input("Data e ora check-up (AAAA-MM-GG HH:MM): ").strip()
    tipo = input("Tipo visita: ").strip()
    note = input("Note (opzionale): ").strip()
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato data non valido.")
        return
    c = CheckUp(data, f"{tipo}: {note}", p)
    print("Check-up aggiunto e registrato su file.")

def accetta_checkup():
    """Permette di accettare un check-up non ancora accettato"""
    p = seleziona_paziente()
    if not p:
        return
    filename = f"{p.name}_{p.surname}_{p.get_cf()}.csv"
    if not os.path.exists(filename):
        print("Nessun check-up trovato per questo paziente.")
        return

    # legge tutte le righe
    with open(filename, "r", newline="") as f:
        reader = list(csv.reader(f))
    header, rows = reader[0], reader[1:]
    
    # mostra i check-up non accettati
    non_accettati = [(i, row) for i, row in enumerate(rows) if row[2].lower() != "yes"]
    if not non_accettati:
        print("Non ci sono check-up da accettare.")
        return

    print("Check-up non accettati:")
    for idx, (i, row) in enumerate(non_accettati, 1):
        print(f"{idx}. {row[0]} | {row[1]} | {row[2]}")

    scelta = input("Seleziona check-up da accettare: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(non_accettati):
        print("Scelta non valida.")
        return

    index = non_accettati[int(scelta)-1][0]
    rows[index][2] = "Yes"

    # riscrive il CSV aggiornato
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print("Check-up accettato!")

