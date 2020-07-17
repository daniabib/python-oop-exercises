import emoji
import random

class Caneta:
    pinturas = [":winking_face_with_tongue:", ":zipper-mouth_face:", ":grinning_face_with_big_eyes:", ]

    def __init__(self, modelo, cor, ponta=0.5, carga=100, tampada=True):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampada = False
        self.empty = "Acabou a tinta! =("
        
    def check_to_print(self):
        if (not self.tampada):
            print('A caneta está tampada, besta!')
        elif (self.carga <= 0):
            print(self.empty)
        else:
            return True            

    def escrever(self, texto):
        if (self.check_to_print()):
            print(texto)
            self.carga -= 10
    

    def rabiscar(self):
        if (self.check_to_print()):
            print('----/\--\/----')        
            self.carga -= 5

    def pintar(self):
        if (self.check_to_print()):
            emj = random.randint(0, len(self.pinturas)-1)
            print(emoji.emojize(self.pinturas[emj]))        
            self.carga -= 20

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False
              
    def recarregar(self):
          self.carga = 100

can_1 = Caneta("BIC", "Azul", ponta=0.8)

# print(can_1.modelo)
# print(can_1.cor)
# print(can_1.ponta)
# print(can_1.carga)
# print(can_1.tampada)
# print(can_1.pintar())
# print(can_1.pintar())
# print(can_1.pintar())


