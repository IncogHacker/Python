



class Errors:

    @property
    def attributerror(self):
        try:
            x=10
            x.append(12)

        except AttributeError as t:
              return f"Your Error is--{t}"
        
    @property
    def typeerror(self):
         
         try:
              x=10
              y="rishabh"

              z=x+y

         except TypeError as t:
              return f"Your Error is {t}"
    
        






obj=Errors()

print(obj.attributerror)
print(obj.typeerror)









