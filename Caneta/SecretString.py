# -*- coding: utf-8 -*-

class SecretString:
    ''' Mostra uma maneira incorreta de se guardar uma senha. 
        O interpreter não impede que variáveis com  __ sejam acessadas.'''
        
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    
    def decrypt(self, pass_phrase):
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''