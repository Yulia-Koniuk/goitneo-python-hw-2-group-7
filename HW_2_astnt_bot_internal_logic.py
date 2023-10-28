from collections import UserDict

# base class for fields record
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# class for storing a contact name
class Name(Field):
    pass

# class for storing a phone number (10 digits)
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number should contain 10 letters")
        super().__init__(value)

# class for storing info about a contact, incld name and phone list
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)
        for i, phone_obj in enumerate(self.phones):
            if phone_obj.value == old_phone_obj.value:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class for storing and managing records
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        if name in self.data:
            return self.data[name]
        



