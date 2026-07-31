import { NavLink } from "react-router-dom";

import {
  FaHome,
  FaUpload,
  FaChartBar,
  FaBriefcase,
  FaLightbulb,
  FaFilePdf,
  FaUser,
} from "react-icons/fa";

import "../assets/styles/Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">

      <NavLink to="/dashboard">
        <FaHome />
        <span>Dashboard</span>
      </NavLink>

      <NavLink to="/upload">
        <FaUpload />
        <span>Upload Resume</span>
      </NavLink>

      <NavLink to="/analysis">
        <FaChartBar />
        <span>Analysis</span>
      </NavLink>

      <NavLink to="/job-match">
        <FaBriefcase />
        <span>Job Match</span>
      </NavLink>

      <NavLink to="/recommendations">
        <FaLightbulb />
        <span>Recommendations</span>
      </NavLink>

      <NavLink to="/reports">
        <FaFilePdf />
        <span>Reports</span>
      </NavLink>

      <NavLink to="/profile">
        <FaUser />
        <span>Profile</span>
      </NavLink>

    </aside>
  );
}

export default Sidebar;