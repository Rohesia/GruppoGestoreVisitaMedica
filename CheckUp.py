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
            print(f"No visit file found for: {self.patience.name}_{self.patience.surname}.")
    
    @staticmethod
    def print_by_patience(patience:Patience):
        filename = f"{patience.name}_{patience.surname}_{patience.code}.csv"
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(" | ".join(row))
        else:
            print(f"No visit file found for: {patience.name}_{patience.surname}.")


# 1. Create a patient
p = Patience("Luca", "Rossi", "A123")
p1 = Patience("Andrea", "Marii", "B432")
p2 = Patience("Tanja", "Marisi", "B312")
p3 = Patience("Gianmarco", "Ottanini", "Z043")

# 2. Create a check-up for this patient
checkup1 = CheckUp(datetime.now(), "Routine blood test", p)

# 3. Accept the check-up
checkup1.accept()

# 4. Generate the CSV file (creates or appends)
checkup1.generate_file()

# 5. Print all visits from the file
print("Visits for patient Luca Rossi:")
checkup1.print_from_file()

# 6. Create other 2 check-up for different patiences
checkup2 = CheckUp(datetime.now(), "Dental Analysis", p1)
checkup2.accept()
checkup2.generate_file()
checkup3 = CheckUp(datetime.now(), "Follow-up visit", p3)
checkup3.accept()
checkup3.generate_file()

# 7. Generate a different CheckUp for the same patience
checkup2 = CheckUp(datetime.now(), "Follow-up visit", p)
checkup2.accept()
checkup2.generate_file()

checkup1.print_from_file()
checkup2.print_from_file()
checkup3.print_from_file()

# 8. Print again to see both visits
print("\nUpdated visits for patient Luca Rossi:")
CheckUp.print_by_patience(patience=p)
CheckUp.print_by_patience(patience=p2)
