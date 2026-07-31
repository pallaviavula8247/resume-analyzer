import "./DashboardCard.css";

function DashboardCard({ title, value, icon, color }) {
  return (
    <div className="dashboard-card">
      <div className="card-top">
        <div
          className="card-icon"
          style={{ backgroundColor: color }}
        >
          {icon}
        </div>

        <h3>{title}</h3>
      </div>

      <h2>{value}</h2>
    </div>
  );
}

export default DashboardCard;