# -*- coding: utf-8 -*-
"""

@author: Paolo Minniti
"""

import Contacts


class Phonebook:
    contacts = []

    def __init__(self):
        pass
    
    def update_contact(self, surname,name):
        """
        method that updates contact using surname and name
        surname(str)
        name(str)
        """
        for i in self.contacts: #scansiona in cerca del cognome
            if i["_Contact__surname"] == surname and i["_Contact__name"] == name:
                scelta= input("È questo il contatto da modificare ? Y/N").upper()
                if(scelta=="Y"): 
                    try: 
                        print("Immettere i nuovi dati")
                        surname= input("Cognome: ")
                        name= input("Nome: ")
                        phone= int(input("Numero: "))
                        c= Contacts.Contact(surname, name,phone)
                        self.contacts.append(c.getDict())
                        # self.contacts.append({ "surname":cognome,"name":nome, "phone": numeroTelefono })
                        print("Contatto inserito con successo")
                        # self.__lista.append(p) #inserimento in lista del nuovo elemento
                        self.contacts.remove(i) #rimozione dalla lista del vecchio elemento
                        break
                    except ValueError:
                        print("Numero di telefono non valido")
                        print()
                    except:
                        print("Errore in input")
                        print()
                elif(scelta=="N"):
                    continue
                else:
                    print("Opzione non valida")
                    print()
                    break
        else:
            print("Contatto non trovato")
            print()
            

    def add_new_contact(self,surname,name,phone):
    
        """
        method that inserts a contact
        surname(str)
        name(str)
        phone (int)
        """
        
        for i in self.contacts: 
            if i["_Contact__surname"] == surname  and i["_Contact__name"] == name:
                # print(f"cognome: {i['_Contact__surname']}, nome:{i['_Contact__name']}, contattatto esistente in rubrica,non può essere aggiunto!!!")
                print("contattatto esistente in rubrica,non può essere aggiunto!!!")
                print()
                return
        c= Contacts.Contact(surname, name,phone)
        self.contacts.append(c.getDict())
        print("Contatto inserito con successo")
        print()
    
  
    def display_all_contacts(self):
        """
        method that prints all contacts
        """
     
        print('-'*40)
        print('COGNOME | NOME | Numero di telefono')
        print('-'*40)
        for contact in self.contacts:
            print(contact["_Contact__surname"] + ' | ' + 
                  contact["_Contact__name"] + ' | ' + 
                  str(contact["_Contact__phone"]))
        print('-'*40)
        print()

 
    def delete_contact(self):
        """
        method that deletes a contact
        """
        print("Immettere cognome e nome del contatto da cancellare")
        surname= input("Cognome: ")
        name= input("Nome: ")
        for contact in self.contacts:
            if  contact["_Contact__surname"] == surname and contact["_Contact__name"] == name:
                self.contacts.remove(contact)
                print("Il seguente conttatto è stato cancellato.")
                print(f"cognome: {contact['_Contact__surname']}, nome:{contact['_Contact__name']}, telefono: {contact['_Contact__phone']}")
                print()
                return
        print("Contatto non trovato")
        print()

   
    def search_contact_by_name(self):
        """
        method that searches for a contact using name
        """
        found = 0
        search = input("Quale contatto desideri cercare per nome?")
        for contact in self.contacts:
            if contact["_Contact__name"] == search:
                print(f"Contatto trovato ! cognome: {contact['_Contact__surname']},name: {contact['_Contact__name']}, telefono: {contact['_Contact__phone']}")
                print()
                found = 1
        if(found==0): 
            print(f"{search} non trovato") 
            print()
        
   
    def search_contact(self):
        """
        method that searches for a contact using surname
        """
        found = 0
        search = input("Quale contatto desideri cercare per cognome?")
        for contact in self.contacts:
            if contact["_Contact__surname"] == search:
                print(f"Contatto trovato ! cognome: {contact['_Contact__surname']},name: {contact['_Contact__name']}, telefono: {contact['_Contact__phone']}")
                print()
                found = 1
        
        if(found==0): #stampa il seguente messaggio
            print(f"{search} non trovato")
            print()
            
    def __help__(self):
        help(self)
    
        

    def __str__(self):
        res = ""
        for contact in self.contacts:
            res += contact.__str__() + "\n"
        return res
    



