from boardgame import Boardgame


def display_menu():
    """Prints the user menu to the terminal"""
    print("\n1. Print all games highest Gibbons rating to lowest")
    print("2. Print all games from a year")
    print("3. Print all games with a weight equal to or lower than a provided weight")
    print("4. The People VS Dr. Gibbons")
    print("5. Print best games based on player count")
    print("6. Exit the program")


def create_boardgames(file_name):
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


class Executive:
    """In charge of reading file input, creating board game objects, printing the menu, and executing all queries"""
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        """handles function calls and user input for the program"""
        boardgames = create_boardgames(self.file_name)

        while True:
            display_menu()

            # Get user input and handle queries
            menu_choice = input("\nEnter a number 1-6 to choose\n")

            match menu_choice:

                case "1":
                    # Prints all games highest Gibbons rating to lowest

                    boardgames = sorted(boardgames)
                    boardgames.reverse()

                    for game in boardgames:
                        print(str(game))

                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    break
                case _:
                    print("\nEnter a valid number between 1 and 6")
                    input("Press enter to continue...")

        # Break message
        print("\nExiting...")
