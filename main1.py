from Documentaire import Documentaire, Exemplaire 
import copy
D0 = Documentaire("pyton" ,"01/1/2023")
D1 = Documentaire("java" ,"1/06/2022")
DC = copy.copy (D0)

print (D0.ToString())
print(D1.ToString())
print(D0.Eqauls(D1))
print (DC.ToString())

E2 = Exemplaire("pyton" ,"01/1/2023","12/05/2023")
E3 = Exemplaire("java" ,"1/06/2022","15/107/2023",213)

print (E2.ToString())
print(E3.ToString())
print(E2.Eqauls(E3))