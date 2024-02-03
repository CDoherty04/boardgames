from boardgame import Boardgame


def display_menu():
    """Prints the user menu to the terminal"""
    print("1. Print all games highest Gibbons rating to lowest")
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


def menu1(games):
    """Prints all games highest Gibbons rating to lowest"""

    # Sorts games based on Gibbons ratings, and reverses the list to get highest to lowest
    games = sorted(games)
    games.reverse()

    # Print all games
    print("")
    for game in games:
        print(str(game))


def menu2(games):
    """Obtains a year from the user and either print all the games from that year or print 'No games found'"""

    # Get year
    while True:
        try:
            year = int(input("Enter a year: ").strip())
            break
        except ValueError:
            print("That is not a valid year, try again...\n")

    print(f"\nGames from the year {year}:\n")

    # Print all games if they belong in year
    at_least_one = False
    for game in games:

        if int(game.yearpublished) == year:
            at_least_one = True
            print(str(game))

    if not at_least_one:
        print("No games found\n")


def menu3(games):
    """Obtains a weight (0-5) from the user and prints all games at or below that weight"""
    pass


def menu4(games):
    """Obtain a float (0-10) from the user and prints all games where the people's rating and Dr. Gibbons rating
    are separated by that much or more"""
    pass


def menu5(games):
    """Obtains a player count and prints all games that are best at said count"""
    pass


class Executive:
    """In charge of reading file input, creating board game objects, printing the menu, and executing all queries"""
    def __init__(self, file_name):
        self.file_name = file_name

    def run(self):
        """handles function calls and user input for the program"""

        # Create boardgames based on file
        boardgames = create_boardgames(self.file_name)
        print("")

        while True:
            display_menu()

            # Get user input and handle queries
            menu_choice = input("\nEnter a number 1-6 to choose: ")

            match menu_choice:

                case "1":
                    menu1(boardgames)

                case "2":
                    menu2(boardgames)

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
