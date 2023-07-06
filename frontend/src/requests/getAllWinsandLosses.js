import React from "react";

const URL = 'https://22lcozxsiolmtepmnlrezcfrf40pnqys.lambda-url.us-east-1.on.aws/'

export async function GetAllWinsandLosses() {
  try {
    const response = await fetch(URL);
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