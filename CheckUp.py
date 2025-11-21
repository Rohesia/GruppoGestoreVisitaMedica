import csv
from datetime import datetime
import os
from Patience import Patience

class CheckUp:
    def __init__(self, date:datetime, notes:str, patience:Patience):
        self.__date = date
        self.__notes = notes
        self.__patience = patience  # instance of Patience
        self.__is_accepted = False

    # Accept the check-up
    def accept(self):
        self.__is_accepted = True

    # properties
    @property
    def date(self) -> datetime:
        return self.__date
    
    @property
    def notes(self) -> str:
        return self.__notes
    
    @property
    def patience(self) -> Patience:
        return self.__patience
    
    @property
    def is_accepted(self) -> bool:
        return self.__is_accepted


    # Generate CSV file if not exists
    def generate_file(self):
        filename = f"./{self.__patience.name}_{self.__patience.surname}_{self.__patience.code}.csv"
        file_exists = os.path.exists(filename)

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Date", "Notes", "Accepted"])
            writer.writerow([self.__date.strftime("%Y-%m-%d %H:%M"), self.__notes,"Yes" if self.__is_accepted else "No"])

    # Print all visits from file
    def print_from_file(self):
        filename = f"{self.__patience.name}_{self.__patience.surname}_{self.__patience.code}.csv"
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(" | ".join(row))
        else:
            print("No visit file found.")

p = Patience("Luca", "Rossi", "A123")
check = CheckUp(datetime.now(), "Controllo pressione", p)
check.accept()
check.generate_file()
check.print_from_file()