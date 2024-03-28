from dado import Dado
from peca import LudoPeca

#Dado
dado = Dado()

peca = LudoPeca("red")

dadoSorteado = dado.roll()
print("O dado sorteou: " + str(dadoSorteado))

peca.move(dadoSorteado)

print("Posicao da peca: " + str(peca.position))

#no ludo sao 56 casas para percorrer e somar pontos/tirar pecas do jogo


