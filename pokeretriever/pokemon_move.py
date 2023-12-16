from pokeretriever.pokedex_object import PokedexObject


class PokemonMove(PokedexObject):
    def __init__(self, poke_id: int = -1, name: str = "", **kwargs):
        """
        Initializes the PokemonMove object.
        :param name: a string of move name
        :param poke_id: an int of move id
        :param generation: a string of generation
        :param accuracy: an int of accuracy
        :param pp: an int of pp value
        :param power: an int of power
        :param move_type: a string of move type
        :param damage_class: a string of damage class
        :param effect_short: a string of effect short
        :param learn_level: an int of learn level
        :param url: a string of url
        """
        super().__init__(poke_id, name)
        self._generation = kwargs.get('generation', "")
        self._accuracy = kwargs.get('accuracy', -1)
        self._pp = kwargs.get('pp', -1)
        self._power = kwargs.get('power', -1)
        self._move_type = kwargs.get('move_type', "")
        self._damage_class = kwargs.get('damage_class', "")
        self._effect_short = kwargs.get('effect_short', "")
        self._learn_level = kwargs.get('learn_level', -1)
        self._url = kwargs.get("url", "")

    def __str__(self) -> str:
        """
        Gets the string that prints the object.
        :return: a string
        """
        return f"▶ Move\nName: {self.name}\nID: {self.poke_id}\nGeneration: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\nPP: {self.pp}\nPower: {self.power}\nMove Type: {self.move_type}\n" \
               f"Damage Class: {self.damage_class}\nEffect Short: {self.effect_short}\n" \
               f"Level Learned: {self.learn_level}"

    def get_shortened_info(self) -> str:
        """
        Gets the shortened_info for pokemon report.
        :return: a string
        """
        return f"Move ▶ Name: {self.name}, Level Learned: {self.learn_level}, Url: {self.url}"

    def get_learn_level(self) -> int:
        """
        Returns learn level.
        :return: a int
        """
        return self._learn_level

    def set_learn_level(self, learn_level: int) -> None:
        """
        Sets learn level.
        """
        self._learn_level = learn_level

    def get_generation(self) -> str:
        """
        Returns generation.
        :return: a string representing the generation
        """
        return self._generation

    def set_generation(self, generation: str) -> None:
        """
        Sets generation.
        """
        self._generation = generation

    def get_accuracy(self) -> int:
        """
        Returns accuracy.
        :return: an integer representing the accuracy
        """
        return self._accuracy

    def set_accuracy(self, accuracy: int) -> None:
        """
        Sets accuracy.
        :param accuracy: an integer representing the accuracy
        """
        self._accuracy = accuracy

    def get_pp(self) -> int:
        """
        Gets PP.
        :return: an int representing pp
        """
        return self._pp

    def set_pp(self, pp: int) -> None:
        """
        Sets PP.
        :param pp: a integer representing pp
        """
        self._pp = pp

    def get_power(self) -> int:
        """
        Gets power.
        :return: an integer representing power
        """
        return self._power

    def set_power(self, power: int) -> None:
        """
        Sets power.
        :param power: an integer representing power
        """
        self._power = power

    def get_move_type(self) -> str:
        """
        Gets a type.
        :return: a string representing type
        """
        return self._move_type

    def set_move_type(self, move_type: str) -> None:
        """
        Sets move type.
        :param move_type: a string representing power
        """
        self._move_type = move_type

    def get_damage_class(self) -> str:
        """
        Gets damage class.
        :return: a string representing damage class
        """
        return self._damage_class

    def set_damage_class(self, damage_class: str) -> None:
        """
        Sets damage class.
        :param damage_class: a string representing damage class
        """
        self._damage_class = damage_class

    def get_effect_short(self) -> str:
        """
        Gets effect short.
        :return: a string representing effect short
        """
        return self._effect_short

    def set_effect_short(self, effect_short: str) -> None:
        """
        Sets effect short.
        :param effect_short: a string representing effect short
        """
        self._effect_short = effect_short

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
    accuracy = property(get_accuracy, set_accuracy)
    pp = property(get_pp, set_pp)
    power = property(get_power, set_power)
    move_type = property(get_move_type, set_move_type)
    damage_class = property(get_damage_class, set_damage_class)
    effect_short = property(get_effect_short, set_effect_short)
    learn_level = property(get_learn_level, set_learn_level)
    url = property(get_url, set_url)
