import sys

sys.path.append('./utils')
from constants import SHEET # noqa E402
from players import Players # noqa E402


def lambda_handler(name, opp):
    players = Players(SHEET)
    score = players.getPlayerByName(name).getScoreOpponent(opp)
    return score

print(lambda_handler('alice', 'dave'))