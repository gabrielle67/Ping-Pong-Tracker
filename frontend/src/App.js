import React from 'react';
import Navigation from './components/nav/Navigation';
import GetHighestScorer from './requests/getHighestScorer';
import { DoughnutChart } from './components/charts/doughnut';
import HorizontalBarChart from './components/charts/horizontal_bar';

function App() {
  return (
    <div className= "app">
      <Navigation />
      <h2>
        Current Ping Pong Champion:
        <GetHighestScorer />
      </h2>
      <HorizontalBarChart />
      <DoughnutChart />
    </div>
  );
}

export default App;
