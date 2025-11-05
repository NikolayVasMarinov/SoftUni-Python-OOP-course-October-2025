from First_steps_in_OOP_exercise.zad8.project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str, pokemons: list[Pokemon] = []):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str) -> str:
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon.name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for p in self.pokemons:
            result += "\n- " + p.pokemon_details()

        return result