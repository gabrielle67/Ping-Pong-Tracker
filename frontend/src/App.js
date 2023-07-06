import React from 'react';
import Navigation from './components/nav/Navigation';
import GetHighestScorer from './requests/getHighestScorer';
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
    </div>
  );
}

export default App;
