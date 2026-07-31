import { useNavigate } from "react-router-dom";

function QuickActions() {

  const navigate = useNavigate();

  return (

    <div className="dashboard-card">

      <h2>Quick Actions</h2>

      <button onClick={() => navigate("/upload")}>
        Upload Resume
      </button>

      <button onClick={() => navigate("/analysis")}>
        Analyze Resume
      </button>

      <button onClick={() => navigate("/reports")}>
        View Reports
      </button>

    </div>

  );

}

export default QuickActions;