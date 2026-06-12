class age_varification():
   def set_age(self, age):
      if age < 0:
         print("valueError")
      elif age < 18:
         print("Under age error")
      elif age > 100:
         print("invalid age error")
      else:
         print("valid age")


a = age_varification()
a.set_age(age = 28)
    