from utente import Paziente
from checkup import CheckUp
from datetime import datetime
# lista dei pazienti
pazienti = []

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
    print("Paziente creato con successo!")

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
    c.generate_file()
    print("Check-up aggiunto e registrato su file.")
    
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