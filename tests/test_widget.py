import pytest

from src.widget import get_data, mask_account_card


def test_dated(data):
    assert get_data(data) == "11.07.2018"


@pytest.fixture
def cards():
    return "Visa Platinum 7000 7922 8960 6361"


@pytest.fixture
def check():
    return "Счет 73654108430135874305"


@pytest.fixture
def data():
    return "2018-07-11T02:26:18.671407"


@pytest.mark.parametrize("string, expected_result", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result
