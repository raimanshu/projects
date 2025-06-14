// src/reducer.js

// Action types
export const INCREMENT = 'increment';
export const DECREMENT = 'decrement';
export const RESET = 'reset';

// Reducer function
export function reducer(state, action) {
  switch (action.type) {
    case INCREMENT:
      return { count: state.count + 1 };
    case DECREMENT:
      return { count: state.count - 1 };
    case RESET:
      return { count: 0 };
    default:
      throw new Error('Unknown action');
  }
}
