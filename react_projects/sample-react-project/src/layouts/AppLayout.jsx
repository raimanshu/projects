import React from "react";
import { Outlet } from "react-router-dom";

const AppLayout = ({ children }) => {
  console.log(children);
  return (
    <div style={{ border: "5px solid red" }}>
      BrowserRouter vs HashRouter vs Router Tags <br />
      Router vs Routes vs Route Tags <br />
      react-router-dom vs react-router packages <br />
      <h1>App Layout</h1>
      <Outlet />
    </div>
  );
};

export default AppLayout;
