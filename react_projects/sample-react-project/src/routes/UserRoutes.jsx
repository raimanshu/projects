import { Route, Router, Routes } from "react-router-dom";
import { USER_ROUTES } from "../constants/UserConstants";
import Dashboard from "../views/user/Dashboard";

const UserRoutes = () => {
  return (
    <>
      {/* <Route path="/" element={<AppLayout />} /> */}
      <Route index path={USER_ROUTES.dashboard} element={<Dashboard />} />
    </>
  );
};

export default UserRoutes;
