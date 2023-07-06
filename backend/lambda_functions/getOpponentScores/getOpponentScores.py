import sys

sys.path.append('./utils')
sys.path.append('./models')
from utils.constants import SHEET # noqa E402
from models.players import Players # noqa E402


def lambda_handler(event, context):
    players = Players(SHEET)
    player = event.player
    opp = event.opp
    score = players.getPlayerByName(player).getScoreOpponent(opp)
    return score