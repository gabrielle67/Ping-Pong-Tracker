class Player {
    constructor(name) {
      this.name = name;
      this.scores = {};
      this.totalSets = 0;
      this.totalWins = 0;
      this.totalLosses = 0;
    }

    /* check for valid input */
    checkOpponent(opponent){
        return opponent !== null;
    }

    checkOpponentExists(opponent){
        /* returns true if opponent is not in scores*/
        return !this.scores.hasOwnProperty(opponent);
    }

    checkScore(score){
        const wins = score[0];
        const losses = score[1];

        return !(wins < 0 || losses < 0 || isNaN(wins) || isNaN(losses));
    }

    /* Getters & Setters */
    get getName(){
        return this.name;
    }

    get getTotalWins(){
        return this.totalWins;
    }

    get getTotalLosses(){
        return this.totalLosses;
    }

    get getScores(){
        return this.scores;
    }

    get getTotalSets(){
        return this.totalSets;
    }

    get getWinRate() {
        if (this.totalSets === 0) {
          return 0;
        }
        return ((this.totalWins / this.totalSets) * 100).toFixed(2);
    }

    getScoreOpponent(opponent){
        if (this.checkOpponent(opponent)) {
            return this.scores[opponent]
        } else {
            console.error(`getScoreOppoenent: Opponent does not exist`)
        }
    }
    
    set setName(name){
        this.name = name;
    }

    set setScores(scores){
        this.scores = scores;
    }


    updateScore(opponent, score){
        /* this is different from 'addScore'. Here, you are changing the
        total number of wins against an opponent. This should only be used
        to update accidental wins. */
        if (!this.checkOpponent(opponent)){
            throw new Error(`Opponent does not exist`)
        } else if(!this.checkScore(score)) {
            throw new Error(`Score must be a positive integer`)
        } else { 
            const wins = score[0];
            const losses = score[1];
            const totalGame = wins + losses;

            const oldScores = this.scores[opponent];
            const oldWins = oldScores[0];
            const oldLosses = oldScores[1];

            /*remove old scores from dataset*/
            this.totalSets -= oldWins + oldLosses;
            this.totalWins -= oldWins;
            this.totalLosses -= oldLosses;
            
            /*add new scores*/
            this.totalSets += totalGame;
            this.totalWins += wins;
            this.totalLosses += losses;
            this.scores[opponent] = score;
        }
    }

    addOpponent(opponent) {
        if (this.checkOpponent(opponent) && this.checkOpponentExists(opponent)){
            this.scores[opponent] = [0, 0];
        } else {
            throw new Error(`Opponent ${opponent} already exist in scores!`);
        }
    }

    removeOpponent(opponent){
        if (this.checkOpponent(opponent) && !this.checkOpponentExists(opponent)){
            delete this.scores[opponent];
        } else {
            throw new Error(`Opponent ${opponent} does not exist in scores!`);
        }
    }

    addScore(opponent, score) {
        if (!this.checkScore(score)){
            throw new Error(`checkScore: Score must be a positive integer`)
        } else{

            const wins = score[0];
            const losses = score[1];

            this.scores[opponent] = score;
            this.totalSets += wins + losses;

            if (wins > 0) {
            this.totalWins += wins;
            }
        }
    }
}

module.exports = Player;



