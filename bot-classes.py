from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate():
            raise ValueError("Invalid phone number")

    def validate(self):
        return len(self.value) == 10 and self.value.isdigit()

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        phone.value = new_phone

    def find_phone(self, phone):
        return next((p for p in self.phones if p == phone), None)

    def get_all_phones(self):
        return [p.value for p in self.phones]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}"

    def __eq__(self, other):
        return isinstance(other, Record) and self.name == other.name and self.phones == other.phones

    def __hash__(self):
        return hash((self.name, tuple(self.phones)))

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def find_records(self, name_part):
        return [record for record in self.data.values() if name_part in record.name.value]
