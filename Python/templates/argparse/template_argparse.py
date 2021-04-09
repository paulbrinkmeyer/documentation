import argparse

def _a_main():
    arguments = _a_parse_arguments()
    argument_name = arguments.argument_name

    # ...

def _a_parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-a",
        "--argument_name",
        required=True,
        help="The name of the test to run"
    )

    arguments = parser.parse_args()

    return arguments

if __name__ == '__main__':
    _a_main()
