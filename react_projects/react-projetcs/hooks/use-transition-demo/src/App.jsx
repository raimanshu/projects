import React, { useState, useTransition, useMemo } from 'react';

// Generate a large list of items
const bigList = Array.from({ length: 20000 }, (_, i) => `Item ${i + 1}`);

const App = () => {
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('');
  const [isPending, startTransition] = useTransition();

  // Handle input change with transition
  const handleChange = (e) => {
    const value = e.target.value;
    setInput(value);

    // Mark filtering as a transition
    startTransition(() => {
      setFilter(value);
    });
  };

  // Filter list memoized for performance
  const filteredList = useMemo(() => {
    if (!filter) return bigList;
    return bigList.filter((item) => item.toLowerCase().includes(filter.toLowerCase()));
  }, [filter]);

  return (
    <div style={{ padding: 20, fontFamily: 'Arial, sans-serif' }}>
      <h1>useTransition Demo: Filter Large List</h1>
      <input
        type="text"
        value={input}
        onChange={handleChange}
        placeholder="Type to filter"
        style={{ padding: '8px', width: '300px', fontSize: '16px' }}
      />
      {isPending && <p style={{ color: 'red' }}>Loading...</p>}
      <ul style={{ maxHeight: 300, overflowY: 'auto' }}>
        {filteredList.slice(0, 100).map((item) => (
          <li key={item}>{item}</li> // Show only first 100 for performance
        ))}
      </ul>
    </div>
  );
};

export default App;
