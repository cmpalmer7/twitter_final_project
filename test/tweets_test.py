
from app.tweets import to_percent

def test_to_percent():

    assert to_percent(10,20) == "50%"

    assert to_percent(3,4) == "75%"

    assert to_percent(5,6) == "83%"
