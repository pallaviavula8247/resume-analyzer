function SkillCard({ ats }) {

  if (!ats) {

    return (

      <div className="dashboard-card">

        <h2>Skills Analysis</h2>

        <div
          style={{
            textAlign: "center",
            padding: "20px",
            color: "#666",
          }}
        >
          No skill analysis available.
        </div>

      </div>

    );

  }

  return (

    <div className="dashboard-card">

      <h2>Skills Analysis</h2>

      {/* Skill Score */}

      <div
        style={{
          marginBottom: "20px",
        }}
      >

        <strong>
          Skill Score
        </strong>

        <div
          style={{
            width: "100%",
            height: "12px",
            background: "#E5E7EB",
            borderRadius: "10px",
            marginTop: "8px",
            overflow: "hidden",
          }}
        >

          <div
            style={{
              width: `${ats.skill_score}%`,
              height: "100%",
              background: "#7C3AED",
              borderRadius: "10px",
            }}
          />

        </div>

        <p
          style={{
            marginTop: "8px",
            fontWeight: "bold",
          }}
        >
          {ats.skill_score}%
        </p>

      </div>

      {/* Strengths */}

      <div
        style={{
          marginBottom: "20px",
        }}
      >

        <h3>✅ Strengths</h3>

        {ats.strengths?.length > 0 ? (

          <ul>

            {ats.strengths.map((item, index) => (

              <li key={index}>
                {item}
              </li>

            ))}

          </ul>

        ) : (

          <p>No strengths found.</p>

        )}

      </div>

      {/* Missing Skills */}

      <div
        style={{
          marginBottom: "20px",
        }}
      >

        <h3>⚠ Missing Skills</h3>

        {ats.missing_skills?.length > 0 ? (

          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: "8px",
            }}
          >

            {ats.missing_skills.map((skill, index) => (

              <span
                key={index}
                style={{
                  background: "#FEE2E2",
                  color: "#B91C1C",
                  padding: "6px 12px",
                  borderRadius: "20px",
                  fontSize: "13px",
                }}
              >
                {skill}
              </span>

            ))}

          </div>

        ) : (

          <p>No missing skills.</p>

        )}

      </div>

      {/* Weaknesses */}

      <div>

        <h3>❌ Weaknesses</h3>

        {ats.weaknesses?.length > 0 ? (

          <ul>

            {ats.weaknesses.map((item, index) => (

              <li key={index}>
                {item}
              </li>

            ))}

          </ul>

        ) : (

          <p>No weaknesses found.</p>

        )}

      </div>

    </div>

  );

}

export default SkillCard;