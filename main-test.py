from main import Add
def test_Add():
    assert Add(2, 3) == 5
    assert Add(-1, 1) == 0
    print("Test passed")

if __name__ == "__main__":
    test_Add()
    print("All tests passed")
   