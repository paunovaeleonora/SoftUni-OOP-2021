from project.player.player import Player


class PlayerRepository:
    def __init__(self):

        self.players = []

    def add(self, player: Player):
        if any(p.username == player.username for p in self.players):
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        p = self.find(player)
        self.players.remove(p)

    def find(self, username: str):
        searched_player = [player for player in self.players if player.username == username][0]
        return searched_player

    @property
    def count(self):
        return len(self.players)


