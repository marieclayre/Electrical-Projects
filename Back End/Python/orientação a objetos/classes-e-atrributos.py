class carros():
    def __init__(self,marca,modelo,ano,cor, statusFarol = 'desligado'):
        self.marca = marca
        self.modelo = modelo
        self.anoDeFabricacao = ano
        self.cor = cor

        self.statusFarol = statusFarol
        self.velocimetro = 0

    def ligarFarol(self):
        if (self.statusFarol == 'desligado'):
            self.statusFarol = 'ligado' 
            print("Farol ligado")
        else:
            print("Farol já ligado")
    def desligarFarol(self):
        if(self.statusFarol == 'ligado'):
            self.statusFarol = 'desligado'
            print("Farol desligado")
    def acelerar(self, acresVelocidade):
        self.velocimetro = self.velocimetro + acresVelocidade
    def frear(self, decVelocidade = 5):
        if (self.velocimetro > decVelocidade):
            self.velocimetro = self.velocimetro - decVelocidade
        else:
            self.velocimetro = 0
#criando objetos
gol = carros("wolks","gol", 2010,"laranja")
fusca = carros("wolks","fusca",1990,"azul claro")
uno = carros("fiat","uno",2000,"azul escuro", statusFarol= 'ligado')
gol2 = carros("wolks","gol", 2010,"laranja")

#utilizando objetos
print(gol.velocimetro)
gol.acelerar(10)
print(gol.velocimetro)

print(gol2.velocimetro)
gol2.acelerar(20)
print(gol2.velocimetro)

fusca.ligarFarol()
print(fusca.statusFarol)
fusca.ligarFarol()
fusca.statusFarol
fusca.desligarFarol()

print(uno.statusFarol)

print(gol.velocimetro)
gol.frear(12)
print(gol.velocimetro)
'''
#interação do objetos
i = 0 
lista = []

while i < 3:
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano de fabricação: "))
    cor = input("Digite a cor: ")
    carro = carros(marca, modelo, ano, cor)
    lista.append(carro)
    i+= 1

print(lista[0].marca)
lista[1].ligarFarol()
'''

