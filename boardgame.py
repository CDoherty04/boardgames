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
        # Format player counts separated by commas (2,3) into 2 or 3
        player_counts = self.bggbestplayers.split(",")
        returned_str = ""

        # One suggested player count formatted without commas or "or"s
        if len(player_counts) == 1:
            returned_str = player_counts[0]

        # Two suggested player count formatted without commas but with an "or"
        elif len(player_counts) == 2:
            returned_str = player_counts[0] + " or " + player_counts[1]

        # More than two suggested player count formatted with commas and "or"s
        else:
            returned_str = player_counts[0]
            for player in player_counts[1:]:
                returned_str += ", " + player
            # Inject "or" before the last number (3, 'or '4)
            returned_str = returned_str[:-1] + "or " + returned_str[-1]

        return (f"{self.name}, published in {self.yearpublished}, "
                f"has a Gibbon's rating of: {self.grating}, "
                f"an average rating on BGG of {self.avgrating}, "
                f"a complexity of {self.avgweight}, and a best "
                f"player count of {returned_str} player(s).")

    def __repr__(self):
        """Official/background format"""
        return (f"boardgame.Boardgame({self.name}, {self.grating}, "
                f"{self.avgrating}, {self.avgweight}, "
                f"{self.yearpublished}, {self.bggbestplayers})")
