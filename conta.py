class Conta:
    """Classe conta corrente.
    """
       
    def __init__(self, numero, titular, saldo, limite) -> None:        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):        
        print("Saldo {0} do titular {1}".format(self.__saldo, self.__titular))

    def deposita(self, valor):        
        self.__saldo += valor

    def saca(self, valor):        
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Valor do saque ultrapassa o limite.")    

    def __pode_sacar(self, valor):
        valor_do_saque = self.__saldo + self.__limite
        return valor <= valor_do_saque

    def transfere(self, destino,valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite    

    @staticmethod
    def codigo_banco():
        return "001"

    
