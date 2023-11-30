class Documentaire :
    _count = 0 
    def __init__(self, titre, date) :
        self._titre = titre
        self._date = date 
        Documentaire._count += 1
        self._code = Documentaire._count

    def Getcode(self) :
        return self._code
    
    def setcode(self, code) :
        self._code = code 

    def Gettitre(self) :
        return self._titre
    
    def settitre(self, titre) :
        self._titre = titre 

    def Getdate(self) :
        return self._date
    
    def setdate(self, date) :
        self._date = date 

    def Getcount(self) :
        return Documentaire._count
    
    def ToString (self) :
        return "Code :" + str(self.Getcode()) + ";  Title" + str(self.Gettitre()) + ";  Date" + str(self.Getdate()) + "."
    
    def Eqauls (self,doc1) :
        if self._code == doc1._code :
            return True
        else : 
            return False
        
class Exemplaire (Documentaire) :
    
    def __init__(self, titre, date,  dateach, numero = 12345 ):
        super().__init__(titre, date)
        self.__numero = numero
        self.__dateach = dateach

    def Getnumero(self) :
        return self.__numero
    
    def setnumero(self, numero) :
        self.__numero = numero 

    def Getdateach(self) :
        return self.__dateach
    
    def setdateach(self, dateach) :
        self.__dateach = dateach

    def ToString(self):
        return super().ToString() + "; Number :" + str(self.Getnumero()) + "; Date of purchase :" + str(self.Getdateach()) + "."
    
    def Eqauls(self, ex1):
        if self.__numero == ex1.__numero :
            return True
        else : 
            return False
