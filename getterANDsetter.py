class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,new_balance):
        self.__balance=new_balance

acc1=Bankaccount("megha",100000)
acc1.set_balance(5000)
print(acc1.name,acc1.get_balance())            