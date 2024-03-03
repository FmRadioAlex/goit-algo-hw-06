import os
from collections import UserDict
os.system("cls")

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return str(self.name)
    

class Phone(Field):
    def __init__(self, phone):
        if len(phone)==10:
            self.phone=phone
        
    def __str__(self):
        return str(self.phone)    

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone(self,number):
        self.phones.append(number)

    def delete_phone(self,phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self,old_num,new_num):
        
        enum=0
        for count in self.phones:
            if old_num == count:
                self.phones[enum] = new_num
            enum+=1
    
    def find_phone(self,phone):
        if phone in self.phones:
            return phone
        


    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict,Phone):
    
    def add_record(self,class_person):
        
        self.data[class_person.name.name] = class_person
        
       
    def find(self,name):
        
       return self.get(name)
    
    def delete(self,name):
        for nick, other in self.data.items():
            if nick==name:
                del self.data[nick]
                return other
        
            

    def __str__(self) -> str:
        return self.class_person
    
    

# Створення нової адресної книги
book = AddressBook()


# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")



# Додавання запису John до адресної книги
book.add_record(john_record)                #AdressBook->Recod->Name,[Phone]

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)                #AdressBook->Recod->Name,[Phone]

 
# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)


# Знаходження та редагування телефону для John
john = book.find("John")                        # Отримуємо класс John( в теоріі але не працює)
                             # грубо кажучі ось так воно повинно бути 
john.edit_phone("1234567890", "1112223333")     #john->book.find()->AdressBook->Recod->Name,[Phone]


print(f"\n{john}",end="\n\n")                    # Виведення: Contact name: John, phones: 1112223333; 5555555555



# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}",end='\n\n')  # Виведення: 5555555555



# Видалення запису Jane
print(f"Delete: {book.delete("Jane")}",end="\n\n")



for name, record in book.data.items():
    print(record)
