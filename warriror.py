
class Warrior():
    def __init__(self):
        self.ranking_list = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.achievements = []
        self.experience = 100
        self.level = 1
        self.rank = self.get_rank(self.level)
        

    def get_rank(self,arg):
        
        if arg >= 1 and arg <= 9:
            return  "Pushover"
        elif arg >= 10 and arg <= 19:
            return  "Novice"
        elif arg >= 20 and arg <= 29:
            return  "Fighter"
        elif arg >= 30 and arg <= 39:
            return  "Warrior"
        elif arg >= 40 and arg <= 49:
            return  "Veteran"
        elif arg >= 50 and arg <= 59:
            return  "Sage"
        elif arg >= 60 and arg <= 69:
            return  "Elite"
        elif arg >= 70 and arg <= 79:
            return  "Conqueror"
        elif arg >= 80 and arg <= 89:
            return  "Champion"
        elif arg >= 90 and arg <= 99:
            return  "Master"
        elif arg == 100:
            return "Greatest"
        else:
            return "Greatest"
            


    def battle(self,opp):
        
        message = ""
        
        if opp > 100:
            return "Invalid level"
    
        if  opp > 0:

            d = opp - self.level
                    
            if d == 0:
                self.experience += 10
                message = "A good fight"
            elif d == -1:
                self.experience += 5
                message =  "A good fight"
            elif d <= -2:
                self.experience += 0

                message = "Easy fight"
            
            elif d >= 5 and ((opp//10) - self.ranking_list.index(self.rank) ) > 0:
                self.experience += 0

                message = "You've been defeated"
                
            elif d > 0:
                self.experience += 20*d*d

                message = "An intense fight"
        elif opp > 100:
            message =  "Invalid level"
            
        else:
            self.rank = self.get_rank(self.level)
            message =  "Invalid level"

        self.improve()
        return message
        



    def improve(self):
        
        if self.experience >= 100 and self.experience <= 10000:
        
            self.level = self.experience // 100

            self.rank = self.get_rank(self.level)
        else:
            self.level = 100
            self.experience = 10000
                

        

    def training(self,params):
        description = params[0]
        xps = params[1]
        min_level = params[2]

        if self.level >= min_level:
            self.experience = self.experience + xps
            self.achievements.append(description)
            self.improve()
            self.rank = self.get_rank(self.level)
            return description
        else:
            self.rank = self.get_rank(self.level)
            return "Not strong enough"

