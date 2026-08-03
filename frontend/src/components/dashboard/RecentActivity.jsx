import {
  FaUpload,
  FaRobot,
  FaBriefcase,
  FaFilePdf,
  FaHistory,
} from "react-icons/fa";

function RecentActivity({ activities = [] }) {

  const getIcon = (type) => {

    switch (type) {

      case "upload":
        return <FaUpload color="#2563EB" />;

      case "analysis":
        return <FaRobot color="#7C3AED" />;

      case "job":
        return <FaBriefcase color="#16A34A" />;

      case "report":
        return <FaFilePdf color="#DC2626" />;

      default:
        return <FaHistory color="#6B7280" />;

    }

  };

  return (

    <div className="dashboard-card">

      <h2>Recent Activity</h2>

      {activities.length === 0 ? (

        <div
          style={{
            padding: "30px",
            textAlign: "center",
            color: "#6B7280",
          }}
        >

          <FaHistory
            size={40}
            style={{
              marginBottom: "10px",
            }}
          />

          <p>No recent activity found.</p>

        </div>

      ) : (

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "15px",
            marginTop: "15px",
          }}
        >

          {activities.map((activity, index) => (

            <div
              key={index}
              style={{
                display: "flex",
                gap: "15px",
                alignItems: "flex-start",
                borderBottom: "1px solid #E5E7EB",
                paddingBottom: "15px",
              }}
            >

              <div
                style={{
                  fontSize: "22px",
                  marginTop: "3px",
                }}
              >
                {getIcon(activity.type)}
              </div>

              <div
                style={{
                  flex: 1,
                }}
              >

                <h4
                  style={{
                    margin: 0,
                    fontSize: "16px",
                  }}
                >
                  {activity.title}
                </h4>

                <p
                  style={{
                    margin: "6px 0",
                    color: "#6B7280",
                    fontSize: "14px",
                  }}
                >
                  {activity.description}
                </p>

                <small
                  style={{
                    color: "#9CA3AF",
                  }}
                >
                  {new Date(activity.time).toLocaleString()}
                </small>

              </div>

            </div>

          ))}

        </div>

      )}

    </div>

  );

}

export default RecentActivity;