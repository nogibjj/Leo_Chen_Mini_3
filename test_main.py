from main import square_number


def test_square():
    """Testing square function"""
    assert square_number(5) == 25
    assert square_number(7) == 49
    assert square_number(9) == 81
    print("Success")


if __name__ == "__main__":
    test_square()
