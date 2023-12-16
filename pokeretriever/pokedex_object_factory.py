import abc
from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokemon import Pokemon
from pokeretriever.pokemon_ability import PokemonAbility
from pokeretriever.pokemon_move import PokemonMove
from pokeretriever.pokemon_stat import PokemonStat


class PokedexObjectFactory(abc.ABC):
    """
    Abstract class representing the factory of Pokedex objects.
    """
    @abc.abstractmethod
    def create_pokedex_obj(self, json) -> PokedexObject:
        """
        Creates a Pokedex object.
        :param json: a dict of the JSON response
        :return: a PokedexObject
        """
        pass


class PokemonFactory(PokedexObjectFactory):
    """
    Creates a Pokemon object.
    """
    def create_pokedex_obj(self, json) -> Pokemon:
        parsed_data = {
            "poke_id": json["id"],
            "name": json["name"],
            "height": json["height"],
            "weight": json["weight"],

            "stats": [PokemonStat(
                **{"name": stat_json['stat']["name"],
                   "url": stat_json['stat']['url'],
                   "base": stat_json['base_stat']})
                for stat_json in json['stats']],

            "types": [pokemon_type["type"]["name"] for pokemon_type in json['types']],

            "abilities": [PokemonAbility(
                **{"name": ability_json['ability']["name"],
                   "url": ability_json['ability']['url']
                   })
                for ability_json in json['abilities']],

            "moves": [PokemonMove(
                **{"name": move_json['move']["name"],
                   "url": move_json['move']['url'],
                   "learn_level": move_json['version_group_details'][0]['level_learned_at']})
                for move_json in json['moves']],
        }
        return Pokemon(**parsed_data)


class AbilityFactory(PokedexObjectFactory):
    """
    Creates a PokemonAbility object.
    """
    def create_pokedex_obj(self, json) -> PokemonAbility:
        effects_en = [entry for entry in json["effect_entries"] if entry["language"]["name"] == "en"]
        effect = "N/A"
        effect_short = "N/A"
        if len(effects_en) > 0:
            try:
                effect = effects_en[0]['effect'].replace("\n", "")
                effect_short = effects_en[0]['short_effect']
            except AttributeError or TypeError:
                pass

        parsed_data = {
            "poke_id": json["id"],
            "name": json["name"],
            "generation": json['generation']['name'],
            "effect": effect,
            "effect_short": effect_short,
            "pokemon": [pokemon['pokemon']['name'] for pokemon in json['pokemon']]
        }
        return PokemonAbility(**parsed_data)


class MoveFactory(PokedexObjectFactory):
    """
    Creates a PokemonMove object.
    """
    def create_pokedex_obj(self, json) -> PokemonMove:
        effects_en = [entry for entry in json["effect_entries"] if entry["language"]["name"] == "en"]
        effect_short = effects_en[0]['short_effect'] if len(effects_en) > 0 else "N/A"

        parsed_data = {
            "poke_id": json["id"],
            "name": json["name"],
            "generation": json['generation']['name'],
            "accuracy": json['accuracy'],
            "pp": json['pp'],
            "power": json['power'],
            "move_type": json['type']['name'],
            "damage_class": json['damage_class']['name'],
            "effect_short": effect_short,
        }
        return PokemonMove(**parsed_data)


class StatFactory(PokedexObjectFactory):
    """
    Creates a PokemonStat object.
    """
    def create_pokedex_obj(self, json) -> PokemonStat:
        parsed_data = {
            "poke_id": json["id"],
            "name": json["name"],
            "is_battle_only": json["is_battle_only"]
        }
        return PokemonStat(**parsed_data)
