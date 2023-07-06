import React from "react";
import { WINSLOSSESREQUEST } from "./constants";

export async function GetAllWinsandLosses() {
  try {
    const response = await fetch(WINSLOSSESREQUEST);
    const data = await response.json();
    const updatedData = data.map((item) => ({
      ...item,
      losses: -parseInt(item.losses),
      wins: parseInt(item.wins)
    }));
    console.trace()
    console.log(updatedData)
    return updatedData;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}
export default GetAllWinsandLosses;