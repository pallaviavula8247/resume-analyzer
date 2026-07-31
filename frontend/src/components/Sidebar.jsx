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
        <FaHome /> Dashboard
      </NavLink>

      <NavLink to="/upload">
        <FaUpload /> Upload Resume
      </NavLink>

      <NavLink to="/analysis">
        <FaChartBar /> Resume Analysis
      </NavLink>

      <NavLink to="/job-match">
        <FaBriefcase /> Job Match
      </NavLink>

      <NavLink to="/recommendations">
        <FaLightbulb /> Recommendations
      </NavLink>

      <NavLink to="/reports">
        <FaFilePdf /> Reports
      </NavLink>

      <NavLink to="/profile">
        <FaUser /> Profile
      </NavLink>

    </aside>
  );
}

export default Sidebar;