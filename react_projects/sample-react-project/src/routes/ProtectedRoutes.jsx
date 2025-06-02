// ProtectedRoute.jsx
import React from "react";
import { Navigate } from "react-router-dom";
import { AUTH_ROUTES } from "../constants/AuthenticationConstants";

const ProtectedRoute = ({ children }) => {
  const userLoggedIn = Boolean(localStorage.getItem("userLoggedIn"));
  console.log(userLoggedIn);

  return userLoggedIn ? children : <Navigate to={AUTH_ROUTES.login} replace />;
};

export default ProtectedRoute;
