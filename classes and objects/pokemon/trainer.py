from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        searched_pokemon = [p for p in self.pokemon if p.name == pokemon_name]
        if not searched_pokemon:
            return f'Pokemon is not caught'
        self.pokemon.remove(searched_pokemon[0])
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        details = [f'- {i.pokemon_details()}\n' for i in self.pokemon]
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n{''.join(details)}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
