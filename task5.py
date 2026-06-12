class login_system:
    __password = "python@123"
    __attempt = 3

    def wrong_password(self):
       if self.__password != self.__password:
           self.__attempt -= 1
           print("wrong password")

    def account_lock(self):
        if self.__attempt == 0:
           print("Account lock error ")
           


    def correct_password(self):
        if self.__password == self.__password:
           print(" login sucessfully")

l = login_system()
l.wrong_password()
l.correct_password()
l.account_lock()
