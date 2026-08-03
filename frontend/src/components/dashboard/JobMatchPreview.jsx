function JobMatchPreview({ jobs = [] }) {

  if (jobs.length === 0) {

    return (

      <div className="dashboard-box">

        <h2>Top Job Matches</h2>

        <div
          style={{
            height: "250px",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            color: "#666",
            fontSize: "18px",
          }}
        >
          No Job Matches Available
        </div>

      </div>

    );

  }

  return (

    <div className="dashboard-box">

      <h2>Top Job Matches</h2>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "15px",
          paddingTop: "10px",
        }}
      >

        {jobs.slice(0, 5).map((job, index) => (

          <div
            key={index}
            style={{
              border: "1px solid #E5E7EB",
              borderRadius: "10px",
              padding: "15px",
            }}
          >

            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
              }}
            >

              <h3
                style={{
                  margin: 0,
                  fontSize: "17px",
                }}
              >
                {job.job_title}
              </h3>

              <span
                style={{
                  background: "#7C3AED",
                  color: "#fff",
                  padding: "6px 12px",
                  borderRadius: "20px",
                  fontWeight: "bold",
                }}
              >
                {job.match_score}%
              </span>

            </div>

            <p
              style={{
                marginTop: "8px",
                color: "#666",
              }}
            >
              Match Level:
              <strong>
                {" "}
                {job.match_level}
              </strong>
            </p>

            {job.matched_skills &&
              job.matched_skills.length > 0 && (

              <div
                style={{
                  marginTop: "10px",
                }}
              >

                <strong>
                  Matched Skills:
                </strong>

                <div
                  style={{
                    marginTop: "8px",
                    display: "flex",
                    flexWrap: "wrap",
                    gap: "8px",
                  }}
                >

                  {job.matched_skills.map((skill, i) => (

                    <span
                      key={i}
                      style={{
                        background: "#EDE9FE",
                        color: "#6D28D9",
                        padding: "5px 10px",
                        borderRadius: "20px",
                        fontSize: "13px",
                      }}
                    >
                      {skill}
                    </span>

                  ))}

                </div>

              </div>

            )}

          </div>

        ))}

      </div>

    </div>

  );

}

export default JobMatchPreview;