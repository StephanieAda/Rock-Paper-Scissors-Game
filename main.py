import random
MOVES = ["rock", "paper", "scissors"]
P1_SCORE = 0
P2_SCORE = 0
CYCLE = 0
no_round = 0
game_continue = True
my_own_move = " "
opp_move = random.choice(MOVES)


class Player:
    def move(self):
        return 'rocks'

    def learn(self, my_move, their_move):
        pass

    class RandomPlayer:

        def move(self):
            return random.choice(MOVES)

        def learn(self, my_move, their_move):
            pass

    class HumanPlayer:

        def move(self):
            choose = input("Pick A Move. Rock, Paper or Scissors?: ").lower()
            if choose == 'rock' or choose == 'paper' or choose == 'scissors':
                return choose
            else:
                print("Incorrect Choice, Try Again")
                return self.move()

        def learn(self, my_move, their_move):
            pass

    class ReflectPlayer:
        def move(self):
            return opp_move

        def learn(self, my_move, their_move):
            global my_own_move, opp_move
            my_own_move = my_move
            opp_move = their_move

    class CyclePlayer:
        def move(self):
            global CYCLE
            if CYCLE >= 3:
                CYCLE = 0
            choice = MOVES[CYCLE]
            CYCLE += 1
            return choice

        def learn(self, my_move, their_move):
            pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def scoreboard(s1, s2):
    global P1_SCORE, P2_SCORE
    if beats(s1, s2):
        print('Player 1 wins')
        P1_SCORE += 1
    elif s1 == s2:
        print('Draw')
    else:
        P2_SCORE += 1
        print("Player 2 wins")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        scoreboard(move1, move2)
        print(f"Score = {P1_SCORE}:{P2_SCORE}")
        # print(score_board)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        global no_round, game_continue
        print("Game Start!")

        # if you want the game to play 5 rounds before asking ou if you want to continue, chane it to "0",
        # then uncomment next line
        # while game_continue % 5 == 0:
        #    game_continue += 1
        #             OR
        # if you want it to end when one player is ahead by 5 points
        # while (P1_SCORE - P2_SCORE) == 5 or (P1_SCORE - P2_SCORE) == -5:
        
        while game_continue:
            print(f"Round {no_round}: ")
            self.play_round()
            if input("Continue? y or n:").lower() == 'y':
                no_round += 1
            else:
                print("Game Over")
                print(f"Score = {P1_SCORE}:{P2_SCORE}")
                if P1_SCORE > P2_SCORE:
                    print("Player 1 Wins!")
                elif P2_SCORE > P1_SCORE:
                    print("Player 2 Wins!")
                else:
                    print("Player 1 and Player 2 Draw!")
                game_continue = False


if __name__ == '__main__':
    player = Player()
    random_player = player.RandomPlayer()
    human_player = player.HumanPlayer()
    reflect_player = player.ReflectPlayer()
    cycle_player = player.CyclePlayer()

    game = Game(human_player, reflect_player)
    game.play_game()
