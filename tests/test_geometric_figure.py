class TestTriangle:

    def test_get_name(self, fixture_triangle):
        assert "Triangle" == fixture_triangle.name

    def test_get_area(self, fixture_triangle):
        assert 6 == fixture_triangle.get_area()

    def test_get_angles(self, fixture_triangle):
        assert 3 == fixture_triangle.get_angles()

    def test_get_perimeter(self, fixture_triangle):
        assert 12 == fixture_triangle.get_perimeter()

    def test_add_area(self, fixture_triangle, fixture_rectangle):
        assert 18 == fixture_triangle.add_area(fixture_rectangle)


class TestRectangle:
    def test_get_name(self, fixture_rectangle):
        assert "Rectangle" == fixture_rectangle.name

    def test_get_area(self, fixture_rectangle):
        assert 2 == fixture_rectangle.get_area()

    def test_get_angles(self, fixture_rectangle):
        assert 4 == fixture_rectangle.get_angles()

    def test_get_perimeter(self, fixture_rectangle):
        assert 6 == fixture_rectangle.get_perimeter()

    def test_add_area(self, fixture_rectangle, fixture_triangle):
        assert 18 == fixture_rectangle.add_area(fixture_triangle)


class TestSquare:
    def test_get_name(self, fixture_square):
        assert "Square" == fixture_square.name

    def test_get_area(self, fixture_square):
        assert 25 == fixture_square.get_area()

    def test_get_angles(self, fixture_square):
        assert 4 == fixture_square.get_angles()

    def test_get_perimeter(self, fixture_square):
        assert 20 == fixture_square.get_perimeter()

    def test_add_area(self, fixture_square, fixture_rectangle):
        assert 26 == fixture_square.add_area(fixture_rectangle)


class TestCircle:
    def test_get_name(self, fixture_circle):
        assert "Circle" == fixture_circle.name

    def test_get_area(self, fixture_circle):
        assert 78.5 == fixture_circle.get_area()

    def test_get_angles(self, fixture_circle):
        assert 0 == fixture_circle.get_angles()

    def test_get_perimeter(self, fixture_circle):
        assert 31.4 == fixture_circle.get_perimeter()

    def test_add_area(self, fixture_circle, fixture_rectangle):
        assert 37.4 == fixture_circle.add_area(fixture_rectangle)
