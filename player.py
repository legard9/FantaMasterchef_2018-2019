class Player: 

    name = None
    points = None
    bet = None

    ##inizializza il giocatore
    def __init__(self,name,bet):
        self.name = name
        self.bet = bet

    #stampa lo stato del giocatore con tutte le sue informazioni
    def status (self):
        print("Giocatore:", self.name, "- Punti:", self.points , "\n" , "Previsione:", self.bet, "\n")

    #calcola i punti guadagnati dal giocatore
    def calc_points (self,exits):
        points = 0  
        table_exact = [12,10,8,7,6,5,4,3,2,1,1]
        table_almost = [3,3,3,2,2,2,1,1,1,1,0]
        for i in range (0,11):
            if self.bet[i] == exits[i]:
                points += table_exact[i]
            elif (i-1 >= 0) and (self.bet[i] == exits[i-1]):
                points += table_almost[i]
            elif (i+1 <= 10) and (self.bet[i] == exits[i+1]):
                points += table_almost[i]
            else:
                continue
        self.points = points        
