import { useNavigate } from "react-router-dom";

function QuickActions({ onDownload }) {

  const navigate = useNavigate();

  return (

    <div className="dashboard-card">

      <h2>Quick Actions</h2>

      <div className="quick-actions-container">

        <button
          onClick={() => navigate("/upload")}
        >
          📤 Upload Resume
        </button>

        <button
          onClick={() => navigate("/analysis")}
        >
          🤖 Analyze Resume
        </button>

        <button
          onClick={() => navigate("/reports")}
        >
          📋 View Reports
        </button>

        <button
          onClick={onDownload}
        >
          📄 Download PDF Report
        </button>

      </div>

    </div>

  );

}

export default QuickActions;