from src.main import print_hw


def test_hw():
    """
    Sample test
    """
    hw_str = print_hw()
    assert hw_str == "Hello World!"
