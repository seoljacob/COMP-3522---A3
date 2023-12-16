import abc
from pokedex_request import PokedexRequest
from pokeretriever.pokedex_resource import PokedexResource
from pokeretriever import poke_retriever


class BaseRequestHandler(abc.ABC):
    """
    Baseclass for all handlers that handle Pokedex Request.
    """

    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, input_request: PokedexRequest):
        """
        Each handler would have a specific implementation of how it processes a request.
        :param input_request: a Reqeust
        """
        pass

    def set_handler(self, handler):
        """
        Each handler can invoke another handler at the end of its processing of the request.
        :param handler: a BaseRequestHandler
        """
        self._next_handler = handler


class RequestModeHandler(BaseRequestHandler):
    """
    Handles reqeust mode.
    """

    def __init__(self):
        """ Construct RequestModeHandler class. """
        super().__init__()

    @staticmethod
    def get_query_value(input_request) -> list:
        """
        Get query value.
        :param input_request: a Request
        :return: a list of names or ids
        """
        query_value = []

        if input_request.id:
            query_value += input_request.id
        if input_request.name:
            query_value += input_request.name

        return query_value

    def handle_request(self, input_request: PokedexRequest):
        """
        Validate the request mode.
        :param input_request: a Reqeust
        """
        global pokedex
        query_value = RequestModeHandler.get_query_value(input_request)
        pokedex_objs = []

        for query in query_value:
            if input_request.mode == PokedexResource.POKEMON.value:
                pokedex = poke_retriever.execute_request(PokedexResource.POKEMON.value, query)
                pokedex_objs.append(pokedex)
            elif input_request.mode == PokedexResource.ABILITY.value:
                pokedex = poke_retriever.execute_request(PokedexResource.ABILITY.value, query)
                pokedex_objs.append(pokedex)
            elif input_request.mode == PokedexResource.MOVE.value:
                pokedex = poke_retriever.execute_request(PokedexResource.MOVE.value, query)
                pokedex_objs.append(pokedex)

        input_request.pokedex_result = pokedex_objs
        return self._next_handler.handle_request(input_request)


class RequestInputFileHandler(BaseRequestHandler):
    """
    Handles request input.
    """

    def __init__(self):
        """ Construct RequestInputTypeHandler class. """
        super().__init__()

    def handle_request(self, input_request: PokedexRequest):
        """
        Validate the request input file.
        :param input_request: a Request
        """
        ids = []
        names = []
        if input_request.input_file:
            try:
                with open(input_request.input_file, "r") as file:
                    data = file.readlines()
                    for line in data:
                        if line.strip().isdigit():
                            ids.append(line.strip())
                        else:
                            names.append(line.strip().lower())
                if ids:
                    input_request.id = ids
                if names:
                    input_request.name = names
            except FileNotFoundError:
                print("Error: File does not exist")
            except Exception as e:
                print(e)

        return self._next_handler.handle_request(input_request)


class RequestExpandHandler(BaseRequestHandler):
    """
    Handles request expand.
    """

    def __init__(self):
        """ Construct RequestExpandHandler class. """
        super().__init__()

    def handle_request(self, input_request: PokedexRequest):
        """
        Validate the request expand.
        :param input_request: a Request
        """
        if input_request.is_expanded and input_request.mode == PokedexResource.POKEMON.value:
            updated_pokedex_objs = []
            for pokedex_obj in input_request.pokedex_result:
                updated_pokedex_objs.append(pokedex_obj.get_expanded_string())
            input_request.pokedex_result = updated_pokedex_objs
        # set next handler
        self._next_handler.handle_request(input_request)


class RequestOutputHandler(BaseRequestHandler):
    """
    Handles request output.
    """

    def __init__(self):
        """ Construct RequestOutputTypeHandler class. """
        super().__init__()

    def handle_request(self, input_request: PokedexRequest):
        """
        Validate the request output.
        :param input_request: a Request
        """
        if input_request.output_file:
            with open(input_request.output_file, "w", encoding="utf-8") as file:
                for pokedex_obj in input_request.pokedex_result:
                    file.write(str(pokedex_obj) + "\n")
        else:
            for pokedex_obj in input_request.pokedex_result:
                print(pokedex_obj)
