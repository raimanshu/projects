import React from "react";
import { Outlet } from "react-router-dom";

const UserLayout = ({ children }) => {
  console.log(children);
  return (
    <div style={{ border: "5px solid yellow" }}>

      <h1>User Layout</h1>
      <Outlet />
    </div>
  );
};

export default UserLayout;