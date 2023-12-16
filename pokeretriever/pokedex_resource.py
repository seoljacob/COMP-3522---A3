import enum


class PokedexResource(str, enum.Enum):
    """
    Enum class of mode of the pokedex.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"
