from pokeretriever.pokedex_object import PokedexObject


class PokemonStat(PokedexObject):
    """
     A class describing stats of the pokemon.
    """

    def __init__(self, poke_id: int = -1, name: str = "", **kwargs):
        """
        Initializes the Stat object.
        :param name: a string describing poke name
        :param poke_id: an integer describing poke id
        :param base: an int of base value
        :param is_battle_only: a boolean whether the pokemon is battle only
        :param url: a string of url
        """
        super().__init__(poke_id, name)
        self._base = kwargs.get('base', -1)
        self._is_battle_only = kwargs.get('is_battle_only', False)
        self._url = kwargs.get('url', "")

    def __str__(self) -> str:
        """
        Gets the string that prints the object
        :return: a string
        """
        return f"▶ Stat\nName: {self.name}\n" \
               f"Base Value: {self.base}\n" \
               f"ID: {self.poke_id}\n" \
               f"Battle Only: {self._is_battle_only}"

    def get_shortened_info(self) -> str:
        """
        Gets the shortened_info for pokemon report.
        :return: a string
        """
        return f"Stat ▶ Name: {self.name}, Base Value: {self.base}, Url: {self.url}"

    def get_battle_only(self) -> bool:
        """
        Gets the status of battle only
        :return: a boolean
        """
        return self._is_battle_only

    def set_battle_only(self, is_battle_only: bool) -> None:
        """
        Sets the status of battle only
        :param is_battle_only: a boolean
        """
        self._is_battle_only = is_battle_only

    def get_base(self) -> int:
        """
        Gets the base value of this object
        :return: a string
        """
        return self._base

    def set_base(self, base: int) -> None:
        """
        Sets the base value of this object
        :param base: a string
        :return:
        """
        self._base = base

    def get_url(self) -> str:
        """
        Gets url.
        :return: a string representing url
        """
        return self._url

    def set_url(self, url: str) -> None:
        """
        Sets url.
        :param url: a string representing url
        """
        self._url = url

    battle_only = property(get_battle_only, set_battle_only)
    base = property(get_base, set_base)
    url = property(get_url, set_url)
