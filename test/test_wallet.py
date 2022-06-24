from src.wallet import Wallet, InsufficientAmount
import pytest


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    # crear el objeto sin argumentos
    assert empty_wallet.balance == 0


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(
        empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(20)


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
