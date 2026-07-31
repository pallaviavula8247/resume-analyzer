import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "../layout/Layout";

import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Dashboard from "../pages/Dashboard";
import UploadResume from "../pages/UploadResume";
import AnalysisResult from "../pages/AnalysisResult";
import Reports from "../pages/Reports";
import Profile from "../pages/Profile";
import Recommendations from "../pages/Recommendations";
import JobMatch from "../pages/JobMatch";
import NotFound from "../pages/NotFound";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>

        {/* Public Routes */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes with Navbar */}
        <Route element={<Layout />}>

          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/upload" element={<UploadResume />} />

          <Route path="/analysis" element={<AnalysisResult />} />

          <Route path="/job-match" element={<JobMatch />} />

          <Route
            path="/recommendations"
            element={<Recommendations />}
          />

          <Route path="/reports" element={<Reports />} />

          <Route path="/profile" element={<Profile />} />

        </Route>

        {/* 404 */}
        <Route path="*" element={<NotFound />} />

      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;