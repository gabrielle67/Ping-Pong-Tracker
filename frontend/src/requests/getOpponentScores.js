import { OPPONENTSCORESREQUEST } from "./constants";

export async function GetOpponentScores(player1, player2) {
  try {
    const requestUrl = `${OPPONENTSCORESREQUEST}?name=${player1}&opp=${player2}`;
    console.log(requestUrl);
    const response = await fetch(requestUrl);
    const data = await response.json();
    const arr = Array.from(data)
    return arr;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}
export default GetOpponentScores;