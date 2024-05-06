import pytest
from domain import Phone, Record, AddressBook

@pytest.mark.parametrize('number', ['+380631234567', '0631234567', '+380634539564', '0635715347'])
def test_phone_success(number):
    phone = Phone(number)
    assert phone.value == number

@pytest.mark.parametrize('phone', [
    '+3806312345678', '06312345678', '+3806345395648', '06357153478', '380543622374',
    '380543622374', '380543622374', '380543622374', '380543622374', '380543622374',
])
def test_phone_failure(phone):
    with pytest.raises(ValueError):
        Phone(phone)

@pytest.mark.parametrize('phone', ['+380631234567', '0631234567', '+380634539564', '0635715347'])
def test_record_add_phone_success(phone):
    record = Record('name')
    assert record.add_phone(phone)
    assert not record.add_phone(phone)
    assert record.find_phone(phone)

@pytest.mark.parametrize('phone', [
    '+3806312345678', '06312345678', '+3806345395648', '06357153478', '380543622374',
    '380543622374', '380543622374', '380543622374', '380543622374', '380543622374',
])
def test_record_add_phone_failure(phone):
    record = Record('name')
    with pytest.raises(ValueError):
        record.add_phone(phone)
    
@pytest.mark.parametrize('phone', ['+380631234567', '0631234567', '+380634539564', '0635715347'])
def test_record_delete_phone(phone):
    record = Record('name')
    record.add_phone(phone)
    assert record.find_phone(phone)
    assert record.delete_phone(phone)
    assert not record.find_phone(phone)
    assert not record.delete_phone(phone)

@pytest.mark.parametrize('phone,newPhone', [
    ('+380631234567', "+3806312345678"),
    ('0631234567', "06312345678"),
    ('+380634539564', "+3806345395648"),
    ('0635715347', "06357153478")
])
def test_record_edit_phone(phone, newPhone):
    record = Record('name')
    record.add_phone(phone)
    assert record.find_phone(phone)
    assert record.edit_phone(phone, newPhone)
    assert not record.find_phone(phone)
    assert record.find_phone(newPhone)
    assert not record.edit_phone(phone, newPhone)

def test_record_str():
    record = Record('name')
    record.add_phone('+380631234567')
    record.add_phone('0631234567')
    record.add_phone('+380634539564')
    record.add_phone('0635715347')
    assert str(record) == 'Contact name: name, phones: +380631234567; 0631234567; +380634539564; 0635715347'

def test_address_book_add_record():
    record = Record('name')
    address_book = AddressBook({})
    assert address_book.add_record(record)
    assert not address_book.add_record(record)
    assert address_book.has_record('name')

def test_address_book_delete():
    record = Record('name')
    address_book = AddressBook({'name': record})
    assert address_book.has_record('name')
    assert address_book.delete('name')
    assert not address_book.delete('name')
    assert not address_book.has_record('name')

def test_address_book_find():
    record = Record('name')
    address_book = AddressBook({'name': record})
    assert address_book.find('name') == record
    assert address_book.find('name1') is None