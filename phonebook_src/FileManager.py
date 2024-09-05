# -*- coding: utf-8 -*-
"""

@author: Paolo Minniti
"""
import json

class FileManager:
    
    """
    class for json file management
    """
   
    def __init__(self, filename):
        """
        inizialization
        filename(str)
        """
        self.__filename= filename
            
            
    def load(self):
        """
        method that reads data from a json file
        """
        with open(self.__filename,'r') as json_file:
           datafile = json.load(json_file)
           return datafile
        
 
    
    def save(self,contacts):
        """
        method that saves data to a json file
        """
        with open(self.__filename,'w') as json_file:
            return json.dump(contacts ,json_file)
        
    def __help__(self):
        help(self)
        

      


