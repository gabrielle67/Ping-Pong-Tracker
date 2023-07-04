import React from 'react';
import Navigation from './components/nav/Navigation';
import GetHighestScorer from './components/requests/getHighestScorer';

function App() {
  return (
    <div className= "app">
      <Navigation />
      <h2>
        Current Ping Pong Champion:
        <GetHighestScorer />
      </h2> 
    </div>
  );
}

export default App;
