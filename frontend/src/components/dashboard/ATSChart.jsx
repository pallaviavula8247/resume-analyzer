function ATSChart({ chartData }) {

  if (
    !chartData ||
    !Array.isArray(chartData.labels) ||
    !Array.isArray(chartData.scores)
  ) {
    return (
      <div className="dashboard-card">

        <h2>ATS Score History</h2>

        <p>No ATS Chart Available.</p>

      </div>
    );
  }

  return (
    <div className="dashboard-card">

      <h2>ATS Score History</h2>

      <table
        style={{
          width: "100%",
          marginTop: "20px",
          borderCollapse: "collapse",
        }}
      >

        <thead>

          <tr>

            <th
              style={{
                textAlign: "left",
                padding: "10px",
              }}
            >
              Resume
            </th>

            <th
              style={{
                textAlign: "center",
              }}
            >
              Score
            </th>

            <th>
              Progress
            </th>

          </tr>

        </thead>

        <tbody>

          {chartData.labels.map((label, index) => {

            const score = chartData.scores[index];

            let color = "#ef4444";

            if (score >= 80) color = "#22c55e";
            else if (score >= 60) color = "#f59e0b";

            return (

              <tr key={index}>

                <td
                  style={{
                    padding: "12px",
                  }}
                >
                  {label}
                </td>

                <td
                  style={{
                    textAlign: "center",
                    fontWeight: "bold",
                  }}
                >
                  {score}%
                </td>

                <td>

                  <div
                    style={{
                      width: "100%",
                      background: "#ddd",
                      borderRadius: "20px",
                      overflow: "hidden",
                    }}
                  >

                    <div
                      style={{
                        width: `${score}%`,
                        background: color,
                        color: "#fff",
                        textAlign: "center",
                        padding: "4px",
                      }}
                    >
                      {score}%
                    </div>

                  </div>

                </td>

              </tr>

            );

          })}

        </tbody>

      </table>

    </div>
  );
}

export default ATSChart;