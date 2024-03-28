

class Tabuleiro:
    
    def __init__(self):
        self.casas = [None] * 52
        
    def addPeca(self, peca):
        self.casas[peca.position] = peca
        
    
        
        
    