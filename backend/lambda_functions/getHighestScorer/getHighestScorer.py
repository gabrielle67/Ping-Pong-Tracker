import sys

sys.path.append('./utils')
sys.path.append('./models')
#from constants import SHEET # noqa E402
from player import Player # noqa E402


def lambda_handler(event, context):
    player = Player('Sally')
    return player.getName()
