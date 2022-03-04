from main import Add

def TestAdd():
    assert Add(2, 3) == 5
    print("Add Function works correctly")

if __name == '__main__':
    TestAdd()