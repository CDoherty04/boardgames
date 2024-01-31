class Boardgame:
    """Blueprint for the boardgames, initializing board game attributes,
    and creating __str__ and __repr__ methods for the games"""
    def __init__(self, name, gibbonsrating, baverage, avgweight,
                 yearpublished, bggbestplayers):
        self.name = name  # Name of the game
        self.grating = gibbonsrating  # Gibbon's Rating
        self.avgrating = baverage  # Game Board Geek Average Rating
        self.avgweight = avgweight  # Game complexity
        self.yearpublished = yearpublished  # Year game was published
        self.bggbestplayers = bggbestplayers  # Best player count

    def __str__(self):
        """Readable format"""
        return (f"{self.name}, published in {self.yearpublished},"
                f" has a Gibbon's rating of: {self.grating},"
                f"an average rating on BGG of {self.avgrating},"
                f"a complexity of {self.avgweight}, and a best"
                f"player count of {self.bggbestplayers}.")

    def __repr__(self):
        """Official/background format"""
        return (f"boardgame.Boardgame({self.name}, {self.grating}, "
                f"{self.avgrating}, {self.avgweight}, "
                f"{self.yearpublished}, {self.bggbestplayers})")
