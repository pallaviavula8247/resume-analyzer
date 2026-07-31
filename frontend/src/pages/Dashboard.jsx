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

import { getProfile } from "../services/authService";

import "../assets/styles/Dashboard.css";

function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const loadProfile = async () => {
      try {
        const data = await getProfile();
        setUser(data);
      } catch (error) {
        console.error("Failed to load profile:", error);
      }
    };

    loadProfile();
  }, []);

  return (
    <div className="dashboard-page">

      {/* Welcome Section */}
      <div className="dashboard-header">

        <h1 className="welcome-text">
          Welcome, {user?.full_name || "User"} 👋
        </h1>

        <p className="dashboard-subtitle">
          AI Powered Resume Analyzer Dashboard
        </p>

      </div>

      {/* Statistics Cards */}
      <div className="cards-container">

        <DashboardCard
          title="Uploaded Resumes"
          value="3"
          icon={<FaUpload />}
          color="#7C3AED"
        />

        <ATSCard />

        <ScoreCard />

        <SkillCard />

        <JobMatchCard />

        <DashboardCard
          title="Reports"
          value="5"
          icon={<FaFileAlt />}
          color="#F59E0B"
        />

      </div>

      {/* Charts Section */}
      <div className="dashboard-grid">

        <ATSChart />

        <JobMatchPreview />

      </div>

      {/* Bottom Section */}
      <div className="bottom-grid">

        <RecentActivity />

        <QuickActions />

      </div>

    </div>
  );
}

export default Dashboard;