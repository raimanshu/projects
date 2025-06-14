import React, { useState, useMemo } from 'react';

// Simulate expensive calculation
function expensiveFactorial(n) {
  console.log('Calculating factorial...');
  let result = 1;
  for (let i = 2; i <= n; i++) {
    // Artificial delay
    for (let j = 0; j < 10000000; j++) {}
    result *= i;
  }
  return result;
}

const App = () => {
  const [number, setNumber] = useState(5);
  const [inc, setInc] = useState(0);

  // Memoize factorial result, only recalc if `number` changes
  const factorial = useMemo(() => expensiveFactorial(number), [number]);

  // Handler to safely parse number input
  const handleChange = (e) => {
    const val = e.target.value;
    // If empty string, set 0 or you can set '' based on your UI preference
    if (val === '') {
      setNumber(0);
      return;
    }
    const parsed = parseInt(val, 10);
    if (!isNaN(parsed)) {
      setNumber(parsed);
    }
  };

  return (
    <div style={{ fontFamily: 'Arial', padding: 20 }}>
      <h1>Factorial Calculator</h1>
      <input
        type="number"
        value={number}
        onChange={handleChange}
        style={{ padding: 5, fontSize: 18, width: 100 }}
        min={0}
      />
      <p>Factorial: {factorial}</p>

      <button onClick={() => setInc((i) => i + 1)}>Re-render</button>
      <p>Re-render count: {inc}</p>
    </div>
  );
};

export default App;
