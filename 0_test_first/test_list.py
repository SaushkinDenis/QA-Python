class TestList:

    # Проверка команды append()
    def test_list_one(self, fixture_one, random_number):
        l1 = fixture_one
        l1.append(random_number)
        assert len(l1) == 6

    # Проверка команды clear()
    def test_list_two(self, fixture_one):
        l1 = fixture_one
        l1.clear()
        assert len(l1) == 0

    # Проверка команды insert()
    def test_list_three(self, fixture_one, random_number):
        l1 = fixture_one
        l1.insert(0, random_number)
        assert l1[0] == random_number

    # Проверка команды pop()
    def test_list_four(self, fixture_one):
        assert fixture_one.pop(0) == 1

    # Проверка команды count()
    def test_list_five(self, fixture_one):
        assert fixture_one.count(1) == 1
