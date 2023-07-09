import React, { useState, useEffect } from 'react';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import GetAllPlayerNames from '../requests/getAllPlayerNames';
import GetOpponentScores from '../requests/getOpponentScores';
import { DoughnutChart } from './charts/doughnut';

export function PlayerDropdowns({ onSelectPlayer1, onSelectPlayer2 }) {
    const [listData, setListData] = useState([]);
    const [selectedPlayer1, setSelectedPlayer1] = useState('');
    const [selectedPlayer2, setSelectedPlayer2] = useState('');
    const [playerScores, setPlayerScores] = useState([]);
    const [chartData, setChartData] = useState(null);

    useEffect(() => {
      const fetchData = async () => {
        try {
            const data = await GetAllPlayerNames();
            setListData(data);
            if (listData != null){
                setSelectedPlayer1(data[0]);
                setSelectedPlayer2(data[1]);
            } else {
              <load className='loading-chart'>
              <h3>
                loading names...
              </h3>
              </load>;
            }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
  
      fetchData();
    },[]);   

    useEffect(() => {
        async function updateChart() {
          try {
                console.log(selectedPlayer1)
                const scores = await GetOpponentScores(selectedPlayer1, selectedPlayer2);
                setPlayerScores(scores);
                setChartData({
                    labels: [selectedPlayer1, selectedPlayer2],
                    data: scores
                });
            } catch (error) {
              console.error('Error fetching opponent scores:', error);
            }
          }
    
        updateChart();
      }, [selectedPlayer1, selectedPlayer2]);

      const handlePlayer1Change = (option) => {
        setSelectedPlayer1(option.value);
      };
    
      const handlePlayer2Change = (option) => {
        setSelectedPlayer2(option.value);
      };

    const defaultOption1 = listData[0];
    const defaultOption2 = listData[1];
    console.log(chartData)

    return (
      <div>
        <div className="opponent-container">
          <div className="doughnut-chart">
            {chartData !== null && (
              <>
                {chartData.data && chartData.data[0] === 0 && chartData.data[1] === 0 ? (
                  <load className="loading-chart">
                    <h3>You're tied! ...at 0 points. Play a round!</h3>
                  </load>
                ) : (
                  <>
                    {chartData.labels && chartData.labels[0] === chartData.labels[1] ? (
                      <load className="loading-chart">
                        <h3>Identical names picked.</h3>
                      </load>
                    ) : (
                      <DoughnutChart labels={chartData.labels} input={chartData.data} />
                    )}
                  </>
                )}
              </>
            )}
          </div>
          <h3 className="dropdown-directions">Select 2 players to view their overall score!</h3>
          <div className="dropdown-container">
            <Dropdown options={listData} onChange={handlePlayer1Change} value={defaultOption1} />
            <Dropdown options={listData} onChange={handlePlayer2Change} value={defaultOption2} />
          </div>
        </div>
      </div>
    );
}    