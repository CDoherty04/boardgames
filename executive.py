from boardgame import Boardgame


class Executive:
    """In charge of reading file input, creating board game objects,
    printing the menu, and executing all queries"""
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        """handles function calls and user input for the program"""
        boardgames = self.create_boardgames(self.file_name)
        for game in boardgames:
            print(str(game) + "\n")

        while True:
            self.display_menu()

            # Get user input and handle queries
            menu_choice = input("\nEnter a number 1-6 to choose\n")
            match menu_choice:
                case "1":
                    pass
                case "6":
                    break

        # Break message
        print("\nExiting...")

    def display_menu(self):
        """Prints the user menu to the terminal"""
        print()
        print("1. Print all games highest Gibbons rating to lowest")
        print("2. Print all games from a year")
        print("3. Print all games with a weight equal to or lower than a provided weight")
        print("4. The People VS Dr. Gibbons")
        print("5. Print best games based on player count")
        print("6. Exit the program")

    def create_boardgames(self, file_name):
        """Uses the Boardgame class to create a list of games"""
        with open(file_name, "r", encoding='utf8') as file:
            lines = file.readlines()

        # Remove extraneous white space and ignore "Title" row
        lines = [line.strip() for line in lines]
        lines.pop(0)

        games = []
        for line in lines:
            game_values = line.split("\t")
            games.append(Boardgame(game_values[0], game_values[1], game_values[2],
                                   game_values[3], game_values[4], game_values[5]))

        return games
