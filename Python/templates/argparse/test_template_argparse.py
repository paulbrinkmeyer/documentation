from mock import patch, MagicMock

import template_argparse as target


@patch("template_argparse._a_parse_arguments", autospec=True)
def test__a_main(mock_apa):
    # setup
    mock_arguments = MagicMock()
    mock_arguments.test_name = "a_test_name"
    mock_apa.return_value = mock_arguments

    # actual function call
    target._a_main()

    # validate results
    assert 1 == mock_apa.call_count

@patch("template_argparse.argparse.ArgumentParser", autospec=True)
def test__a_parse_arguments(mock_ap):
    # setup
    mock_arguments = {"test_name": "mock_test"}
    mock_parser = MagicMock()
    mock_parser.parse_args.return_value = mock_arguments
    mock_ap.return_value = mock_parser

    # actual function call
    arguments = target._a_parse_arguments()

    # validate results
    assert arguments == mock_arguments
