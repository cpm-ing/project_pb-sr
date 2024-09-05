# -*- coding: utf-8 -*-
"""

@author: Paolo Minniti
"""
import os
from FileManager import FileManager
from Phonebook import Phonebook





def menu():
    """
    method that sets phonebook  menu
    """
    print("Rubrica telefonica")
    print("1 - Aggiungi contatto alla rubrica")
    print("2 - Visualizza i contatti della rubrica")
    print("3 - Cancella un contatto")
    print("4 - Cerca un contatto per cognome")
    print("5 - Cerca un contatto per nome")
    print("6 - Modifica un contatto ")
    print("7 - Uscita dal programma")
    return input( "Seleziona un comando valido, grazie: " )



def main():
    """
    main method
    """
    FILE_NAME ='contacts.json'
    user_filemanager = FileManager(FILE_NAME)
    user_phonebook = Phonebook()
    if os.path.exists(FILE_NAME): 
       user_phonebook.contacts = user_filemanager.load()
    user_action = menu()
    while user_action != "7":
        if user_action == "1":
           try:
               name= input("Nome: ")
               surname= input("Cognome: ")
               phone= int(input("Numero: "))
               user_phonebook.add_new_contact(surname,name,phone)
           except ValueError:
               print("Numero di telefono non valido")
           except:
               print("Errore in input")
         
        if user_action == "2": 
           user_phonebook.display_all_contacts()
        if user_action == "3": 
           user_phonebook.delete_contact()
        if user_action == "4": 
           user_phonebook.search_contact()
        if user_action == "5": 
           user_phonebook.search_contact_by_name()
        if user_action == "6":
           surname= input("Cognome: ")
           name = input("Nome: ")
           user_phonebook.update_contact(surname,name)
        user_action = menu()
 
    user_filemanager.save(user_phonebook.contacts)
    
    

if __name__ == "__main__":
    main()


