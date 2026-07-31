import { FaBell, FaUserCircle } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

import "../assets/styles/Navbar.css";

function Navbar() {
  const navigate = useNavigate();

  const user = JSON.parse(localStorage.getItem("user"));

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");

    navigate("/login");
  };

  return (
    <header className="navbar">

      <div className="navbar-logo">
        📄 Resume Analyzer
      </div>

      <div className="navbar-right">

        <FaBell className="navbar-icon" />

        <div className="navbar-user">
          <FaUserCircle className="user-icon" />
          <span>{user?.full_name || "User"}</span>
        </div>

        <button
          className="logout-btn"
          onClick={handleLogout}
        >
          Logout
        </button>

      </div>

    </header>
  );
}

export default Navbar;