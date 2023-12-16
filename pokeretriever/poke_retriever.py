import asyncio
import aiohttp

from pokeretriever.pokedex_resource import PokedexResource
from pokeretriever.pokedex_object import PokedexObject
from pokeretriever.pokedex_object_factory import PokemonFactory, AbilityFactory, MoveFactory, StatFactory

BASE_ENDPOINT = 'https://pokeapi.co/api/v2/'


def execute_request(resource, query_value) -> PokedexObject:
    """
    Interface for retrieving data from the PokeAPI.
    :param resource: The resource to query.
    :param query_value: The value to query.
    :return: A PokedexObject.
    """
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(_get_pokemon_object(resource, query_value))
    resource_parse_map = {
        PokedexResource.POKEMON.value: PokemonFactory(),
        PokedexResource.ABILITY.value: AbilityFactory(),
        PokedexResource.MOVE.value: MoveFactory(),
        PokedexResource.STAT.value: StatFactory(),
    }
    return resource_parse_map[resource].create_pokedex_obj(response)


async def _get_pokemon_object(resource, query_value) -> dict:
    """
    Retrieves a PokedexObject from the PokeAPI.
    :param resource: The resource to query.
    :param query_value: The value to query.
    :return: A dict of the JSON response.
    """
    endpoint = BASE_ENDPOINT + resource + '/' + query_value
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                response = await response.json()
                return response
    except Exception as e:
        print("Error: Failed to retrieve data from endpoint.")
        print("-Error Detail: ", end="")
        print(e)
        exit(1)
