import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title } from 'chart.js';
import { doughnut_background } from './chart_plugins/background_color';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(
    ArcElement, 
    Tooltip, 
    Legend, 
    doughnut_background,
    Title,

);

export function DoughnutChart({ labels, input }) {
    const options = {
        plugins: {
            customCanvasBackgroundColor: {
                color: 'rgba(153, 255, 255, 0)'
            },
            title: {
                display: true,
                text: "Player vs Player scores:  " + labels[0] + " VS " + labels[1],
                color: 'white',
            },
            legend: {
                position: 'bottom',
                labels: {color: 'white'}
            }
        },
        maintainAspectRatio: false,
    }

    const data = {
        labels: labels,
        datasets: [
          {
            label: 'wins',
            data: input,
            backgroundColor:['pink', 'blue'],
            borderColor:['red'],
            borderWidth: 1,
          },
        ],
      };
      
  return (
    <Doughnut data={data} options={options}/>
  )
}
