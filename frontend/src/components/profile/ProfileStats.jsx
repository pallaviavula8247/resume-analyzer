import {
  FaFileAlt,
  FaChartLine,
  FaTrophy,
  FaBriefcase,
  FaRobot,
} from "react-icons/fa";

function ProfileStats({ statistics }) {

  const stats = statistics?.statistics || {};

  const cards = [
    {
      title: "Uploaded Resumes",
      value: stats.total_resumes || 0,
      icon: <FaFileAlt />,
      color: "#3B82F6",
    },
    {
      title: "Average ATS Score",
      value: stats.average_ats_score || 0,
      icon: <FaChartLine />,
      color: "#10B981",
    },
    {
      title: "Highest ATS Score",
      value: stats.highest_ats_score || 0,
      icon: <FaTrophy />,
      color: "#F59E0B",
    },
    {
      title: "Job Matches",
      value: stats.total_job_matches || 0,
      icon: <FaBriefcase />,
      color: "#8B5CF6",
    },
    {
      title: "AI Recommendations",
      value: stats.total_recommendations || 0,
      icon: <FaRobot />,
      color: "#EF4444",
    },
  ];

  return (

    <div className="profile-stats">

      <h2>Resume Statistics</h2>

      <div className="profile-stats-grid">

        {cards.map((card, index) => (

          <div
            key={index}
            className="profile-stat-card"
          >

            <div
              className="profile-stat-icon"
              style={{
                backgroundColor: card.color,
              }}
            >
              {card.icon}
            </div>

            <div className="profile-stat-content">

              <h3>{card.value}</h3>

              <p>{card.title}</p>

            </div>

          </div>

        ))}

      </div>

    </div>

  );

}

export default ProfileStats;