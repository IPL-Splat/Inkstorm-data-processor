class Player:
    """
    Stores player info
    """
    def __init__(self, PlayerName, County):
        self.name = PlayerName
        self.country = County

    def __str__(self):
        return "Player: {}\nCounty: {}\n~~\n".format(self.name, self.country)


class Team:
    """
    Stores team information
    """
    def __init__(self, Name):
        self.teamName = Name
        self.ID = Name.replace(" ", "_")
        self.players = []

    def add_member(self, member: Player):
        self.players.append(member)

    def play_count(self) -> int:
        return len(self.players)

    def __str__(self):
        playerStr = ""
        for player in self.players:
            playerStr += str(player)
        return "TeamName: {}\nTeamID: {}\nPlayers:\n~~\n{}\n---------".format(self.teamName, self.ID, playerStr)
