class Player:
    def __init__(self, name):
        self.name = name
        self.scores = {}
        self.totalSets = 0
        self.totalWins = 0
        self.totalLosses = 0

    # Validators
    def checkOpponent(self, opponent):
        """
        Validates that the opponent is not null
        """
        return opponent is not None and opponent != ''

    def checkOpponentExists(self, opponent):
        """
        Validates that the opponent exists in Player scores
        """
        if self.checkOpponent(opponent):
            return opponent in self.scores
        raise ValueError("Opponent cannot be empty or None")

    def checkScore(self, score):
        """
        Validates that the score is a positive int
        """
        wins = score[0]
        losses = score[1]
        return (wins >= 0 and losses >= 0)

    # getters and setters
    def getName(self):
        return self.name

    def getTotalWins(self):
        return self.totalWins

    def getTotalLosses(self):
        return self.totalLosses

    def getScores(self):
        return self.scores

    def getTotalSets(self):
        return self.totalSets

    def getWinRate(self):
        if (self.totalSets == 0):
            return 0
        return round(((self.totalWins / self.totalSets) * 100))

    def getScoreOpponent(self, opponent):
        if self.checkOpponentExists(opponent):
            return self.scores[opponent]
        raise ValueError("Opponent must exist in Player scores")

    def setName(self, name):
        self.name = name

    def setScores(self, scores):
        self.scores = scores

    def addOpponent(self, opponent):
        if not self.checkOpponentExists(opponent):
            self.scores[opponent] = [0, 0]
        else:
            raise ValueError("Opponent cannot already exist in Player scores")

    def removeOpponent(self, opponent):
        if self.checkOpponentExists(opponent):
            del self.scores[opponent]
        else:
            raise ValueError("Opponent must exist in Player scores")

    def addScore(self, opponent, score):
        if not self.checkScore(score):
            raise ValueError("Score must be positive integer")
        else:
            wins = score[0]
            losses = score[1]

            self.scores[opponent][0] += wins
            self.scores[opponent][1] += losses
            self.totalSets += wins + losses

            self.totalWins += wins
            self.totalLosses += losses
