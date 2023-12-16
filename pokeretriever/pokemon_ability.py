from pokeretriever.pokedex_object import PokedexObject


class PokemonAbility(PokedexObject):
    def __init__(self, poke_id: int = -1, name: str = "", **kwargs):
        """
        Initializes the PokemonAbility object.
        :param name: a string of move name
        :param poke_id: an int of move id
        :param generation: a string of move generation
        :param effect: a string of move effect
        :param effect_short: a string of move effect short
        :param pokemon: a list of strings of pokemon
        :param url: a string of move url
        """
        super().__init__(poke_id, name)
        self._generation = kwargs.get("generation", "")
        self._effect = kwargs.get("effect", "")
        self._effect_short = kwargs.get("effect_short", "")
        self._pokemon = kwargs.get("pokemon", [])
        self._url = kwargs.get("url", "")

    def __str__(self) -> str:
        """
        Gets the string that prints the object.
        :return: a string
        """
        return f"▶ Ability \nName: {self.name}\n" \
               f"Generation:{self.generation} \n" \
               f"Effect:{self.effect} \n" \
               f"ShortEffect:{self.short_effect} \n" \
               f"Pokemons:{', '.join(self.pokemon)}"

    def get_shortened_info(self) -> str:
        """
        Gets the shortened_info for pokemon report.
        :return: a string
        """
        return f"Ability ▶ Name: {self.name}, Url: {self.url}"

    def get_generation(self) -> str:
        """
        Gets a generation.
        :return: a string
        """
        return self._generation

    def set_generation(self, generation: str) -> None:
        """
        Sets a generation.
        :param generation: a string
        """
        self._generation = generation

    def get_effect(self) -> str:
        """
        Gets an effect.
        :return: a string
        """
        return self._effect

    def set_effect(self, effect: str) -> None:
        """
        Sets an effect.
        :param effect: a string
        """
        self._effect = effect

    def get_effect_short(self) -> str:
        """
        Gets an effect - short.
        :return: a string
        """
        return self._effect_short

    def set_effect_short(self, effect_short: str) -> None:
        """
        Sets an effect - short.
        :param effect_short: a string
        """
        self._effect_short = effect_short

    def get_pokemon(self) -> list[str]:
        """
        Gets a pokemon list.
        :return: a string
        """
        return self._pokemon

    def set_pokemon(self, pokemon: list[str]) -> None:
        """
        Sets a pokemon.
        :param pokemon: a string
        """
        self._pokemon = pokemon

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

    generation = property(get_generation, set_generation)
    effect = property(get_effect, set_effect)
    short_effect = property(get_effect_short, set_effect_short)
    pokemon = property(get_pokemon, set_pokemon)
    url = property(get_url, set_url)
