// src/components/Counter.jsx
import React, { useReducer } from 'react';
import { reducer, INCREMENT, DECREMENT, RESET } from '../reducers/reducer';

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div style={{ textAlign: 'center', marginTop: '3rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>Counter: {state.count}</h1>
      <button onClick={() => dispatch({ type: DECREMENT })} style={{ marginRight: 10 }}>
        -
      </button>
      <button onClick={() => dispatch({ type: RESET })} style={{ marginRight: 10 }}>
        Reset
      </button>
      <button onClick={() => dispatch({ type: INCREMENT })}>+</button>
    </div>
  );
};

export default Counter;
