import { Outlet } from "react-router-dom";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

import "../assets/styles/Layout.css";

function Layout() {
  return (
    <div className="layout">

      <Navbar />

      <div className="layout-body">

        <Sidebar />

        <main className="page-content">
          <Outlet />
        </main>

      </div>

    </div>
  );
}

export default Layout;