const initialState = [
  { id: '1', text: 'Learn React', completed: false },
  { id: '2', text: 'Learn Redux', completed: false },
];

export default function todosReducer(state = initialState, action) {
  switch (action.type) {
    case 'ADD':
      return [...state, { id: Date.now().toString(), text: action.data.text, completed: false }];
    case 'DELETE':
      return state.filter(todo => todo.id !== action.data.id);
    case 'TOGGLE':
      return state.map(todo =>
        todo.id === action.data.id ? { ...todo, completed: !todo.completed } : todo
      );
    case 'RESET':
      return [];
    case 'INIT':
      return action.data.todos || [];
    default:
      return state;
  }
}
