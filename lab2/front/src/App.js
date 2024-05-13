import './App.css';

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    async function fetchData() {
      const response = await axios.get('/api/data');
      setData(response.data.message);
    }
    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>{data}</h1>
    </div>
  );
}

export default App;
