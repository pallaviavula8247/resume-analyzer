function ATSCard({ ats }) {

  if (!ats) {
    return (
      <div className="dashboard-card">

        <h2>ATS Analysis</h2>

        <p>No ATS analysis available.</p>

      </div>
    );
  }

  let color = "#ef4444";
  let status = "Needs Improvement";

  if (ats.ats_score >= 80) {
    color = "#22c55e";
    status = "Excellent";
  } else if (ats.ats_score >= 60) {
    color = "#f59e0b";
    status = "Good";
  }

  return (
    <div className="dashboard-card">

      <h2>ATS Analysis</h2>

      <div
        style={{
          textAlign: "center",
          marginTop: "15px",
        }}
      >
        <h1
          style={{
            color,
            fontSize: "60px",
            marginBottom: "10px",
          }}
        >
          {ats.ats_score}%
        </h1>

        <h3>{status}</h3>
      </div>

      <hr />

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "12px",
          marginTop: "20px",
        }}
      >
        <p>Keyword</p>
        <strong>{ats.keyword_score}%</strong>

        <p>Skills</p>
        <strong>{ats.skill_score}%</strong>

        <p>Education</p>
        <strong>{ats.education_score}%</strong>

        <p>Experience</p>
        <strong>{ats.experience_score}%</strong>

        <p>Projects</p>
        <strong>{ats.project_score}%</strong>

        <p>Certification</p>
        <strong>{ats.certification_score}%</strong>

        <p>Format</p>
        <strong>{ats.format_score}%</strong>

      </div>

    </div>
  );
}

export default ATSCard;