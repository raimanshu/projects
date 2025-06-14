import React, { useState, useCallback } from 'react';

const Button = React.memo(({ handleClick, children }) => {
  console.log(`Rendering button: ${children}`);
  return <button onClick={handleClick}>{children}</button>;
});

const App = () => {
  const [count, setCount] = useState(0);
  const [otherCount, setOtherCount] = useState(0);

  // Memoize increment function so Button only re-renders if count changes
  const increment = useCallback(() => {
    setCount((c) => c + 1);
  }, []);

  // Non-memoized callback for other count
  const incrementOther = () => {
    setOtherCount((c) => c + 1);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Count: {count}</h1>
      <Button handleClick={increment}>Increment Count</Button>

      <h1>Other Count: {otherCount}</h1>
      <Button handleClick={incrementOther}>Increment Other Count</Button>
    </div>
  );
};

export default App;
