"""import pytest
from unittest.mock import MagicMock, patch
from ..lambda_functions.storage import *

from ..lambda_functions.models.players import Players

DUMMY_SCORES = [{ 'Dave': [0, 0] }, { 'Bob': [0, 0] }]
PLAYER_ALICE = 'Alice'


# Mock the sheet object for testing
"""

"""
@pytest.fixture
def players():
    return Players(sheet_mock)
"""
"""
@patch('find_row')
@patch('storage.set_cell')
@patch('storage.add_row')
@patch('storage.get_column')
@patch('storage.get_row')
def test_addPlayer(mock_find_row,
                    mock_set_cell,
                    mock_add_row,
                    mock_get_column,
                    mock_get_row):
    mock_find_row.return_value = None
    mock_get_column.return_value = DUMMY_SCORES
    mock_get_row.return_value = DUMMY_SCORES
    players = Players('sheet')
    # Test adding a new player
    players.addPlayer(PLAYER_ALICE)

    # Verify that the player was added to the sheet
    assert players.checkPlayer(PLAYER_ALICE) is not None

"""
"""

def test_removePlayer():
    players = Players(sheet_mock)
    player_name = "Bob"

    # Add a player for testing
    players.addPlayer(player_name)

    # Test removing an existing player
    players.removePlayer(player_name)

    # Verify that the player was removed from the sheet
    assert players.checkPlayer(player_name) is None

def test_getPlayerByName():
    players = Players(sheet_mock)
    player_name = "Charlie"

    # Add a player for testing
    players.addPlayer(player_name)

    # Test retrieving an existing player
    player = players.getPlayerByName(player_name)

    # Verify that the retrieved player matches the added player
    assert player.getName() == player_name

def test_getScoresByName():
    players = Players(sheet_mock)
    player_name = "David"

    # Add a player for testing
    players.addPlayer(player_name)

    # Test retrieving scores for an existing player
    scores = players.getScoresByName(player_name)

    # Verify that the scores dictionary is not empty
    assert len(scores) > 0

# Add more tests for other methods as needed

"""
