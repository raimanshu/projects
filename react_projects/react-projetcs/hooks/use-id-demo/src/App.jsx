import React, { useId } from 'react';

const App = () => {
  const id = useId();

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: 20 }}>
      <label htmlFor={id} style={{ display: 'block', marginBottom: 8 }}>
        Your Name:
      </label>
      <input id={id} type="text" style={{ padding: 8, fontSize: 16, width: 250 }} />
    </div>
  );
};

export default App;
