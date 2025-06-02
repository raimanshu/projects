import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import { AUTH_ROUTES } from "./constants/AuthenticationConstants";
import { USER_ROUTES } from "./constants/UserConstants";

import Login from "./views/authentication/Login";
import AppLayout from "./layouts/AppLayout";
import AuthenticationRoutes from "./routes/AuthenticationRoutes";
import UserRoutes from "./routes/UserRoutes";
import UserLayout from "./layouts/UserLayout";
import ProtectedRoute from "./routes/ProtectedRoutes";
import PageNotFound from "./views/extras/PageNotFound";

function App() {
  // const userLoggedIn = Boolean(localStorage.getItem("userLoggedIn"));

  return (
    <BrowserRouter>
      <Routes>
        {/* Redirect root '/' to dashboard or login */}
        {/* <Route
          path="/"
          element={
            userLoggedIn ? (
              <Navigate to={USER_ROUTES.dashboard} replace />
            ) : (
              <Navigate to={AUTH_ROUTES.login} replace />
            )
          }
        /> */}

        {/* Public/Auth routes (login, register, etc.) */}
        {/* <Route element={userLoggedIn ? <Navigate to={USER_ROUTES.dashboard} replace /> : <AppLayout />}>
          {AuthenticationRoutes()}
        </Route> */}

        <Route element={<AppLayout />}>{AuthenticationRoutes()}</Route>

        {/* Protected routes */}
        <Route
          element={
            <ProtectedRoute>
              <UserLayout />
            </ProtectedRoute>
          }
        >
          {UserRoutes()}
        </Route>

        {/* 404 fallback */}
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
