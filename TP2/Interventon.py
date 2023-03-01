class Intervention:
    def __init__(self ,numero,date,duree,tarifkm,technicien ):
        self.__numero=numero,
        self.__date=date,
        self.__duree=duree,
        self.__tarifkm=tarifkm,
        self.__technicien=technicien,

        def affiche(self):
            print("***Liste des interventions***"
                "Numéro = " , self.__numero ,
                    "Date = " , self.__date, 
                    "Duree =" , self.__duree,
                    "Tarifkm = " , self.__tarifkm,
                    'technicien = ' , self.__technicien)
                
        def fraisKm(self,dist):
            return self.__tarifkm * dist
                
        def fraisMo():
            pass
       
