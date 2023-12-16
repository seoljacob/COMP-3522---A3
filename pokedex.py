import argparse
from pokedex_request import PokedexRequest
from pokedex_maker import PokedexMaker


class Pokedex:
    """
    Creates a Pokedex object.
    """
    def __init__(self):
        pass

    @staticmethod
    def is_text_file(filename):
        """
        Checks if the file is a text file.
        :param filename: a string
        :return: a boolean
        """
        return filename.endswith(".txt")

    @staticmethod
    def setup_request_commandline() -> PokedexRequest:
        """
        Sets up the request from command line.
        :return: a PokedexRequest
        """
        # set up the arguments
        parser = argparse.ArgumentParser()

        parser.add_argument("mode", choices=["pokemon", "ability", "move"], help="select a mode")

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--inputfile", help="a text file that ends in '.txt'")
        group.add_argument("--inputdata", help="a name or id")

        # stores true args.expanded if --expanded specified, else stores false
        parser.add_argument("--expanded", action="store_true", help="see more details")

        parser.add_argument("--output", help="a text file that ends in '.txt'")

        # read the arguments
        try:
            args = parser.parse_args()
            input_request = PokedexRequest()

            input_request.mode = args.mode

            try:
                if args.inputfile or len(args.inputfile) == 0:
                    input_file = args.inputfile
                    if not Pokedex.is_text_file(input_file):
                        raise Exception("Input file must end in '.txt'")
                    input_request.input_file = input_file
            except TypeError:
                input_request.output_file = False

            if args.inputdata:
                inputdata = args.inputdata
                if inputdata.isdigit():
                    input_request.id = [inputdata]
                elif inputdata.isalpha():
                    input_request.name = [inputdata]
                else:
                    raise Exception("ID must only contain digits and name must only contain alphabets.")

            # may need to handle this here or in the request handler line -> expanded only applies to pokemon mode
            input_request.is_expanded = args.expanded
            try:
                if args.output or len(args.output) == 0:
                    output_file = args.output
                    if not Pokedex.is_text_file(output_file):
                        raise Exception("Output file must end in '.txt'")
                    input_request.output_file = output_file
                else:
                    input_request.output_file = False
            except TypeError:
                input_request.output_file = False

            return input_request
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()


def main(input_request: PokedexRequest):
    """
    Run the program.
    """
    pokedex_maker = PokedexMaker()
    pokedex_maker.execute_request(input_request)


if __name__ == "__main__":
    request = Pokedex.setup_request_commandline()
    main(request)
