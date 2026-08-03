import { useEffect, useState } from "react";
import {
  FaUpload,
  FaFileAlt,
} from "react-icons/fa";

import DashboardCard from "../components/dashboard/DashboardCard";
import ATSCard from "../components/dashboard/ATSCard";
import ScoreCard from "../components/dashboard/ScoreCard";
import SkillCard from "../components/dashboard/SkillCard";
import JobMatchCard from "../components/dashboard/JobMatchCard";
import ATSChart from "../components/dashboard/ATSChart";
import JobMatchPreview from "../components/dashboard/JobMatchPreview";
import RecentActivity from "../components/dashboard/RecentActivity";
import QuickActions from "../components/dashboard/QuickActions";

import { getDashboard } from "../services/dashboardService";
import { downloadReport } from "../services/reportService";

import "../assets/styles/Dashboard.css";

function Dashboard() {

  const [dashboard, setDashboard] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const loadDashboard = async () => {

      try {

        const response = await getDashboard();

        setDashboard(response.data);

      } catch (error) {

        console.error(
          "Failed to load dashboard:",
          error
        );

      } finally {

        setLoading(false);

      }

    };

    loadDashboard();

  }, []);

  const resumeId =
    dashboard?.latest_resume_id;


  /**
   * Download Resume PDF
   */
  const handleDownload = async () => {

    if (!resumeId) {

      alert("No resume available.");

      return;

    }

    try {

      const response =
        await downloadReport(resumeId);

      const pdfBlob = new Blob(
        [response.data],
        {
          type: "application/pdf",
        }
      );

      const downloadUrl =
        window.URL.createObjectURL(pdfBlob);

      const link =
        document.createElement("a");

      link.href = downloadUrl;

      link.download =
        "AI_Resume_Analysis_Report.pdf";

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(
        downloadUrl
      );

    } catch (error) {

      console.error(
        "Download Failed:",
        error
      );

      alert(
        "Unable to download report."
      );

    }

  };


  if (loading) {

    return (

      <div className="dashboard-page">

        <h2>Loading Dashboard...</h2>

      </div>

    );

  }


  return (

    <div className="dashboard-page">

      {/* ========================= */}
      {/* Header */}
      {/* ========================= */}

      <div className="dashboard-header">

        <h1 className="welcome-text">

          Welcome,
          {" "}
          {dashboard?.user?.full_name || "User"} 👋

        </h1>

        <p className="dashboard-subtitle">

          AI Powered Resume Analyzer Dashboard

        </p>

      </div>


      {/* ========================= */}
      {/* Statistics */}
      {/* ========================= */}

      <div className="cards-container">

        <DashboardCard
          title="Uploaded Resumes"
          value={
            dashboard?.statistics?.total_resumes ?? 0
          }
          icon={<FaUpload />}
          color="#7C3AED"
        />

        <ATSCard
          ats={dashboard?.ats}
        />

        <ScoreCard
          statistics={
            dashboard?.statistics
          }
        />

        <SkillCard
          ats={dashboard?.ats}
        />

        <JobMatchCard
          jobMatches={
            dashboard?.job_matches
          }
        />

        <DashboardCard
          title="Recommendations"
          value={
            dashboard?.statistics
              ?.total_recommendations ?? 0
          }
          icon={<FaFileAlt />}
          color="#F59E0B"
        />

      </div>


      {/* ========================= */}
      {/* Charts */}
      {/* ========================= */}

      <div className="dashboard-grid">

        <ATSChart
          chartData={
            dashboard?.charts?.ats_chart
          }
        />

        <JobMatchPreview
          jobs={
            dashboard?.job_matches
          }
        />

      </div>


      {/* ========================= */}
      {/* Bottom */}
      {/* ========================= */}

      <div className="bottom-grid">

        <RecentActivity
          activities={
            dashboard?.recent_activity
          }
        />

        <QuickActions
          onDownload={handleDownload}
        />

      </div>

    </div>

  );

}

export default Dashboard;