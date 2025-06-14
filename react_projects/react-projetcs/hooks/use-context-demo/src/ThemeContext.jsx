// src/ThemeContext.jsx
import React, { createContext, useState } from "react";

// 1. Create the context with default value (optional)
export const ThemeContext = createContext();

// 2. Create a provider component
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState("light"); // state to toggle theme

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
