from wild_cat.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and not player.guild == 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        filtered_player = [p for p in self.players if p.name == player]
        if filtered_player:
            current_player = filtered_player[0]
            return f'Player {current_player} is already in the guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        filtered_player = [p for p in self.players if p.name == player_name]
        if not filtered_player:
            return f'Player {player_name} is not in the guild'
        player = filtered_player[0]
        self.players.remove(player)
        player.guild = "Unaffiliated"
        return f'Player {player_name} has been removed from the guild.'

    def guild_info(self):
        res = f'Guild: {self.name}\n'
        for p in self.players:
            res += p.player_info()
        return res


player = Player('George', 50, 100)
second = Player('Pesho', 20, 200)
print(player.add_skill('Shield Break', 20))
print(player.player_info())
guild = Guild('UGT')
second_guild = Guild('Eli')
print(second_guild.assign_player(second))
print(guild.assign_player(second))
print(guild.assign_player(player))
print(guild.guild_info())
print(second_guild.guild_info())
