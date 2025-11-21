
import csv
from utente import Paziente
from CheckUp import CheckUp
from datetime import datetime
import os

# lista globale dei pazienti
pazienti = []

# gestione del paziente
def carica_pazienti_da_file():
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
    file_exists = os.path.exists("pazienti.csv")
    with open("pazienti.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nome","Cognome","CF","Data Nascita","Email"])
        writer.writerow([p.nome, p.cognome, p.get_cf(), p.get_data_nascita(), p.get_email() or ""])


# gestione file visite

def carica_visite_da_file():
    for file in os.listdir("."):
        if file.endswith(".csv") and file != "pazienti.csv":
            parts = file[:-4].split("_")
            if len(parts) == 3:
                nome, cognome, cf = parts
                paziente = next((p for p in pazienti if p.get_cf() == cf), None)
                if not paziente:
                    paziente = Paziente(nome, cognome, cf, data_nascita="N/A")
                    pazienti.append(paziente)
                with open(file, "r") as f:
                    reader = csv.reader(f)
                    next(reader)  # salta intestazione
                    for row in reader:
                        date_str, notes, accepted = row
                        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                        c = CheckUp(date, notes, paziente)
                        if accepted.lower() == "yes":
                            c.accept()
                        paziente.aggiungi_visita(c)


# gestione pazienti

def mostra_pazienti():
    if not pazienti:
        print("Nessun paziente registrato.")
        return
    for idx, p in enumerate(pazienti, 1):
        print(f"{idx}. {p.info_completa()}")

def seleziona_paziente():
    mostra_pazienti()
    if not pazienti:
        return None
    scelta = input("Seleziona il paziente (numero): ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(pazienti):
        print("Scelta non valida.")
        return None
    return pazienti[int(scelta)-1]

def crea_paziente():
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    cf = input("Codice fiscale: ")
    data_nascita = input("Data di nascita (GG/MM/AAAA): ")
    email = input("Email (opzionale): ").strip() or None
    p = Paziente(nome, cognome, cf, data_nascita, email)
    pazienti.append(p)
    salva_paziente_su_file(p)
    print("Paziente creato con successo!")


# gestione visite

def aggiungi_checkup():
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
    c = CheckUp(data, f"{tipo}: {note}", p)
    p.aggiungi_visita(c)
    c.generate_file() #TODO: REMOVE
    print("Check-up aggiunto e registrato su file.")

def accetta_checkup():
    p = seleziona_paziente()
    if not p:
        return
    visite = p.get_visite()
    if not visite:
        print("Nessuna visita disponibile per questo paziente.")
        return
    for idx, v in enumerate(visite, 1):
        status = "Accettata" if v.is_accepted else "Non accettata"
        print(f"{idx}. {v.date.strftime('%Y-%m-%d %H:%M')} | {v.notes} | {status}")
    scelta = input("Seleziona check-up da accettare: ").strip()
    if not scelta.isdigit() or not 1 <= int(scelta) <= len(visite):
        print("Scelta non valida.")
        return
    visite[int(scelta)-1].accept()
    visite[int(scelta)-1].generate_file()
    print("Check-up accettato!")

def mostra_visite_paziente():
    p = seleziona_paziente()
    if not p:
        return
    if not p.get_visite():
        print("Nessuna visita registrata.")
        return
    for v in p.get_visite():
        status = "Accettata" if v.is_accepted else "Non accettata"
        print(f"{v.date.strftime('%Y-%m-%d %H:%M')} | {v.notes} | {status}")

def mostra_visite_da_file():
    p = seleziona_paziente()
    if not p:
        return
    filename = f"{p.nome}_{p.cognome}_{p.get_cf()}.csv"
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    else:
        print("Nessun file visite trovato per questo paziente.")

def mostra_visite_da_file_per_paziente(p):
    filename = f"{p.nome}_{p.cognome}_{p.get_cf()}.csv"
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    else:
        print("Nessun file visite trovato.")
