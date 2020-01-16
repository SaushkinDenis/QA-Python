class TestSet:

    # Проверка команды pop()
    def test_set_one(self, fixture_two):
        s1 = fixture_two
        assert s1.pop() == 1
        print(s1)

    # Проверка команды add()
    def test_set_two(self, fixture_two, random_number):
        s1 = fixture_two
        s1.add(random_number)
        assert random_number in s1

    # Проверка команды clear()
    def test_set_three(self, fixture_two):
        fixture_two.clear()
        assert len(fixture_two) == 0

    # Проверка команды discard()
    def test_set_four(self, fixture_two):
        f1 = fixture_two
        f1.discard(1)
        assert f1 == {2, 3, 4, 5}

    # Проверка команды union()
    def test_set_five(self, fixture_two):
        assert fixture_two.union({6, 7}) == {1, 2, 3, 4, 5, 6, 7}
