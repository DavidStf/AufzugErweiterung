class Aufzug():
   
    #Atributte
    def __init__(self,bezeichnung,maxKapazität,tiefsteEtage,aktuelleEtage,höchsteEtage,aktuelleAnzahlPersonen,Türauf,):
        self.bezeichnung= bezeichnung
        self.maxKapazität=maxKapazität
        self.tiefsteEtage=tiefsteEtage
        self.aktuelleEtage=aktuelleEtage
        self.höchsteEtage= höchsteEtage
        self.aktuelleAnzahlPersonen=aktuelleAnzahlPersonen
        self.Türauf=False

    #Methode
    def einsteigenPerson(self,person):
        self.Türauf = True
        print(":Die Tür geht auf:",self.Türauf)
        self.aktuelleAnzahlPersonen +=person
        print(self.aktuelleAnzahlPersonen,"Person(en) ist(sind) eingestiegen")
        
        if self.aktuelleAnzahlPersonen > self.maxKapazität:
            print("Achtung max Kapazität erreicht!!")
        print("\n")
         

    def aussteigenPerson(self,person):
        self.Türauf = True
        print("Die Tür geht auf:",self.Türauf)
        self.aktuelleAnzahlPersonen -=person
        print("Es ist(sind) nur ",self.aktuelleAnzahlPersonen,"Person(en) im Aufzug")
        print("\n")
      
        

    def hochfahren(self,etage):
        self.aktuelleEtage +=etage
        if self.aktuelleEtage < self.höchsteEtage:
            print("hochfahren","Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        else:
            print("Es gibt keine Etagen mehr !")
       

    def runterfahren(self,etage):
        self.aktuelleEtage -=etage
        if self.aktuelleEtage < self.tiefsteEtage:
            print("runterfahren","Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        else:
            print("Es gibt keine Etagen mehr !")

    def info(self):
        print("Aufzug Info")
        print("Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        print("Es ist(sind) nur ",self.aktuelleAnzahlPersonen,"Person(en) im Aufzug")
        
        print(self.aktuelleAnzahlPersonen,"Person(en) ist(sind) eingestiegen")
        
        print("Die Tür ist zu:",self.Türauf)
        #pass

#Kommandos
#Reihenfolge: bezeichnung,maxKapazität,tiefsteEtage,aktuelleEtage,höchsteEtage,aktuelleAnzahlPersonen,Türauf,
"""aufzug= Aufzug("AufzugNebengebäude",7,0,0,6,0,False)

aufzug.hochfahren(3)
print("\n")
aufzug.einsteigenPerson(8)

aufzug.aussteigenPerson(5)

aufzug.runterfahren(1)
print("\n")
aufzug.info()"""

#Menü Aufbau
print("Es.. ladet.....")
print("Wählen Sie ein der folgenden Optionen aus:")
print("-------------------------------------------")
print(":Für Hochfahren drücken Sie die (1).")
print(":Für Runterfahren drücken Sie die (2)")
print(":Für Einsteigen drücken Sie (3)")
print(":Für Aussteigen drücken Sie (4)")
print("-------------------------------------------")
print(int(input("Wählen Sie eine Option aus:")))
print("\n")