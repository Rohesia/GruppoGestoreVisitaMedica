# classe paziente 

class Paziente:
    def __init__(self, nome: str, cognome: str, cf: str, data_nascita: str, email: str = None):
        self.nome = nome 
        self.cognome = cognome 
        # attributi protetti 
        self._cf = cf 
        self._email = email 
        self._data_nascita = data_nascita 
        # lista delle visite del paziente 
        self._visite = []
        
        # metodi get e set 
    def get_cf(self):
        return self._cf

    def set_cf(self, cf: str):
        self._cf = cf

    def get_data_nascita(self):
        return self._data_nascita

    def set_data_nascita(self, data: str):
        self._data_nascita = data

    def get_email(self):
        return self._email

    def set_email(self, email: str):
        self._email = email

    def aggiungi_visita(self, visita):
        # aggiunge un oggetto visita alla lista delle visite
        self._visite.append(visita)
    
    def get_visite(self):
        return self._visite
    
    def info(self):
        return f"Nome: {self.nome} {self.cognome}\nCodice fiscale: {self._cf}\nData di nascita: {self._data_nascita}"
    
    def info_completa(self):
        email_info = f"\nEmail: {self._email}" if self._email else ""
        visite_info = f"\nNumero di visite registrate: {len(self._visite)}"
        return f"{self.info()}{email_info}{visite_info}"
 
'''
p = Paziente("Mario", "Rossi", "MR123", "15/05/1985", "mario.rossi@email.com")
print(p.info())
print(p.info_completa())
'''   


