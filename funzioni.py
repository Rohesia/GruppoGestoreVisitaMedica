# funzioni.py

import csv
import os
from datetime import datetime
from utente import Paziente
from CheckUp import CheckUp

# lista globale dei pazienti
pazienti = []

# --- PAZIENTI ---
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

def salva_paziente_su_file(p: Paziente):
    file_exists = os.path.exists("pazienti.csv")
    with open("pazienti.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nome", "Cognome", "CF", "Data Nascita", "Email"])
        writer.writerow([p.name, p.surname, p.code, p.birth, p.email or ""])

def mostra_pazienti():
    if not pazienti:
        print("Nessun paziente registrato.")
        return
    for i, p in enumerate(pazienti, 1):
        print(f"{i}. {p.info_completa()}")

def seleziona_paziente():
    mostra_pazienti()
    if not pazienti:
        return None

    s = input("Seleziona numero paziente: ").strip()
    if not s.isdigit() or not (1 <= int(s) <= len(pazienti)):
        print("Scelta non valida.")
        return None

    return pazienti[int(s)-1]

# --- CREAZIONE PAZIENTE  ---
def crea_paziente():
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    cf = input("Codice fiscale: ")
    nascita = input("Data di nascita (GG/MM/AAAA): ")
    email = input("Email: ").strip() or None

    # crea oggetto Paziente e salva su file
    p = Paziente(nome, cognome, cf, nascita, email)
    pazienti.append(p)
    salva_paziente_su_file(p)

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
    
    # crea check-up e salva
    check = CheckUp(d, f"{tipo}: {note}", p)
    if acc == "s":
        check.accept()
    check.save()

    print("Paziente creato + prima visita registrata.")

# --- AGGIUNTA CHECK-UP SUCCESSIVI ---
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

    check = CheckUp(d, f"{tipo}: {note}", p)
    if acc == "s":
        check.accept()
    check.save()
    print("Check-up aggiunto.")
