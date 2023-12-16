from base_request_handler import *
from pokeretriever.pokedex_object import PokedexObject
from pokedex_request import PokedexRequest


class PokedexMaker:
    """
    PokedexMaker executes the request with given input.
    """
    def __init__(self):
        """ Constructs PokedexMaker class. """
        self.header_handler = None
        # Initialize the handlers
        self.request_mode_handler = RequestModeHandler()
        self.request_input_file_handler = RequestInputFileHandler()
        self.request_expand_handler = RequestExpandHandler()
        self.request_output_file_handler = RequestOutputHandler()

    def execute_request(self, input_request: PokedexRequest) -> PokedexObject:
        """
        Accepts a request and start executing the first handler in the appropriate chain.
        :param input_request: a Request
        :return: a PokedexObject
        """
        # Read the input file and save id and names to PokedexRequest
        self.header_handler = self.request_input_file_handler
        self.request_input_file_handler.set_handler(self.request_mode_handler)
        self.request_mode_handler.set_handler(self.request_expand_handler)
        self.request_expand_handler.set_handler(self.request_output_file_handler)

        return self.header_handler.handle_request(input_request)
