class PokedexRequest:
    def __init__(self):
        """
        Initializes the request.
        """
        self._mode = None
        self._input_file = None
        self._id = None
        self._name = None
        self._is_expanded = None
        self._output_file = None
        self._pokedex_result = None

    def get_mode(self):
        """
        Get the mode of the request.
        """
        return self._mode

    def set_mode(self, value):
        """
        Set the mode of the request.
        """
        self._mode = value

    def get_input_file(self):
        """
        Get the input file of the request.
        :return: a string
        """
        return self._input_file

    def set_input_file(self, value):
        """
        Set the input file of the request.
        """
        self._input_file = value

    def get_id(self):
        """
        Get the id of the request.
        :return: a list
        """
        return self._id

    def set_id(self, value):
        """
        Set the id of the request.
        :param value: an list
        """
        self._id = value

    def get_name(self):
        """
        Get the name of the request.
        :return: a list
        """
        return self._name

    def set_name(self, value):
        """
        Set the name of the request.
        """
        self._name = value

    def get_is_expanded(self):
        """
        Get the is_expanded of the request.
        :return: a boolean
        """
        return self._is_expanded

    def set_is_expanded(self, value):
        """
        Set the is_expanded of the request.
        :param value: a boolean
        """
        self._is_expanded = value

    def get_output_file(self):
        """
        Get the output file of the request.
        :return: a string
        """
        return self._output_file

    def set_output_file(self, value):
        """
        Set the output file of the request.
        :param value: a string
        """
        self._output_file = value

    def get_pokedex_result(self):
        """
        Get the pokedex result of the request.
        :return: a list of PokedexObject
        """
        return self._pokedex_result

    def set_pokedex_result(self, value):
        """
        Set the pokedex result of the request.
        :param value: a list of PokedexObject
        """
        self._pokedex_result = value

    mode = property(get_mode, set_mode)
    input_file = property(get_input_file, set_input_file)
    id = property(get_id, set_id)
    name = property(get_name, set_name)
    is_expanded = property(get_is_expanded, set_is_expanded)
    output_file = property(get_output_file, set_output_file)
    pokedex_result = property(get_pokedex_result, set_pokedex_result)

    def __str__(self):
        """
        Returns a string representation of the request.
        :return: a string
        """
        return self.mode