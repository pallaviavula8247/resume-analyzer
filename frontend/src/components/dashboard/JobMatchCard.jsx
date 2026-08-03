function JobMatchCard({ jobMatches = [] }) {

  if (jobMatches.length === 0) {

    return (

      <div className="dashboard-card">

        <h2>Best Job Match</h2>

        <div
          style={{
            textAlign: "center",
            padding: "20px",
            color: "#666",
          }}
        >
          No job matches available.
        </div>

      </div>

    );

  }

  // Find the highest matching job
  const bestMatch = [...jobMatches].sort(
    (a, b) => b.match_score - a.match_score
  )[0];

  let badgeColor = "#EF4444";

  if (bestMatch.match_score >= 80) {

    badgeColor = "#16A34A";

  } else if (bestMatch.match_score >= 60) {

    badgeColor = "#F59E0B";

  }

  return (

    <div className="dashboard-card">

      <h2>Best Job Match</h2>

      <div
        style={{
          textAlign: "center",
          marginBottom: "20px",
        }}
      >

        <h3
          style={{
            marginBottom: "10px",
          }}
        >
          {bestMatch.job_title}
        </h3>

        <div
          style={{
            fontSize: "42px",
            fontWeight: "bold",
            color: "#7C3AED",
          }}
        >
          {bestMatch.match_score}%
        </div>

        <span
          style={{
            display: "inline-block",
            marginTop: "10px",
            background: badgeColor,
            color: "#fff",
            padding: "6px 15px",
            borderRadius: "20px",
            fontWeight: "bold",
          }}
        >
          {bestMatch.match_level}
        </span>

      </div>

      <div>

        <h4>Matched Skills</h4>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "8px",
            marginTop: "10px",
          }}
        >

          {bestMatch.matched_skills?.map((skill, index) => (

            <span
              key={index}
              style={{
                background: "#EDE9FE",
                color: "#6D28D9",
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