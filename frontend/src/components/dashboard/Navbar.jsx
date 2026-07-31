import { NavLink, useNavigate } from "react-router-dom";
import "../styles/Navbar.css";

function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");

    navigate("/login");
  };

  return (
    <nav className="navbar">

      {/* Logo */}
      <div className="logo">
        📄 Resume Analyzer
      </div>

      {/* Navigation Links */}
      <div className="nav-links">

        <NavLink to="/" className="nav-item">
          Home
        </NavLink>

        <NavLink to="/dashboard" className="nav-item">
          Dashboard
        </NavLink>

        <NavLink to="/upload" className="nav-item">
          Upload Resume
        </NavLink>

        <NavLink to="/analysis" className="nav-item">
          Analysis
        </NavLink>

        <NavLink to="/job-match" className="nav-item">
          Job Match
        </NavLink>

        <NavLink to="/recommendations" className="nav-item">
          Recommendations
        </NavLink>

        <NavLink to="/reports" className="nav-item">
          Reports
        </NavLink>

        <NavLink to="/profile" className="nav-item">
          Profile
        </NavLink>

      </div>

      {/* Logout */}
      <button className="logout-btn" onClick={handleLogout}>
        Logout
      </button>

    </nav>
  );
}

export default Navbar;