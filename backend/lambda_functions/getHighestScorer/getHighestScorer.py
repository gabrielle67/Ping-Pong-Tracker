from models.players import Players
from utils.constants import SHEET


def lambda_handler(event, context):
    players = Players(SHEET)
    highestScorer = players.getHighestScorer()
    return highestScorer
