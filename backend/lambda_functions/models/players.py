import sys
import ast
import logging
sys.path.append('./lambda_functions')
from player import Player # noqa E402
from constants import ( # noqa E402
    COL_NAME,
    COL_SCORES,
    COL_WINS,
    COL_SETS,
    COL_LOSS
)
from storage import ( # noqa E402
    find_row,
    get_column,
    set_cell,
    remove_row,
    get_row,
    add_row
)


logger = logging.getLogger('Players')

class Players:
    def __init__(self, sheet):
        self.sheet = sheet

    def rowToPlayer(self, data):
        """
        converts the sheet row list to a player object
        """
        player = Player(data[0])
        player.totalSets = int(data[1])
        player.totalWins = int(data[2])
        player.totalLosses = int(data[3])

        scoresDict = ast.literal_eval(data[4])
        player.scores = scoresDict

        return player

    def playerToRow(self, player):
        """
        converts player object to sheets row list
        """
        data = [
            player.getName(),
            player.getTotalSets(),
            player.getTotalWins(),
            player.getTotalLosses(),
            str(player.getScores())
        ]

        return data

    def createPlayer(self, playerName):

        col = get_column(self.sheet, COL_NAME)[1:]

        player = Player(playerName.lower())
        player.totalSets = 0
        player.totalWins = 0
        player.totalLosses = 0

        for name in col:
            player.addOpponent(name)
        return player

    def checkPlayer(self, playerName):
        """
        check if player exists, return player
        """
        row = find_row(self.sheet, playerName.lower())
        if row is not None:
            data = get_row(self.sheet, row)
            return self.rowToPlayer(data)
        else:
            return None

    def addPlayer(self, playerName):
        """
        add new player object to sheets
        """
        if self.checkPlayer(playerName) is None:
            logger.info('creating new player...')
            player = self.createPlayer(playerName)
            col = get_column(self.sheet, COL_SCORES)[1:]

            logger.info('creating new scores list for other players')
            scores_list = []
            for scores in col:
                score = ast.literal_eval(scores)
                score[playerName.lower()] = [0, 0]
                scores_list.append(str(score))

            logger.info('putting new scores in spreadsheet...')
            row = 2
            for i in scores_list:
                set_cell(self.sheet, row, COL_SCORES, i)
                row += 1

            logger.info('adding new player to spreadsheet...')
            data = self.playerToRow(player)
            add_row(self.sheet, data)
        else:
            raise ValueError("Player already exists")

    def removePlayer(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            row = find_row(self.sheet, playerName)
            remove_row(self.sheet, row)

            col = get_column(self.sheet, COL_SCORES)[1:]
            scores_list = []
            for scores in col:
                score = ast.literal_eval(scores)
                del score[playerName]
                scores_list.append(str(score))

            row = 2
            for i in scores_list:
                set_cell(self.sheet, row, COL_SCORES, i)
                row += 1
        else:
            raise ValueError("Player does not exist")

    def getPlayerByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player
        else:
            raise ValueError("Player does not exist")

    def getScoresByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player.getScores()
        else:
            raise ValueError("Player does not exist")

    def getTotalWinsByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player.getTotalWins()
        else:
            raise ValueError("Player does not exist")

    def getTotalLossesByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player.getTotalLosses()
        else:
            raise ValueError("Player does not exist")

    def getWinRateByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player.getWinRate()
        else:
            raise ValueError("Player does not exist")

    def getTotalSetsByName(self, playerName):
        player = self.checkPlayer(playerName)
        if player is not None:
            return player.getTotalSets()
        else:
            raise ValueError("Player does not exist")

    def getHighestScorer(self):
        names = get_column(self.sheet, COL_NAME)[1:]
        wins = get_column(self.sheet, COL_WINS)[1:]

        ind = wins.index(max(wins))
        return names[ind]

    def addPointandMarkLoss(self, winner, loser):
        winnerResult = self.checkPlayer(winner)
        loserResult = self.checkPlayer(loser)

        if (winnerResult is not None) and (loserResult is not None):
            winnerRow = find_row(self.sheet, winner.lower())
            loserRow = find_row(self.sheet, loser.lower())

            winnerResult.addScore(loser.lower(), [1, 0])
            loserResult.addScore(winner.lower(), [0, 1])

            set_cell(self.sheet, winnerRow, COL_SETS, winnerResult.totalSets)
            set_cell(self.sheet, winnerRow, COL_WINS, winnerResult.totalWins)
            set_cell(self.sheet, winnerRow, COL_SCORES, str(winnerResult.getScores()))

            set_cell(self.sheet, loserRow, COL_SETS, loserResult.totalSets)
            set_cell(self.sheet, loserRow, COL_LOSS, loserResult.totalLosses)
            set_cell(self.sheet, loserRow, COL_SCORES, str(loserResult.getScores()))

        else:
            raise ValueError("One or more players not found")
