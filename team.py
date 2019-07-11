class Team():
    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id
        self.win = 0
        self.loss = 0
        self.draw = 0
        self.goals = 0
        self.gp = 0
        
    def update_gp(self):
        self.gp = self.win + self.loss + self.draw
        
    def add_win(self):
        self.win += 1
        self.update_gp() 
        
    def add_loss(self):
        self.loss += 1
        self.update_gp()
    
    def add_draw(self):
        self.draw += 1
        self.update_gp()
        
    def add_goals(self, goal):
        self.goals += goal
        
    def team_print(self):
        print("Team Name: {}".format(self.name))
        print("2011 Games Played: {}".format(self.gp))
        print("2011 Wins: {}".format(self.win))
        print("2011 Draws: {}".format(self.draw))
        print("2011 Losses: {}".format(self.loss))
        print("2011 Total Goals: {}\n".format(self.goals))
        