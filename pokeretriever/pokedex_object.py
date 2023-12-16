from abc import ABC


class PokedexObject(ABC):
    """
    Abstract class representing Pokedex object.
    """
    def __init__(self, pokedex_id: int, name: str) -> None:
        """
        Initializes the Pokedex object.
        :param name: a string describing the pokemon name
        :param pokedex_id: an integer describing poke id
        """
        self._poke_id = pokedex_id
        self._name = name

    def get_poke_id(self) -> int:
        """
        Returns the id of the pokemon.
        :return: an int
        """
        return self._poke_id

    def set_poke_id(self, poke_id: int) -> None:
        """
        Sets the poke id.
        :param poke_id: an int
        """
        self._poke_id = poke_id

    def get_name(self) -> str:
        """
        Returns the name of pokemon.
        :return: a string
        """
        return self._name

    def set_name(self, name: str) -> None:
        """
        Sets the name of the pokemon.
        :param name: a string
        """
        self._name = name

    poke_id = property(get_poke_id, set_poke_id)
    name = property(get_name, set_name)
