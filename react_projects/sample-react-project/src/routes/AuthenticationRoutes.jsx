import { Navigate, Route, Router, Routes } from "react-router-dom";
import { AUTH_ROUTES } from "../constants/AuthenticationConstants";
import App from "../App";
import Login from "../views/authentication/Login";
import Register from "../views/authentication/Register";
import ForgetPassword from "../views/authentication/ForgetPassword";
import AppLayout from "../layouts/AppLayout";

const AuthenticationRoutes = () => {
  return (
    <>
      <Route path="/" element={<Navigate to={AUTH_ROUTES.login} replace />} />
      <Route index path={AUTH_ROUTES.login} element={<Login />} />
      <Route path={AUTH_ROUTES.register} element={<Register />} />
      <Route path={AUTH_ROUTES.forgotPassword} element={<ForgetPassword />} />
    </>
  );
};

export default AuthenticationRoutes;
