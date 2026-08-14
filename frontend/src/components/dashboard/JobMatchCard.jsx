import "./DashboardCard.css";

function JobMatchCard({ jobMatches = [] }) {
  if (!jobMatches || jobMatches.length === 0) {
    return (
      <div className="dashboard-card">
        <div className="card-top">
          <div
            className="card-icon"
            style={{ background: "#10B981" }}
          >
            💼
          </div>

          <h3>Best Job Match</h3>
        </div>

        <div
          style={{
            textAlign: "center",
            padding: "30px",
            color: "#777",
          }}
        >
          No Job Matches Available
        </div>
      </div>
    );
  }

  const bestMatch = [...jobMatches].sort(
    (a, b) => b.match_score - a.match_score
  )[0];

  const score = bestMatch.match_score;

  let badgeColor = "#EF4444";
  let progressColor = "#EF4444";

  if (score >= 80) {
    badgeColor = "#22C55E";
    progressColor = "#22C55E";
  } else if (score >= 60) {
    badgeColor = "#F59E0B";
    progressColor = "#F59E0B";
  }

  return (
    <div className="dashboard-card">

      <div className="card-top">

        <div
          className="card-icon"
          style={{
            background: "#10B981",
          }}
        >
          💼
        </div>

        <h3>Best Job Match</h3>

      </div>

      <h2
        style={{
          marginTop: "10px",
          color: "#7C3AED",
          fontSize: "42px",
        }}
      >
        {score}%
      </h2>

      <h4
        style={{
          marginTop: "10px",
        }}
      >
        {bestMatch.job_title}
      </h4>

      <span
        style={{
          display: "inline-block",
          marginTop: "12px",
          padding: "6px 18px",
          borderRadius: "20px",
          background: badgeColor,
          color: "#fff",
          fontWeight: "bold",
        }}
      >
        {bestMatch.match_level}
      </span>

      <div
        style={{
          marginTop: "20px",
        }}
      >
        <div
          style={{
            width: "100%",
            background: "#E5E7EB",
            height: "12px",
            borderRadius: "20px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${score}%`,
              height: "100%",
              background: progressColor,
              transition: "0.5s",
            }}
          />
        </div>
      </div>

      <div
        style={{
          marginTop: "25px",
        }}
      >
        <strong>Matched Skills</strong>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "8px",
            marginTop: "12px",
          }}
        >
          {bestMatch.matched_skills?.map((skill, index) => (
            <span
              key={index}
              style={{
                background: "#EEF2FF",
                color: "#4338CA",
                padding: "6px 12px",
                borderRadius: "20px",
                fontSize: "13px",
              }}
            >
              {skill}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

export default JobMatchCard;