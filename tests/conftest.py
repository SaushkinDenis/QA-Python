import pytest

from geometric_figure import Triangle, Rectangle, Square, Circle


@pytest.fixture
def fixture_triangle():
    return Triangle([3, 4, 5])


@pytest.fixture
def fixture_rectangle():
    return Rectangle([1, 2])


@pytest.fixture
def fixture_square():
    return Square(5)


@pytest.fixture
def fixture_circle():
    return Circle(5)
