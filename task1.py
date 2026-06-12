class employee:
    __salary = 50000
    def increment(self):
        self.__salary += 10000

    def decreament(self):
        self.__salary -= 5000

    def get_sallery(self):
        print(self.__salary)

e = employee()
e.increment()
e.decreament()
e.get_sallery()
