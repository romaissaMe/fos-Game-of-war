import random
#modelisation des cartes
#un tableau taille = 52 chaque carte est codée par un entier de 1 à 52, la carte la plus puissante est celle avec le numéro le plus grand 

class Game:
    def __init__(self):
        self.cartes=[num for num in range(2, 15) for _ in range(4)]
        self.player1_hand=[] # manche joueur 1
        self.player2_hand=[] # manche joueur 2
        self.player1_stack=[] # tas d'attente joueur 1
        self.player2_stack=[] # tas d'attente joueur 2
        self.n_reach_stack_player1=0 # nombre de fois d'arrive de joueur 1 a son tas d'attente
        self.n_reach_stack_player2=0 # nombre de fois d'arrive de joueur 2 a son tas d'attente

    def shuffles_distribute(self):
        random.shuffle(self.cartes)
        self.player1_hand=self.cartes[0:26]
        self.player2_hand=self.cartes[26:]

    def play_random_card(self,player_hand): #jouer par joueur 1
        if(len(player_hand)!=0):
            index=random.randint(0,len(player_hand)-1)
            c=player_hand[index]
            del player_hand[index]
            
        else:
            if(self.player1_stack!=0):
                index=random.randint(0,len(self.player1_stack)-1)
                c=self.player1_stack[index]
                del self.player1_stack[index]
                self.n_reach_stack_player1 += 1 
            else:
                return None
        return c        


    
    def play_best_card(self,player_hand): #jouer par joueur 2
        if(len(player_hand)!=0):
            player_hand.sort(reverse=True)
            c = player_hand[0]
            del player_hand[0]
        else:
            if(self.player2_stack!=0):
                self.player2_stack.sort(reverse=True)
                c=self.player2_stack[0]
                del self.player2_stack[0] 
                self.n_reach_stack_player2 += 1 
            else:
                return None
        return c
    
    
    def play_worst_card(self,player_hand): #jouer par joueur 2 en cas de draw
        if(len(player_hand)!=0):
            player_hand.sort()
            c=player_hand[0]
            del player_hand[0]
        else:
            if(self.player2_stack!=0):
                self.player2_stack.sort()
                c=self.player2_stack[0]
                del self.player2_stack[0]
                self.n_reach_stack_player2 += 1 
            else:
                return None
        return c 

    def play_game(self):
        #les cartes jouées sur la table lors d'un tour 
        on_table=[]
        while(self.n_reach_stack_player1<3 or self.n_reach_stack_player2<3):

            #player1 choisie une carte aleatoire
            c1=self.play_random_card(self.player1_hand)
            #si c1 est none cad manche et tas d'attente  sont vides
            if(not c1):
                print("player 2 won the game !")
                break
            
            #player2 choisie sa meilleure carte 
            c2=self.play_best_card(self.player2_hand)
            if(not c2):
                print("player 1 won the game !")
                break

            print(f'player_1 played {c1} : player_2 played {c2}')
            on_table.extend([c1,c2])

            #regles de jeu
            if c1>c2:
                self.player1_stack.extend(on_table)
                on_table=[]
                print(f'player_1 got the round')
            elif c1<c2:
                self.player2_stack.extend(on_table)
                on_table=[]
                print(f'player_2 got the round')
            else:
                #c1=c2 donc utiliser 2 cartes comme token
                print(f'player_1 and player_2 playes same cards they will use tokens')
                #player_1 choisie une carte aleatoire
                tk1=self.play_random_card(self.player1_hand)
                if(not tk1):
                    print("player_1 run out of cards player_2 won the game !")
                    break
                #player_2 choisie sa mauvaise carte
                tk2=self.play_worst_card(self.player2_hand)
                if(not tk2):
                    print("player_2 run out of cards player_1 won the game !")
                    break
                
                on_table.extend([tk1,tk2])
        
        if(self.n_reach_stack_player1==3):
            print("player_2 won the game!")
        elif(self.n_reach_stack_player2==3):
            print("player_3 won the game!")
        


if __name__=='__main__':
    game=Game()
    game.shuffles_distribute()
    game.play_game()
