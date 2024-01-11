from src.change_me import ChangeMe


class TestChangeMe:

    def test_change_me(self):
        change_me = ChangeMe()

        assert change_me.my_method() == True
