from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokemon_ability import PokemonAbility
from pokeretriever.pokemon_move import PokemonMove
from pokeretriever.pokemon_stat import PokemonStat


class Pokemon(PokedexObject):
    """
    Pokomen Class represents a Pokemon object.
    """

    def __init__(self, poke_id: int = -1, name: str = "", **kwargs):
        """
        Initialize the attributes of Pokemon class.
        :param name: a string
        :param poke_id: an int
        :param height: an int
        :param weight: an int
        :param stats: a list of PokemonStat
        :param types: a list of types
        :param abilities: a list of PokemonAbility
        :param moves: a list of PokemonMove
        """
        super().__init__(poke_id, name)
        self._height = kwargs.get('height')
        self._weight = kwargs.get('weight')
        self._stats = kwargs.get('stats')
        self._types = kwargs.get('types')
        self._abilities = kwargs.get('abilities')
        self._moves = kwargs.get('moves')

    def __str__(self) -> str:
        """
        Return a statement of the class.
        :return: a string describing the class
        """
        stats_string = ',\n'.join([data.get_shortened_info() for data in self.stats])
        move_string = ',\n'.join([data.get_shortened_info() for data in self.moves])
        abilities_string = ',\n'.join([data.get_shortened_info() for data in self.abilities])
        return f"{self.name.title()} ID: {self.poke_id} ▶ Height:{self.height}, Weight: {self.weight}," \
               f" Types: {', '.join(self.types).title()}\n" \
               f"### Abilities ###\n" \
               f"{abilities_string}\n" \
               f"### Stats ###\n" \
               f"{stats_string}\n" \
               f"### Moves ###\n" \
               f"{move_string}"

    def get_expanded_string(self) -> str:
        """
        Gets the string of the object for expanded infos
        :return: a string
        """
        base_info = f"{self.name.title()} ID: {self.poke_id} -> Height:{self.height}, Weight: {self.weight} \n"
        expanded_ability = '\n\n'.join([str(ability) for ability in self.abilities])
        expanded_stat = '\n\n'.join([str(stat) for stat in self.stats])
        expanded_move = '\n\n'.join([str(move) for move in self.moves])
        return f"{base_info}\n{expanded_ability}\n{expanded_stat}\n{expanded_move}"

    def get_height(self) -> int:
        """
        Gets height
        :return: int
        """
        return self._height

    def set_height(self, height: int) -> None:
        """
        Sets height.
        :param height: int
        """
        self._height = height

    def get_weight(self) -> int:
        """
        Gets weight
        :return: int
        """
        return self._weight

    def set_weight(self, weight: int) -> None:
        """
        Sets weight.
        :param weight: int
        """
        self._weight = weight

    def get_stats(self) -> list[PokemonStat]:
        """
        Gets stats
        :return: list of PokemonStat
        """
        return self._stats

    def set_stats(self, stats) -> None:
        """
        Sets stats.
        :param stats: a list
        """
        self._stats = stats

    def get_types(self) -> list[str]:
        """
        Gets types
        :return: a list of types
        """
        return self._types

    def set_types(self, types: list[str]) -> None:
        """
        Sets types.
        :param types: a list of types
        """
        self._types = types

    def get_abilities(self) -> list[PokemonAbility]:
        """
        Gets abilities.
        :return: a list of PokemonAbility
        """
        return self._abilities

    def set_abilities(self, abilities: list[PokemonAbility]) -> None:
        """
        Sets abilities.
        :param abilities: a list of PokemonAbility
        """
        self._abilities = abilities

    def get_moves(self) -> list[PokemonMove]:
        """
        Gets moves
        :return: a list of PokemonMove
        """
        return self._moves

    def set_moves(self, moves: list[PokemonMove]) -> None:
        """
        Sets moves.
        :param moves: a list of PokemonMove
        """
        self._moves = moves

    height = property(get_height, set_height)
    weight = property(get_weight, set_weight)
    stats = property(get_stats, set_stats)
    types = property(get_types, set_types)
    abilities = property(get_abilities, set_abilities)
    moves = property(get_moves, set_moves)
