import csv
from datetime import datetime
import os
from utente import Paziente as Patience

class CheckUp:
    def __init__(self, date:datetime, notes:str, patience:Patience):
        self.__date = date
        self.__notes = notes
        self.__patience = patience  # instance of Patience
        self.__is_accepted = False
        self._load_to_file()

    # Accept the check-up
    def accept(self):
        self.__is_accepted = True
        self.update_acceptance()

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
    
    ## METHODS ##

    def update_acceptance(self):
        filename = f"{self.__patience.name}_{self.__patience.surname}_{self.__patience.code}.csv"

        # Read all rows
        with open(filename, mode='r', newline='') as file:
            reader = list(csv.reader(file))

        # Find the row matching this checkup's date + notes
        for i, row in enumerate(reader):
            if row[0] == self.__date.strftime("%Y-%m-%d %H:%M") and row[1] == self.__notes:
                reader[i][2] = "Yes" if self.__is_accepted else "No"
                break

        # Rewrite the file with updated rows
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    # Generate CSV file if not exists
    def _load_to_file(self):
        filename = f"./{self.__patience.name}_{self.__patience.surname}_{self.__patience.code}.csv" # generates filename
        file_exists = os.path.exists(filename) #checks if exists

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists: # if file not exists, creates it + first row
                writer.writerow(["Date", "Notes", "Accepted"])
            writer.writerow([self.__date.strftime("%Y-%m-%d %H:%M"), self.__notes,"Yes" if self.__is_accepted else "No"]) # loads checkup

    # Print last visit (current)
    def print(self):
        filename = f"{self.__patience.name}_{self.__patience.surname}_{self.__patience.code}.csv"
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = list(csv.reader(file))  # convert iterator to list
                if len(reader) > 1:  # ensure there is at least one visit beyond header
                    last_row = reader[-1]
                    print(" | ".join(last_row))
                else:
                    print("No visits recorded yet.")
        else:
            print(f"No visit file found for: {self.__patience.name}_{self.__patience.surname}.")

    @staticmethod
    def print_all_by_patience(patience:Patience): # static method, takes a Patience and prints its checkups
        filename = f"{patience.name}_{patience.surname}_{patience.code}.csv" # takes filename
        if os.path.exists(filename): # checks if exists
            with open(filename, mode='r') as file:
                reader = csv.reader(file) # opens reader
                for row in reader:
                    print(" | ".join(row)) # prints reader
        else:
            print(f"No visit file found for: {patience.name}_{patience.surname}.")

    @staticmethod
    def print_accepted_by_patience(patience:Patience): # static method, takes a Patience and prints its checkups
        filename = f"{patience.name}_{patience.surname}_{patience.code}.csv" # takes filename
        if os.path.exists(filename): # checks if exists
            with open(filename, mode='r') as file:
                reader = csv.reader(file) # opens reader
                for row in reader:
                    if row[-1].strip().lower() == ("yes"):
                        print(" | ".join(row)) # prints reader
        else:
            print(f"No visit file found for: {patience.name}_{patience.surname}.")

    @staticmethod
    def print_not_accepted_by_patience(patience:Patience): # static method, takes a Patience and prints its checkups
        filename = f"{patience.name}_{patience.surname}_{patience.code}.csv" # takes filename
        if os.path.exists(filename): # checks if exists
            with open(filename, mode='r') as file:
                reader = csv.reader(file) # opens reader
                for row in reader:
                    if row[-1].strip().lower() == ("no"):
                        print(" | ".join(row)) # prints reader
        else:
            print(f"No visit file found for: {patience.name}_{patience.surname}.")

# Create two patients
p1 = Patience("Luca", "Rossi", "A123")
p2 = Patience("Maria", "Bianchi", "B456")

# --- Patient 1: 5 visits, 4 accepted ---
visits_p1 = [
    ("Routine blood test", True),
    ("Follow-up visit", True),
    ("X-ray check", True),
    ("Specialist consultation", False),
    ("Final clearance", True),
]

for notes, accepted in visits_p1:
    c = CheckUp(datetime.now(), notes, p1)
    if accepted:
        c.accept()
    # file writing happens automatically in __init__

# --- Patient 2: 5 visits, 3 accepted ---
visits_p2 = [
    ("Initial check", True),
    ("Blood pressure monitoring", False),
    ("Diet consultation", True),
    ("Cardiology exam", False),
    ("Final report", True),
]

for notes, accepted in visits_p2:
    c = CheckUp(datetime.now(), notes, p2)
    if accepted:
        c.accept()

# --- Demonstrations ---
print("\n=== All visits for Luca Rossi ===")
CheckUp.print_all_by_patience(p1)

print("\n=== Accepted visits for Luca Rossi ===")
CheckUp.print_accepted_by_patience(p1)

print("\n=== Not accepted visits for Luca Rossi ===")
CheckUp.print_not_accepted_by_patience(p1)

print("\n=== Last visit for Luca Rossi ===")
c.print()  # last created checkup for p1

print("\n=== All visits for Maria Bianchi ===")
CheckUp.print_all_by_patience(p2)

print("\n=== Accepted visits for Maria Bianchi ===")
CheckUp.print_accepted_by_patience(p2)

print("\n=== Not accepted visits for Maria Bianchi ===")
CheckUp.print_not_accepted_by_patience(p2)

print("\n=== Last visit for Maria Bianchi ===")
c2 = CheckUp(datetime.now(), "Temporary check", p2)
c2.accept()
c2.print()