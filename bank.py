class ContoBancario:

    total_accounts = 0 # variabile di classe

    def __init__(self,iban,saldo,nome) -> None:
        self.iban = iban
        self.nome = nome
        self.saldo = saldo

        ContoBancario.total_accounts += 1 # quando creo un istanza aumenta di numero

    def deposito(self,importo):
        
        self.saldo += importo
        print(f"{importo} depositato. Il nuovo saldo è {self.saldo}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")

    @staticmethod
    def valida_account(iban):
        if isinstance(iban,int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        
account1 = ContoBancario(1234567890,0,"Alice")

account1.deposito(500)
ContoBancario.get_total_accounts()