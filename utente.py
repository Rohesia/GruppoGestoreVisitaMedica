# classe paziente 

class Paziente:
    def __init__(self, nome: str, cognome: str, cf: str, data_nascita: str = "", email: str = None):
        self.__nome = nome 
        self.__cognome = cognome 
        # attributi protetti 
        self.__cf = cf 
        self.__email = email 
        self.__data_nascita = data_nascita 
        """ 
        # lista delle visite del paziente 
        self._visite = [] """
        
    # Properties

    @property
    def name(self) -> str:
        return self.__nome

    @property
    def surname(self) -> str:
        return self.__cognome
    
    @property
    def code(self) -> str:
        return self.__cf

        # metodi get e set 
    def get_cf(self):
        return self.__cf

    def set_cf(self, cf: str):
        self.__cf = cf

    def get_data_nascita(self):
        return self.__data_nascita

    def set_data_nascita(self, data: str):
        self.__data_nascita = data

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    """ def aggiungi_visita(self, visita):
        # aggiunge un oggetto visita alla lista delle visite
        self._visite.append(visita) """
    
    """ def get_visite(self):
        return self._visite """
    
    def info(self):
        return f"Nome: {self.nome} {self.cognome}\nCodice fiscale: {self._cf}\nData di nascita: {self._data_nascita}"
    
    def info_completa(self):
        email_info = f"\nEmail: {self._email}" if self._email else ""
        #visite_info = f"\nNumero di visite registrate: {len(self._visite)}"
        return f"{self.info()}{email_info}"#{visite_info}"



