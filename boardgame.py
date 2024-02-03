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
        """
        Readable format should look like the below entry

        ============
        name
        gibbonsrating
        baverage
        avgweight
        yearpublished
        bggbestplayers
        ============

        """

        return (f"============\n"
                f"{self.name}\n"
                f"{self.grating}\n"
                f"{self.avgrating}\n"
                f"{self.avgweight}\n"
                f"{self.yearpublished}\n"
                f"{self.bggbestplayers}\n"
                f"============\n")

    def __repr__(self):
        """Official/background format"""
        return (f"boardgame.Boardgame({self.name}, {self.grating}, "
                f"{self.avgrating}, {self.avgweight}, "
                f"{self.yearpublished}, {self.bggbestplayers})")

    def __lt__(self, other):
        if float(self.grating) < float(other.grating):
            return True
        return False
