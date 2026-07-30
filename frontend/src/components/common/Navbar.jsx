import { Link } from "react-router-dom";
import "../../assets/styles/navbar.css";


const Navbar = () => {

  return (

    <nav className="navbar">

      <h2>
        AI Resume Analyzer
      </h2>


      <div className="nav-links">

        <Link to="/">
          Home
        </Link>

        <Link to="/upload">
          Upload
        </Link>

        <Link to="/dashboard">
          Dashboard
        </Link>

        <Link to="/reports">
          Reports
        </Link>

        <Link to="/login">
          Login
        </Link>

      </div>


    </nav>

  );
};


export default Navbar;