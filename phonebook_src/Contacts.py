# -*- coding: utf-8 -*-
"""

@author: Paolo Minniti
"""
class Contact:
    
    """
    class for contact management
    """
    
    def __init__(self, surname, name,phone):
        """
        inizialization
        surname(str)
        name(str)
        phone(int)
        """
        self.__surname= surname
        self.__name= name
        self.__phone= phone

    def getName(self):
        """
        method that returns the contact name
        """
        return self.__name
        
    def getSurname(self):
        """
        method that returns the contact surname
        """
        return self.__surname

        
    def getDict(self):
        """
        method that returns a dictionary
        """
        return self.__dict__

    def getPhone(self):
        """
        method that returns the contact phone number
        """
        return self.__phone

    def __str__(self):
        """
        method that returns a string 
        """
        return "Name: " + self.__name + " Cognome: " + self.__surname  + " Numero: " + str(self.__phone)
    
    def __help__(self):
        help(self)


