import sys

sys.path.append('./utils')
sys.path.append('./models')
from constants import SHEET # noqa E402
from players import Players # noqa E402


def lambda_handler(event, context):
    players = Players(SHEET)
    highestScorer = players.getHighestScorer()
    return highestScorer
