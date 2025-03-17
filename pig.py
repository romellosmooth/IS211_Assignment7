class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_to_score(self, points):
        self.total_score += points

    def reset_score(self):
        self.total_score = 0
import random

class Die:
    def __init__(self):
        random.seed(0)  # Ensuring reproducibility
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value
class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.die = Die()
        self.current_player = self.player1
        self.turn_total = 0

    def switch_turn(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )
        self.turn_total = 0

    def play_turn(self):
        print(f"{self.current_player.name}'s turn.")
        while True:
            print(f"Current turn total: {self.turn_total}")
            print(f"Total score: {self.current_player.total_score}")
            action = input("Enter 'r' to roll or 'h' to hold: ").lower()

            if action == 'r':
                roll = self.die.roll()
                print(f"You rolled a {roll}!")
                if roll == 1:
                    print("You rolled a 1! Turn over. No points added.")
                    self.switch_turn()
                    break
                else:
                    self.turn_total += roll
            elif action == 'h':
                self.current_player.add_to_score(self.turn_total)
                print(f"{self.current_player.name}'s score is now {self.current_player.total_score}.")
                self.switch_turn()
                break
            else:
                print("Invalid input. Please enter 'r' or 'h'.")

    def play_game(self):
        print("Welcome to the game of Pig!")
        while self.player1.total_score < 100 and self.player2.total_score < 100:
            self.play_turn()

        winner = (
            self.player1 if self.player1.total_score >= 100 else self.player2
        )
        print(f"Congratulations {winner.name}, you won with a score of {winner.total_score}!")
if __name__ == "__main__":
    game = Game("Player 1", "Player 2")
    game.play_game()


    
