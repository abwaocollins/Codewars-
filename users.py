class User:
    def __init__(self):
        self.ranking_list = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.i = 0
        self.rank = self.ranking_list[self.i]
        self.progress = 0

    def inc_progress(self,activity):



        d = self.ranking_list.index(activity) - self.ranking_list.index(self.rank)

        if d == -1:
            self.progress += 1
        elif d < -1:
            self.progress += 0
        elif d == 0:
            self.progress += 3
        elif d >= 1:
            self.progress += 10*d*d


        while self.progress >= 100:
            new_prog = self.progress - 100
            self.progress = new_prog
            self.i += 1
            if self.i > 15:
                self.i = 15
            self.rank = self.ranking_list[self.i]

        if self.rank == 8:
            self.progress = 0
            
                                                
user = User()
print(user.rank)
print(user.progress)
user.inc_progress(-7)
print(user.progress)
user.inc_progress(-5)
print(user.rank)
print(user.progress)