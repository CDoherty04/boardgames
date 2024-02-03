from boardgame import Boardgame


def display_menu():
    """Prints the user menu to the terminal"""
    print("1. Print all games highest Gibbons rating to lowest")
    print("2. Print all games from a year")
    print("3. Print all games with a weight equal to or lower than a provided weight")
    print("4. The People VS Dr. Gibbons")
    print("5. Print best games based on player count")
    print("6. Exit the program")


# todo Use pandas
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

    # Get user input until a valid year is given
    while True:
        try:
            year = int(input("Enter a year: ").strip())
            break
        except ValueError:
            print("That is not a valid year, try again...\n")

    print(f"\nGames from the year {year}:\n")

    # Print games that belong in the given year
    at_least_one = False
    for game in games:

        if int(game.yearpublished) == year:
            at_least_one = True
            print(str(game))

    # Case that there are no games published in the given year
    if not at_least_one:
        print("No games found\n")


def menu3(games):
    """Obtains a weight (0-5) from the user and prints all games at or below that weight"""

    # Get user input until a valid weight is given
    while True:
        try:
            weight = float(input("Enter a weight from 0-5 (weight represents the complexity of the game): ").strip())

            # Check for valid range
            if 0.0 <= weight <= 5.0:
                break

            else:
                print("That is not within the range of 0-5, try again...\n")

        except ValueError:
            print("That is not a valid weight, try entering a decimal from 0-5...\n")

    print(f"\nGames less complex or as complex as the weight value of {weight}:\n")

    # Print games that are less complex than given weight
    # There is no case where no games are found
    for game in games:

        if float(game.avgweight) <= weight:
            print(str(game))


def menu4(games):
    """Obtain a float (0-10) from the user and prints all games where the people's rating and Dr. Gibbons rating
    are separated by that much or more"""

    # Get user input until a valid rating is given
    while True:
        try:
            prompt = "Enter a decimal buffer from 0-10 to separate the average rating from Dr. Gibbons rating: "
            buffer = float(input(prompt).strip())

            # Check for valid range
            if 0.0 <= buffer <= 10.0:
                break

            else:
                print("That is not within the range of 0-10, try again...\n")

        except ValueError:
            print("That is not a valid buffer, try entering a decimal from 0-10...\n")

    print(f"\nGames with a buffer greater than {buffer}:\n")

    # Print games that have a buffer greater than or equal to given buffer
    at_least_one = False
    for game in games:

        if abs(float(game.avgrating) - float(game.grating)) >= buffer:
            at_least_one = True
            print(str(game))

    # Case that there are no games with a larger buffer
    if not at_least_one:
        print("No games found\n")


def menu5(games):
    """Obtains a player count and prints all games that are best at said count"""

    # Get user input until a valid player count is given
    while True:
        try:
            player_count = int(input("Enter an integer to represent the preferred player count: ").strip())
            break

        except ValueError:
            print("That is not a valid player count, try entering an integer...\n")

    print(f"\nGames with a preferred player count equal to {player_count}:\n")

    # Print games that have a preferred player count equal to the given player count
    at_least_one = False
    for game in games:

        # Preferred player counts are separated by commas in the tsv file
        best_player_counts = game.bggbestplayers.split(",")

        # So check for every preferred player count
        for pc in best_player_counts:
            if int(pc) == player_count:
                at_least_one = True
                print(str(game))
                break

    # Case that there are no games with said player count
    if not at_least_one:
        print("No games found\n")


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
                    menu3(boardgames)

                case "4":
                    menu4(boardgames)

                case "5":
                    menu5(boardgames)

                case "6":
                    break

                case _:
                    print("\nEnter a valid number between 1 and 6")
                    input("Press enter to continue...\n")

        # Break message
        print("\nExiting...")
