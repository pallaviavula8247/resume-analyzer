import "./DashboardCard.css";

function JobMatchPreview({ jobs = [] }) {
  if (!jobs || jobs.length === 0) {
    return (
      <div className="dashboard-card">
        <div className="card-top">
          <div
            className="card-icon"
            style={{ background: "#8B5CF6" }}
          >
            📊
          </div>

          <h3>Top Job Matches</h3>
        </div>

        <div
          style={{
            padding: "40px",
            textAlign: "center",
            color: "#777",
          }}
        >
          No Job Matches Available
        </div>
      </div>
    );
  }

  return (
    <div className="dashboard-card">

      <div className="card-top">

        <div
          className="card-icon"
          style={{
            background: "#8B5CF6",
          }}
        >
          📊
        </div>

        <h3>Top Job Matches</h3>

      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "18px",
          marginTop: "20px",
        }}
      >

        {jobs.slice(0, 5).map((job, index) => {

          const score = job.match_score;

          let progressColor = "#EF4444";

          if (score >= 80) {
            progressColor = "#22C55E";
          } else if (score >= 60) {
            progressColor = "#F59E0B";
          }

          return (

            <div
              key={index}
              style={{
                border: "1px solid #E5E7EB",
                borderRadius: "12px",
                padding: "18px",
                background: "#FAFAFA",
              }}
            >

              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  marginBottom: "10px",
                }}
              >

                <div>

                  <h4
                    style={{
                      margin: 0,
                      color: "#111827",
                    }}
                  >
                    {job.job_title}
                  </h4>

                  <small
                    style={{
                      color: "#6B7280",
                    }}
                  >
                    {job.match_level}
                  </small>

                </div>

                <div
                  style={{
                    background: "#7C3AED",
                    color: "#fff",
                    padding: "8px 14px",
                    borderRadius: "20px",
                    fontWeight: "bold",
                  }}
                >
                  {score}%
                </div>

              </div>

              <div
                style={{
                  width: "100%",
                  height: "10px",
                  background: "#E5E7EB",
                  borderRadius: "20px",
                  overflow: "hidden",
                  marginBottom: "15px",
                }}
              >

                <div
                  style={{
                    width: `${score}%`,
                    height: "100%",
                    background: progressColor,
                    transition: ".4s",
                  }}
                />

              </div>

              <div
                style={{
                  display: "flex",
                  flexWrap: "wrap",
                  gap: "8px",
                }}
              >

                {(job.matched_skills || []).slice(0, 6).map((skill, i) => (

                  <span
                    key={i}
                    style={{
                      background: "#EEF2FF",
                      color: "#4338CA",
                      padding: "6px 12px",
                      borderRadius: "20px",
                      fontSize: "12px",
                      fontWeight: "500",
                    }}
                  >
                    {skill}
                  </span>

                ))}

              </div>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default JobMatchPreview;