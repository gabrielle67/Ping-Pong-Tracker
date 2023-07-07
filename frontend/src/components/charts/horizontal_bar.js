import React, { useEffect, useState }  from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { horizontal_bar_background } from './chart_plugins/background_color';
import GetAllWinsandLosses from '../../requests/getAllWinsandLosses'

ChartJS.register(
    horizontal_bar_background,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

export const options = {
    animation: {
        delay: (context) => {
          let delay = 0;
          if (context.type === 'data' && context.mode === 'default') {
            delay = context.dataIndex * 600 + context.datasetIndex * 200;
          }
          return delay;
        }
    },
    indexAxis: 'y',
    responsive: true,
    plugins: {
        legend: { 
          position: 'bottom',
          labels: { color: 'white'} },
        title: {
            display: true,
            text: "All Players' Wins and Losses",
            color: 'white'
        },
        customCanvasBackgroundColor: {
            color: 'rgba(153, 255, 255, 0)'
        },
    },
    scales: {
        y: { ticks: { color: 'white' } },
        x: { ticks: { color: 'white' } }
    },
    maintainAspectRatio: false,
};

export default function HorizontalBarChart() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await GetAllWinsandLosses();
        setChartData(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  if (!chartData) {
    return <load className='loading-chart'>
            <h3>
              loading chart...
            </h3>
            </load>;
  }

  const labels = chartData.map((item) => item.name);
  const dataset1Data = chartData.map((item) => item.wins);
  const dataset2Data = chartData.map((item) => item.losses);

  const data = {
    labels,
    datasets: [
      {
        label: 'WINS',
        data: dataset1Data,
        backgroundColor: '#E86850',
      },
      {
        label: 'LOSSES',
        data: dataset2Data,
        backgroundColor: '#FFD800',
      },
    ],
  };

  return (
    <horizontal-bar>
      <Bar options={options} data={data} />
    </horizontal-bar>
  );
}