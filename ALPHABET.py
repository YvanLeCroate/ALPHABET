
class Alphabet :
   
    def __init__ (self, filename) :

        try :
             with open (filename, "r") as file :

                self.filename = filename
                self.alphabet = {}
                for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
                    self.alphabet[lettre] = []
                
                print(f"\nalphabet de {str(filename)[:-4]}")
                for line in file.readlines() :

                    if line[2:4] == "->" and len(line) > 7:
                        lettre = line[0]
                        line = line.strip("\n")
                        line = line[6:]
                        line = line.split("#")

                        proies = []
                        for proie in line :
                            proies.append(proie.split(":"))

                        for proie in proies :
                            self.alphabet[lettre].append(Proie(proie[0].strip(), proie[1].strip(), proie[2].strip()))

                    if line[:15] == "Total de points" :
                        self.anciens_points = int(line.split()[4])
                        print(f"points actuels : {self.anciens_points}\n")


                        self.save(self.filename)

        except FileNotFoundError:

            self.filename = filename      
            self.alphabet = {}      
            for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
                self.alphabet[lettre] = []

            self.save(self.filename)


    def add (self, proie) :

        rajouter = True

        for lettre in self.alphabet :

            for deja_proie in self.alphabet[lettre] :
                if proie.nom == deja_proie.nom :
                        rajouter = False
                        numero_deja_proie = self.alphabet[lettre].index(deja_proie)

            if lettre == proie.nom[0].upper() and rajouter :
                self.alphabet[lettre].append(proie)

            elif lettre == proie.nom[0].upper() :
                self.alphabet[lettre][numero_deja_proie] = proie
      
        self.save(self.filename)                    

    def add_p(self, nom, date="date inconnue") :
        self.add(Proie(nom, "pécho", date))

    def add_k(self, nom, date="date inconnue") :
        self.add(Proie(nom, "ken", date))

    def add_multiple(self, list) :
        for proie in list :
            self.add(proie)

    def add_multiple_p(self, list) :
        for proie in list :
            self.add_p(proie)

    def add_multiple_k(self, list) :
        for proie in list :
            self.add_k(proie)

    def save (self, filename) :

        with open (filename, "w") as file :

            file.write("="*150 + "\n")
            file.write("charo" + "\n\n")

            self.points = 0
            for key,value in self.alphabet.items() :
                proies = " "
                if value != [] :
                    if key in "BHQUXY" :
                        self.points += 10
                    else :
                        self.points += 5

                for proie in value :
                    proies += f"{proie}  #  "
                    
                    if proie.action.lower() in ["pecho", "pécho", "bouillave", "embrasser"]:
                        self.points += 1
                    elif proie.action.lower() in ["dormi", "dodo", "couilles bleues"]:
                        self.points += 2
                    elif proie.action.lower() in ["pipi"]:
                        self.points += 3
                    elif proie.action.lower() in ["prélis", "prelis", "branlette", "doigter", "sucer", "sucette", "masturber", "cuni", "lécher", "lècher", "lecher"]:
                        self.points += 4
                    elif proie.action.lower() in ["baiser", "sexe", "sex", "ken"]:
                        self.points += 6

                proies = proies[:-5]
                file.write(f"{key} -> {proies}\n")
            
            file.write("\n")
            file.write("Total de points : " + str(self.points) + "\n")
            file.write("="*150)
            


class Proie :
    
    def __init__ (self,nom,action,date="date inconnue") :
        self.nom = nom
        self.action = action
        self.date = date

    def changer_action(self,nouveau) :
        self.action = nouveau
        
    def __str__ (self) :        
        return f"{self.nom} : {self.action} : {self.date}"
        
        
