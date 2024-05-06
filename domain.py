import re
from collections import UserDict

class Field:
    """Base class for fields of the record"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class for name field of the record"""
    pass

class Phone(Field):
    """Class for phone field of the record"""
    def __init__(self, value):
        if not re.match(r"^(\+38)?(0\d{9})$", value):
            raise ValueError('Invalid phone number')
        super().__init__(value)

class Record:
    """Class for record, which contains name and phones of the contact"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> bool:
        """Add phone to the record
        
        Args:
            phone: str: phone number
        
        Returns:
            bool: True if phone was added, False if phone already exists"""
        if self.find_phone(phone):
            return False
        self.phones.append(Phone(phone))
        return True
    
    def delete_phone(self, phone_number: str) -> bool:
        """Delete phone from the record
        
        Args:
            phone_number: str: phone number
            
        Returns:
            bool: True if phone was deleted, False if phone not found"""
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
            return True
        return False
    
    def edit_phone(self, phone_number: str, new_phone: str) -> bool:
        """Edit phone in the record
        
        Args:
            phone_number: str: phone number
            new_phone: str: new phone number
        
        Returns:
            bool: True if phone was edited, False if phone not found"""
        phone = self.find_phone(phone_number)
        if phone:
            phone.value = new_phone
            return True
        return False

    def find_phone(self, phone_number: str) -> Phone:
        """Find phone in the record
        
        Args:
            phone_number: str: phone number
            
        Returns:
            Phone: phone object if phone was found, None if phone not found"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """Class for address book, which contains records of contacts"""
    def __init__(self, dict):
        super().__init__(dict)

    def add_record(self, record: Record) -> bool:
        """Add record to the address book
        
        Args:
            record: Record: record object
        
        Returns:
            bool: True if record was added, False if record already exists"""
        if self.has_record(record.name.value):
            return False

        self.data[record.name.value] = record
        return True
    
    def delete(self, name: str) -> bool:
        """Delete record from the address book
        
        Args:
            name: str: name of the contact
            
        Returns:
            bool: True if record was deleted, False if record not found"""
        if self.has_record(name):
            del self.data[name]
            return True
        return False
    
    def find(self, name: str) -> Record:
        """Find record in the address book
        
        Args:
            name: str: name of the contact
            
        Returns:
            Record: record object if record was found, None if record not found"""
        return self.data.get(name)
    
    def has_record(self, name: str) -> bool:
        """Check if record exists in the address book
        
        Args:
            name: str: name of the contact
        
        Returns:
            bool: True if record exists, False if record not found"""
        return self.data.get(name) is not None
    