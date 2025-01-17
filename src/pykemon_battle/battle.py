import random
import time

# from .move import Move
from .pokemon import Pokemon
from .utils import enemy_turn_logic, player_turn_logic, show_health_bar


class Battle:
    """
    Class that contains the battle logic of the game
    """

    def __init__(self, team_size=6):
        self.get_team(team_size=team_size)
        self.enemy_team = None

    def get_team(self, team_size=6):
        """
        Build the team of the player
        """
        self.team = []
        # TODO: Implement the multiple move selections
        # move_selection = input(
        #     "Your team's moveset will be selected: "
        #     "\n1: Automatic"
        #     "\n2: Manual"
        #     "\n3: Random"
        #     "\nAnswer : "
        # )
        move_selection = "random"
        for team_index in range(team_size):
            current_pokemon = None
            while current_pokemon is None:
                pokemon_id = input(f"Choose pokemon {team_index + 1} by id or name: ")
                try:
                    current_pokemon = Pokemon(pokemon_id)
                except ValueError:
                    print("Invalid input")
                    continue
            current_pokemon.get_moves(move_selection=move_selection)
            self.team.append(current_pokemon)

    def choose_dificulty(self):
        """
        Choose the difficulty of the battle
        """
        # TODO: Implent all the difficulities
        # diff = input(
        #     "Choose the difficulty: \n1: Random \n2: Easy \n3: Hard \nAnswer : "
        # )
        difficulty = "random"
        self.build_enemy_team(difficulty=difficulty)

    def build_enemy_team(self, difficulty):
        """
        Build the enemy team
        """
        if difficulty == "random":
            self.enemy_team = []
            for _ in range(len(self.team)):
                enemy_pokemon = Pokemon(random.randint(1, 151))
                enemy_pokemon.get_moves(move_selection="random")
                self.enemy_team.append(enemy_pokemon)
        else:
            raise NotImplementedError

    def start_battle(self):
        """
        Start the battle
        """
        print("Fetching enemy details")
        self.choose_dificulty()
        print("Your opponent is ready")
        time.sleep(0.5)

        print("Trainers. Prepare your teams:")
        time.sleep(1.5)
        print("3")
        time.sleep(0.8)
        print("2")
        time.sleep(0.8)
        print("1")
        time.sleep(1)
        print("FIGHT")
        time.sleep(1)

        player_remaining_pokemon = self.team.copy()
        enemy_remaining_pokemon = self.enemy_team.copy()

        player_pokemon = self.team[0]
        enemy_pokemon = self.enemy_team[0]

        player_turn = player_pokemon.stats["speed"] >= enemy_pokemon.stats["speed"]

        while len(player_remaining_pokemon) > 0 and len(enemy_remaining_pokemon) > 0:
            print("\n")
            show_health_bar(pokemon_1=player_pokemon, pokemon_2=enemy_pokemon)
            time.sleep(2)
            print("\n")
            if player_turn:
                enemy_pokemon, enemy_remaining_pokemon = player_turn_logic(
                    player_pokemon, enemy_pokemon, enemy_remaining_pokemon
                )
            else:
                player_pokemon, player_remaining_pokemon = enemy_turn_logic(
                    player_pokemon, enemy_pokemon, player_remaining_pokemon
                )
            player_turn = not player_turn

        if len(player_remaining_pokemon) > 0:
            print("You won!")
        else:
            print("You lost!")
