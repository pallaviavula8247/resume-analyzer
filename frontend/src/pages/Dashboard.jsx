import { useEffect, useState } from "react";
import { FaUpload, FaFileAlt } from "react-icons/fa";

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
        const data = await getDashboard();

        console.log("Dashboard Data:", data);

        setDashboard(data);
      } catch (error) {
        console.error("Dashboard Error:", error);
      } finally {
        setLoading(false);
      }
    };

    loadDashboard();
  }, []);

  const handleDownload = async () => {
    if (!dashboard?.latest_resume_id) {
      alert("No report available.");
      return;
    }

    try {
      const response = await downloadReport(
        dashboard.latest_resume_id
      );

      const blob = new Blob([response.data], {
        type: "application/pdf",
      });

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;
      link.download = "AI_Resume_Report.pdf";

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error(error);
      alert("Download failed.");
    }
  };

  if (loading) {
    return (
      <div className="dashboard-page">
        <h2>Loading Dashboard...</h2>
      </div>
    );
  }

  if (!dashboard) {
    return (
      <div className="dashboard-page">
        <h2>Dashboard data unavailable.</h2>
      </div>
    );
  }

  return (
    <div className="dashboard-page">

      {/* Header */}

      <div className="dashboard-header">
        <h1>
          Welcome, {dashboard.user?.full_name} 👋
        </h1>

        <p>
          AI Powered Resume Analyzer Dashboard
        </p>
      </div>

      {/* Statistics */}

      <div className="cards-container">

        <DashboardCard
          title="Uploaded Resumes"
          value={dashboard.statistics.total_resumes}
          icon={<FaUpload />}
          color="#7C3AED"
        />

        <ATSCard ats={dashboard.ats} />

        <ScoreCard
          statistics={dashboard.statistics}
        />

        <SkillCard ats={dashboard.ats} />

        <JobMatchCard
          jobMatches={dashboard.job_matches}
        />

        <DashboardCard
          title="Recommendations"
          value={dashboard.statistics.total_recommendations}
          icon={<FaFileAlt />}
          color="#F59E0B"
        />

      </div>

      {/* Charts */}

      <div className="dashboard-grid">

        <ATSChart
          chartData={dashboard.charts.ats_chart}
        />

        <JobMatchPreview
          jobs={dashboard.job_matches}
        />

      </div>

      {/* Bottom */}

      <div className="bottom-grid">

        <RecentActivity
          activities={dashboard.recent_activity}
        />

        <QuickActions
          onDownload={handleDownload}
        />

      </div>

    </div>
  );
}

export default Dashboard;