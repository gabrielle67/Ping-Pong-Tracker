import pytest
from .models.player import Player


@pytest.fixture
def player():
    return Player("Alice")


def test_initialization(player):
    assert player.getName() == "Alice"
    assert player.getTotalWins() == 0
    assert player.getTotalLosses() == 0
    assert player.getScores() == {}
    assert player.getTotalSets() == 0


def test_add_opponent(player):
    player.addOpponent("Bob")
    assert "Bob" in player.getScores()
    assert player.getScores()["Bob"] == [0, 0]
    with pytest.raises(ValueError):
        player.addOpponent("Bob")


def test_remove_opponent(player):
    player.addOpponent("Bob")
    player.removeOpponent("Bob")
    assert "Bob" not in player.getScores()

    with pytest.raises(ValueError):
        player.removeOpponent("Bob")


def test_add_score(player):
    player.addOpponent("Bob")
    player.addScore("Bob", [2, 1])
    assert player.getScores()["Bob"] == [2, 1]
    assert player.getTotalSets() == 3
    assert player.getTotalWins() == 2
    assert player.getTotalLosses() == 1
    with pytest.raises(ValueError):
        player.addScore("Bob", [-1, 1])


def test_get_win_rate(player):
    assert player.getWinRate() == 0
    player.addOpponent("Bob")
    player.addScore("Bob", [5, 5])
    assert player.getWinRate() == 50


def test_get_score_opponent(player):
    player.addOpponent("Bob")
    player.addScore("Bob", [2, 1])
    assert player.getScoreOpponent("Bob") == [2, 1]

    with pytest.raises(ValueError):
        player.getScoreOpponent("Charlie")
