import React, { useEffect, useState } from 'react';

const URL = ''

function GetAllWinsandLosses() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(URL);
        const jsonData = await response.json();
        setData(jsonData);
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

export default GetAllWinsandLosses;