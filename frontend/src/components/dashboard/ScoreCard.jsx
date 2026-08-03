function ScoreCard({ statistics }) {

  if (!statistics) {

    return (

      <div className="dashboard-card">

        <h2>Dashboard Statistics</h2>

        <div
          style={{
            textAlign: "center",
            padding: "20px",
            color: "#666",
          }}
        >
          No statistics available.
        </div>

      </div>

    );

  }

  return (

    <div className="dashboard-card">

      <h2>Dashboard Statistics</h2>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "15px",
          marginTop: "15px",
        }}
      >

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Average ATS Score</span>

          <strong>
            {statistics.average_ats_score}%
          </strong>

        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Highest ATS Score</span>

          <strong>
            {statistics.highest_ats_score}%
          </strong>

        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Total Job Matches</span>

          <strong>
            {statistics.total_job_matches}
          </strong>

        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Total Recommendations</span>

          <strong>
            {statistics.total_recommendations}
          </strong>

        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>Total Resumes</span>

          <strong>
            {statistics.total_resumes}
          </strong>

        </div>

      </div>

    </div>

  );

}

export default ScoreCard;