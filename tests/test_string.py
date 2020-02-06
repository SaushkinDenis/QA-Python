class TestString:

    """Проверка команды concat()"""
    def test_string_one(self, fixture_four):
        assert fixture_four + " 1" == "test 1"

    """Проверка команды repeat()"""
    def test_string_two(self, fixture_four):
        assert (fixture_four * 2) == "testtest"

    """Проверка команды len()"""
    def test_string_three(self, fixture_four):
        assert len(fixture_four) == 4

    """Проверка команды get()"""
    def test_string_four(self, fixture_four):
        assert fixture_four[0] == 't'

    """Проверка команды isalpha()"""
    def test_string_five(self, fixture_four):
        assert fixture_four.isalpha()
        assert not fixture_four.isdigit()
