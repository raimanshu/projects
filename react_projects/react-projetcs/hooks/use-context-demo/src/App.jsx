// src/App.jsx
import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

const App = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);

  const appStyle = {
    height: '100vh',
    backgroundColor: theme === 'light' ? '#fff' : '#333',
    color: theme === 'light' ? '#333' : '#fff',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    fontFamily: 'Arial, sans-serif',
    transition: 'all 0.3s ease',
  };

  return (
    <div style={appStyle}>
      <h1>Current Theme: {theme}</h1>
      <button onClick={toggleTheme} style={{ padding: '10px 20px' }}>
        Toggle Theme
      </button>
    </div>
  );
};

export default App;
