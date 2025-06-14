import React, { useState, useEffect, useLayoutEffect, useRef } from 'react';

const App = () => {
  const boxRefEffect = useRef(null);
  const boxRefLayout = useRef(null);

  const [effectStyle, setEffectStyle] = useState({});
  const [layoutStyle, setLayoutStyle] = useState({});

  // Updates style inside useEffect (after paint)
  useEffect(() => {
    if (boxRefEffect.current) {
      const width = boxRefEffect.current.getBoundingClientRect().width;
      setEffectStyle({
        backgroundColor: width > 150 ? 'lightcoral' : 'lightblue',
        width: width > 150 ? 300 : 100,
      });
    }
  }, []);

  // Updates style inside useLayoutEffect (before paint)
  useLayoutEffect(() => {
    if (boxRefLayout.current) {
      const width = boxRefLayout.current.getBoundingClientRect().width;
      setLayoutStyle({
        backgroundColor: width > 150 ? 'lightgreen' : 'lightyellow',
        width: width > 150 ? 300 : 100,
      });
    }
  }, []);

  return (
    <div style={{ fontFamily: 'Arial', padding: 20 }}>
      <h2>useEffect (may cause flicker)</h2>
      <div
        ref={boxRefEffect}
        style={{
          width: 500,
          height: 100,
          marginBottom: 30,
          transition: 'all 0.5s ease',
          ...effectStyle,
        }}
      >
        Box styled with useEffect
      </div>

      <h2>useLayoutEffect (no flicker)</h2>
      <div
        ref={boxRefLayout}
        style={{
          width: 500,
          height: 100,
          transition: 'all 0.5s ease',
          ...layoutStyle,
        }}
      >
        Box styled with useLayoutEffect
      </div>
    </div>
  );
};

export default App;
