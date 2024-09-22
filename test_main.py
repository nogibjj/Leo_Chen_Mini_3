from main import statistics, count_col, count_row


def test_count_col():
    num_col = count_col()
    assert num_col == 7


def test_count_row():
    num_row = count_row()
    assert num_row == 135


def test_statistics():
    mean, median, std = statistics()
    assert round(mean, 3) == 360.185
    assert median == 221
    assert round(std, 3) == 450.581


if __name__ == "__main__":
    test_count_col()
    test_count_row()
    test_statistics()
    print("Success!")
