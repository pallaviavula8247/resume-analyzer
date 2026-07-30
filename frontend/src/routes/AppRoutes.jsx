import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "../layout/Layout";

import Home from "../pages/Home";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Dashboard from "../pages/Dashboard";
import UploadResume from "../pages/UploadResume";
import AnalysisResult from "../pages/AnalysisResult";
import Reports from "../pages/Reports";
import NotFound from "../pages/NotFound";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>

          <Route path="/" element={<Home />} />

          <Route path="/login" element={<Login />} />

          <Route path="/register" element={<Register />} />

          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/upload" element={<UploadResume />} />

          <Route path="/analysis" element={<AnalysisResult />} />

          <Route path="/reports" element={<Reports />} />

          <Route path="*" element={<NotFound />} />

        </Routes>
      </Layout>
    </BrowserRouter>
  );
};

export default AppRoutes;