import React, { useEffect, useState } from 'react';

const URL = 'https://t7pe7hs2o4liq4pqmpdkpqskj40edaym.lambda-url.us-east-1.on.aws/'

function GetHighestScorer() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(URL);
        const textData = await response.text();
        setData(textData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {data}
    </div>
  );
}

export default GetHighestScorer;
