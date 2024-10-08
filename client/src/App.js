import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [agents, setAgents] = useState([]);
  const [selectedAgent, setSelectedAgent] = useState('');
  const [statusMessage, setStatusMessage] = useState('');

  // Fetch the agent list from the Flask backend on component mount
  useEffect(() => {
    const fetchAgents = async () => {
      try {
        const response = await axios.get('http://localhost:5000/'); // Adjust the URL based on your Flask server
        setAgents(response.data.agents);
      } catch (error) {
        console.error('Error fetching agents:', error);
      }
    };

    fetchAgents();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/select_agent', {
        agent: selectedAgent,
      });
      setStatusMessage(response.data.message);
    } catch (error) {
      console.error('Error selecting agent:', error);
      setStatusMessage('Error selecting agent');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Valorant Agent Instalock</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="agent">Select an agent:</label>
        <select
          id="agent"
          value={selectedAgent}
          onChange={(e) => setSelectedAgent(e.target.value)}
        >
          <option value="" disabled>Select an agent</option>
          {agents.map((agent) => (
            <option key={agent} value={agent}>
              {agent}
            </option>
          ))}
        </select>
        <button type="submit">Instalock</button>
      </form>
      {statusMessage && <p>{statusMessage}</p>}
    </div>
  );
}

export default App;
