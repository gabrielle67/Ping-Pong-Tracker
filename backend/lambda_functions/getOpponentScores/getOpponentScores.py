import sys

sys.path.append('./utils')
sys.path.append('./models')
from utils.constants import SHEET # noqa E402
from models.players import Players # noqa E402


def lambda_handler(event, context):
    players = Players(SHEET)
    player = event["queryStringParameters"].get("name")
    opponent = event["queryStringParameters"].get("opp")
    score = players.getPlayerByName(player).getScoreOpponent(opponent)
    return score
