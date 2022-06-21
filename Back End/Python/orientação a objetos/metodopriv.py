class carros():
    def __init__(self,marca,modelo,ano,cor, statusFarol = 'desligado'):
        self.marca = marca
        self.modelo = modelo
        self.anoDeFabricacao = ano
        self.cor = cor

        self.statusFarol = statusFarol
        self.velocimetro = 0
        self.__status = False

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
    def getstatus(self):
        return self.__status
    def setstatus(self, chave, novostatus):
        chave_certa = self.__verificachave(chave)
        if chave_certa:
            self.__status = novostatus
        else:
            print("Status não pode ser alterado")
    def __verificachave(self, chave):
        if chave == 123456:
            return True
        else:
            return False

fox = carros("Wolks","Fox","2009","Prata")
print(fox.getstatus())

fox.setstatus(123456,True)
print(fox.getstatus())