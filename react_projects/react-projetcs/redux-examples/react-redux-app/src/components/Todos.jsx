import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

const Todos = () => {
  const todos = useSelector((state) => state);
  const dispatch = useDispatch();
  const [input, setInput] = useState("");

  const addTodo = () => {
    const text = input.trim();
    if (text) {
      dispatch({ type: "ADD", data: { text } });
      setInput("");
    }
  };

  const initializeTodos = () => {
    const defaultTodos = [
      { id: "1", text: "Learn React", completed: false },
      { id: "2", text: "Learn Redux", completed: false },
    ];
    dispatch({ type: "INIT", data: { todos: defaultTodos } });
  };

  const deleteTodo = (id) => {
    dispatch({ type: "DELETE", data: { id } });
  };

  const toggleTodo = (id) => {
    dispatch({ type: "TOGGLE", data: { id } });
  };

  const resetTodos = () => {
    dispatch({ type: "RESET" });
  };

  return (
    <div className="container mt-5" style={{ maxWidth: 600 }}>
      <h2 className="mb-4">Simple Redux Todo</h2>

      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Enter new todo"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && addTodo()}
          aria-label="New todo"
        />
        <button className="btn btn-primary" onClick={addTodo} type="button">
          Add
        </button>
      </div>

      <div className="mb-3">
        <button
          className="btn btn-warning me-2"
          onClick={resetTodos}
          type="button"
        >
          Reset Todos
        </button>
        <button
          className="btn btn-info"
          onClick={initializeTodos}
          type="button"
        >
          Initialize Todos
        </button>
      </div>

      <button
        className="btn btn-warning mb-3"
        onClick={resetTodos}
        type="button"
      >
        Reset Todos
      </button>

      <ul className="list-group">
        {todos.map(({ id, text, completed }) => (
          <li
            key={id}
            className={`list-group-item d-flex justify-content-between align-items-center ${
              completed
                ? "list-group-item-secondary text-decoration-line-through"
                : ""
            }`}
          >
            <span
              role="button"
              tabIndex={0}
              onClick={() => toggleTodo(id)}
              onKeyDown={(e) => {
                if (e.key === "Enter" || e.key === " ") toggleTodo(id);
              }}
              style={{ cursor: "pointer" }}
              aria-label={`Toggle todo ${text}`}
            >
              {text}
            </span>
            <button
              className="btn btn-danger btn-sm"
              onClick={() => deleteTodo(id)}
              aria-label={`Delete todo ${text}`}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Todos;
