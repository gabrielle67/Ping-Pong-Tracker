import React, { useEffect, useState } from 'react';
import { HIGHESTSCORERREQUEST } from './constants';

function GetHighestScorer() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(HIGHESTSCORERREQUEST);
        const textData = await response.text();
        setData(textData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  if (!data) {
    return <div>loading champion...</div>;
  }

  return (
    <div>
      {data}
    </div>
  );
}

export default GetHighestScorer;
