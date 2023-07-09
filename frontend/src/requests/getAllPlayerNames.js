import { PLAYERNAMESREQUEST } from "./constants";

export async function GetAllPlayerNames() {
  try {
    const response = await fetch(PLAYERNAMESREQUEST);
    const data = await response.json();
    const arr = Array.from(data)
    return arr;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}
export default GetAllPlayerNames;
