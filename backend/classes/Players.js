const Player = require('./Player');

class Players {
    constructor() {
        this.players = new Map();
    }
  
    /* Check if player exists, return player */
    checkPlayer(playerName) {
        const playerLowerCase = playerName.toLowerCase();
        const player = this.players.get(playerLowerCase);
        return { found: !!player, player: player };
    }

    /* edit map of players */
    addPlayer(player) {
        if(!(player instanceof Player)){
            throw new Error(`Invalid argument. Expected Player object.`);
        }
        
        const results = this.checkPlayer(player.name);
        if (results.found){
            throw new Error(`Player ${player.name} already exists!`)
        }

        this.players.set(player.name.toLowerCase(), player);
        this.players.forEach(existingPlayer => {
            if (existingPlayer.name !== player.name) {
                existingPlayer.addOpponent(player.name);
                player.addOpponent(existingPlayer.name);
            }
        });   
    }

    removePlayer(player){
        const results = this.checkPlayer(player);
        if (!results.found) {
            throw new Error(`Player ${player} not found!`);
        }

        const playerToRemove = results.player;
        this.players.delete(playerToRemove.name.toLowerCase());

        this.players.forEach(existingPlayer => {
            existingPlayer.removeOpponent(player);
        });
    }
  
    /* Getters & Setters */
    getPlayerByName(player) {
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player;
        }
    }

    getScoresByName(player) {
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player.getScores;
        }
    }

    getTotalWinsByName(player) {
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player.getTotalWins;
        }
    }

    getTotalLossesByName(player) {
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player.getTotalLosses;
        }
    }

    getWinRateByName(player) {
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player.getWinRate;
        }
    }

    getTotalSetsByName(){
        const results = this.checkPlayer(player);
        if (!results.found){
            throw new Error(`Player not found!`)
        } else {
            return results.player.getTotalSets;
        }
    }

    get getHighestScorer() {
        var highScore = 0;
        var highestPlayer = '';

        for (const player of this.players.values()) {
            const totalWins = player.totalWins;
            if (totalWins > highScore) {
                highScore = totalWins;
                highestPlayer = player.getName;
            }
        }

        if (highestPlayer === ''){
            return null;
        } else {
            return [highScore, highestPlayer]
        }
    }

    addPointandMarkLoss(winner, loser) {
        const winnerResult = this.checkPlayer(winner);
        const loserResult = this.checkPlayer(loser);

        if (winnerResult.found && loserResult.found) {
            const winningPlayer = winnerResult.player;
            const losingPlayer = loserResult.player;

            if (winningPlayer && losingPlayer && winningPlayer.scores && losingPlayer.scores){
                winningPlayer.totalSets++;
                winningPlayer.totalWins++

                losingPlayer.totalSets++;
                losingPlayer.totalLosses++;
            
                if (winningPlayer.scores[loser] && losingPlayer.scores[winner]) {
                    winningPlayer.scores[loser][0]++;
                    losingPlayer.scores[winner][1]++;
                } else {
                    throw new Error (`scores object not properly defined for one or more players!`)
                }
            } else {
                throw new Error (`one or more players do not exist or scores object not properly defined!`);
            }
        } else {
            throw new Error(`one or more players do not exist!`)
        }
    }


   /* Convert to and from JSON strings */
    toJson() {
      return JSON.stringify(Array.from(this.players));
    }
  
    static fromJson(json) {
        const data = JSON.parse(json);
        const playersMap = new Map(data);
        const players = new Players();
        players.players = playersMap;
        return players;
  }
}

module.exports = Players;





/* 
const playersData = require('./data.json');
const players = Players.fromJson(JSON.stringify(playersData));

console.log(players);
//const bestPlayer = players.getHighestScorer();

//
console.log(bestPlayer) */
