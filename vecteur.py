class Vecteur2D ():
    _count = 0
    def __init__(self, abscisse  , ordonne ):
        self.__abscisse = abscisse
        self.__ordonne = ordonne
        Vecteur2D._count = Vecteur2D._count+ 1
    
    def getabscisse(self):
        return self.__abscisse
    def getordonne(self):
        return self.__ordonne
    
    def setabscisse(self, abscisse):
        self.__abscisse = abscisse
    def setordonne(self, ordonne):
        self.__ordonne = ordonne
    
    def Tostring (self):
        print("\nX = ",self.getabscisse(),"/ Y = ",self.getordonne() , "vector number : ",Vecteur2D._count)
    
    def Equals (self,V1):

        if (self.getabscisse()==V1.getabscisse()) and  (self.getordonne()==V1.getordonne()):
            return True
        else:
            return False
    
    def norme (self):
        print("\nthe standard is : {} cm".format(0.5**((self.__abscisse)**2+(self.__ordonne)**2)))

class Vecteur3D (Vecteur2D):
    def __init__(self, abscisse, ordonne ,z):
        super().__init__(abscisse, ordonne)
        self.z = z

    def getz(self):
        return self.z
    def setz(self,z):
        self.z = z
    def Tostring (self):
        print("X = ",self.getabscisse()," Y = ",self.getordonne() ," Z = ",self.getz(), "le vecteur numero : ",Vecteur2D._count)
    def Equals (self,V3):

        if (self.getabscisse()==V3.getabscisse()) and  (self.getordonne()==V3.getordonne()) and (self.getz()==V3.getz()):
            print("TRUE")
        else:
            print("FALSE")
    def norme (self):
        print("\n the standard is : {} cm".format(0.5**((self.getordonne())**2+(self.getabscisse())**2+(self.getz())**2)))
