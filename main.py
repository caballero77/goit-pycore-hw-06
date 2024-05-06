from domain import AddressBook, Record

book = AddressBook()

john_record = Record("John")
john_record.add_phone("+380632533452")
john_record.add_phone("+380634528763")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("+380645733165")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("+380632533452", "+380631234567")

print(john)

found_phone = john.find_phone("+380634528763")
print(f"{john.name}: {found_phone}")

book.delete("Jane")