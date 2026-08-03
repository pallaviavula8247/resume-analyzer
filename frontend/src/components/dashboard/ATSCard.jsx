function ATSCard({ ats }) {

  if (!ats) {

    return (

      <div className="dashboard-card">

        <h2>ATS Score</h2>

        <div
          style={{
            textAlign: "center",
            padding: "20px",
            color: "#666",
          }}
        >
          No ATS analysis available.
        </div>

      </div>

    );

  }

  let status = "Needs Improvement";

  if (ats.ats_score >= 80) {

    status = "Excellent";

  } else if (ats.ats_score >= 60) {

    status = "Good";

  }

  return (

    <div className="dashboard-card">

      <h2>ATS Score</h2>

      <div
        style={{
          textAlign: "center",
          marginBottom: "20px",
        }}
      >

        <h1
          style={{
            fontSize: "48px",
            color: "#7C3AED",
            margin: 0,
          }}
        >
          {ats.ats_score}%
        </h1>

        <p
          style={{
            fontWeight: "bold",
            color: "#555",
          }}
        >
          {status}
        </p>

      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "12px",
        }}
      >

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Keyword Score</span>
          <strong>{ats.keyword_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Skill Score</span>
          <strong>{ats.skill_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Education</span>
          <strong>{ats.education_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Experience</span>
          <strong>{ats.experience_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Projects</span>
          <strong>{ats.project_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Certifications</span>
          <strong>{ats.certification_score}%</strong>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Format</span>
          <strong>{ats.format_score}%</strong>
        </div>

      </div>

    </div>

  );

}

export default ATSCard;