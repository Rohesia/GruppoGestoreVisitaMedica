# utente.py

class Paziente:
    def __init__(self, nome: str, cognome: str, cf: str, data_nascita: str = "", email: str = None):
        self.__nome = nome
        self.__cognome = cognome
        self.__cf = cf
        self.__email = email
        self.__data_nascita = data_nascita

    # --- PROPERTIES ---
    @property
    def name(self) -> str:
        return self.__nome

    @property
    def surname(self) -> str:
        return self.__cognome
    
    @property
    def code(self) -> str:
        return self.__cf

    @property
    def birth(self) -> str:
        return self.__data_nascita
    
    @property
    def email(self) -> str:
        return self.__email

    # --- INFO ---
    def info(self):
        return (
            f"Nome: {self.__nome} {self.__cognome}\n"
            f"Codice fiscale: {self.__cf}\n"
            f"Data di nascita: {self.__data_nascita}"
        )

    def info_completa(self):
        email_info = f"\nEmail: {self.__email}" if self.__email else ""
        return f"{self.info()}{email_info}"
