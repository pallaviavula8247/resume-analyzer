import { useNavigate } from "react-router-dom";
import {
  FaUpload,
  FaChartBar,
  FaFilePdf,
  FaHistory
} from "react-icons/fa";

import "../../assets/styles/QuickActions.css";


const QuickActions = () => {

  const navigate = useNavigate();


  const actions = [
    {
      title: "Upload Resume",
      icon: <FaUpload />,
      path: "/upload-resume",
      className: ""
    },
    {
      title: "Resume Analysis",
      icon: <FaChartBar />,
      path: "/analysis",
      className: ""
    },
    {
      title: "Reports",
      icon: <FaHistory />,
      path: "/reports",
      className: ""
    },
    {
      title: "Download PDF",
      icon: <FaFilePdf />,
      path: "/reports",
      className: "primary"
    }
  ];


  return (
    <div className="quick-actions-container">

      <h2 className="quick-actions-title">
        Quick Actions
      </h2>


      <div className="quick-actions-grid">

        {actions.map((action, index) => (

          <div
            key={index}
            className={`quick-action-card ${action.className}`}
            onClick={() => navigate(action.path)}
          >

            <div className="quick-action-icon">
              {action.icon}
            </div>


            <h3>
              {action.title}
            </h3>


          </div>

        ))}

      </div>

    </div>
  );
};


export default QuickActions;