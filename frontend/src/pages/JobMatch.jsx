import React from "react";

const JobMatch = () => {
  return (
    <div className="container mt-4">
      <div
        style={{
          background: "#fff",
          padding: "30px",
          borderRadius: "10px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
        }}
      >
        <h2>Job Match</h2>

        <p>
          This page will display AI Job Matching results.
        </p>

        <hr />

        <h4>Features</h4>

        <ul>
          <li>Match Score</li>
          <li>Matched Skills</li>
          <li>Missing Skills</li>
          <li>Extra Skills</li>
          <li>AI Recommendations</li>
        </ul>
      </div>
    </div>
  );
};

export default JobMatch;