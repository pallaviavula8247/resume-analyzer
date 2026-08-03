import api from "./api";

// ===========================================
// Generate Report
// POST /api/reports/generate/:resumeId/
// ===========================================

export const generateReport = async (resumeId) => {
  const response = await api.post(
    `/reports/generate/${resumeId}/`
  );

  return response.data;
};

// ===========================================
// Get Report History
// GET /api/reports/
// ===========================================

export const getReports = async () => {
  const response = await api.get("/reports/");

  return response.data;
};

// ===========================================
// Get Report Detail
// GET /api/reports/:reportId/
// ===========================================

export const getReportDetail = async (reportId) => {
  const response = await api.get(
    `/reports/${reportId}/`
  );

  return response.data;
};

// ===========================================
// Download Report PDF
// GET /api/reports/:reportId/download/
// ===========================================

export const downloadReport = async (reportId) => {
  const response = await api.get(
    `/reports/${reportId}/download/`,
    {
      responseType: "blob",
    }
  );

  return response;
};

// ===========================================
// Delete Report
// DELETE /api/reports/:reportId/delete/
// ===========================================

export const deleteReport = async (reportId) => {
  const response = await api.delete(
    `/reports/${reportId}/delete/`
  );

  return response.data;
};