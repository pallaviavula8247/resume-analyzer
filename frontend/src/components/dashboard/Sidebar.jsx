import {
  FaHome,
  FaUpload,
  FaChartLine,
  FaBriefcase,
  FaFileAlt,
  FaUser,
} from "react-icons/fa";

const Sidebar = () => {
  return (
    <aside className="sidebar">

      <h2 className="sidebar-title">
        Resume Analyzer
      </h2>

      <ul className="sidebar-menu">

        <li>
          <FaHome />
          <span>Dashboard</span>
        </li>

        <li>
          <FaUpload />
          <span>Upload Resume</span>
        </li>

        <li>
          <FaChartLine />
          <span>Resume Analysis</span>
        </li>

        <li>
          <FaBriefcase />
          <span>Job Recommendations</span>
        </li>

        <li>
          <FaFileAlt />
          <span>Reports</span>
        </li>

        <li>
          <FaUser />
          <span>Profile</span>
        </li>

      </ul>

    </aside>
  );
};

export default Sidebar;