import "./DashboardCard.css";

function DashboardCard({ title, value, icon, color = "#7C3AED" }) {
  return (
    <div className="dashboard-card">

      <div className="card-top">

        <div
          className="card-icon"
          style={{ backgroundColor: color }}
        >
          {icon}
        </div>

        <div>
          <h3>{title}</h3>
          <h2>{value}</h2>
        </div>

      </div>

    </div>
  );
}

export default DashboardCard;