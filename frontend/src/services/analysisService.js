import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import ATSScoreCard from "../components/analysis/ATSScoreCard";
import ScoreBreakdown from "../components/analysis/ScoreBreakdown";
import StrengthList from "../components/analysis/StrengthList";
import WeaknessList from "../components/analysis/WeaknessList";
import MissingSkills from "../components/analysis/MissingSkills";
import RecommendationList from "../components/analysis/RecommendationList";
import JobMatchList from "../components/analysis/JobMatchList";

import {
  getATSAnalysis,
  getJobMatches,
  getRecommendations,
} from "../services/analysisService";

import { downloadReport } from "../services/reportService";

import "../assets/styles/AnalysisResult.css";

function AnalysisResult() {

  const { resumeId } = useParams();

  const navigate = useNavigate();

  const [ats, setATS] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [recommendations, setRecommendations] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {

    loadAnalysis();

  }, [resumeId]);

  const loadAnalysis = async () => {

    try {

      setLoading(true);

      const [
        atsResponse,
        jobsResponse,
        recommendationResponse,
      ] = await Promise.all([

        getATSAnalysis(resumeId),

        getJobMatches(resumeId),

        getRecommendations(resumeId),

      ]);

      setATS(atsResponse);

      setJobs(jobsResponse);

      setRecommendations(recommendationResponse);

    } catch (err) {

      console.error(err);

      setError("Unable to load analysis.");

    } finally {

      setLoading(false);

    }

  };

  const handleDownload = async () => {

    try {

      const response = await downloadReport(
        resumeId
      );

      const blob = new Blob(
        [response.data],
        {
          type: "application/pdf",
        }
      );

      const url =
        window.URL.createObjectURL(blob);

      const link =
        document.createElement("a");

      link.href = url;

      link.download =
        "AI_Resume_Analysis_Report.pdf";

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(url);

    } catch (error) {

      alert("Unable to download PDF.");

    }

  };

  if (loading) {

    return (

      <div className="analysis-loading">

        Loading Resume Analysis...

      </div>

    );

  }

  if (error) {

    return (

      <div className="analysis-error">

        {error}

      </div>

    );

  }

  return (

    <div className="analysis-page">

      <div className="analysis-header">

        <h1>

          AI Resume Analysis

        </h1>

        <div>

          <button
            onClick={handleDownload}
          >

            Download PDF

          </button>

          <button
            onClick={() => navigate("/dashboard")}
          >

            Dashboard

          </button>

        </div>

      </div>

      <ATSScoreCard
        ats={ats}
      />

      <ScoreBreakdown
        ats={ats}
      />

      <StrengthList
        strengths={ats?.strengths}
      />

      <WeaknessList
        weaknesses={ats?.weaknesses}
      />

      <MissingSkills
        skills={ats?.missing_skills}
      />

      <RecommendationList
        recommendations={recommendations}
      />

      <JobMatchList
        jobs={jobs}
      />

    </div>

  );

}

export default AnalysisResult;
