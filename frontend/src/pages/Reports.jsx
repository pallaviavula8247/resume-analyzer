import { useCallback, useEffect, useState } from "react";

import { getReports } from "../services/reportService";
import ReportHistory from "../components/reports/ReportHistory";

import "./Reports.css";


// ============================================================
// Reports Page
// ============================================================

const Reports = () => {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");


  // ============================================================
  // Fetch Reports
  // ============================================================

  const fetchReports = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const response = await getReports();

      console.log("Reports API Response:", response);

      /*
        Backend response:

        {
          success: true,
          count: 4,
          reports: [...]
        }
      */

      if (response?.success === true) {
        setReports(
          Array.isArray(response.reports)
            ? response.reports
            : []
        );
      } else {
        setReports([]);

        setError(
          response?.message ||
          "Unable to load reports."
        );
      }

    } catch (err) {

      console.error(
        "Failed to fetch reports:",
        err
      );

      setReports([]);

      if (err.response?.status === 401) {

        setError(
          "Your session has expired. Please login again."
        );

      } else if (err.response?.status === 403) {

        setError(
          "You do not have permission to view reports."
        );

      } else if (err.response?.status === 404) {

        setError(
          "Reports API endpoint was not found."
        );

      } else {

        setError(
          err.response?.data?.message ||
          "Unable to load reports. Please try again."
        );
      }

    } finally {
      setLoading(false);
    }

  }, []);


  // ============================================================
  // Load Reports When Page Opens
  // ============================================================

  useEffect(() => {
    fetchReports();
  }, [fetchReports]);


  // ============================================================
  // Loading State
  // ============================================================

  if (loading) {

    return (
      <div className="reports-page">

        <div className="reports-header">

          <div>
            <h1>Resume Reports</h1>

            <p>
              View, download and manage your
              AI resume analysis reports.
            </p>
          </div>

        </div>

        <div className="report-loading">
          <h3>Loading reports...</h3>
          <p>Please wait while we fetch your reports.</p>
        </div>

      </div>
    );
  }


  // ============================================================
  // Error State
  // ============================================================

  if (error) {

    return (
      <div className="reports-page">

        <div className="reports-header">

          <div>
            <h1>Resume Reports</h1>

            <p>
              View, download and manage your
              AI resume analysis reports.
            </p>
          </div>

          <button
            type="button"
            className="generate-btn"
            onClick={fetchReports}
          >
            Retry
          </button>

        </div>

        <div className="report-empty">

          <h3>
            Unable to load reports
          </h3>

          <p>
            {error}
          </p>

          <button
            type="button"
            className="generate-btn"
            onClick={fetchReports}
          >
            Try Again
          </button>

        </div>

      </div>
    );
  }


  // ============================================================
  // Main Reports Page
  // ============================================================

  return (
    <div className="reports-page">

      {/* ======================================================
          Header
      ====================================================== */}

      <div className="reports-header">

        <div>

          <h1>
            Resume Reports
          </h1>

          <p>
            View, download and manage your
            AI resume analysis reports.
          </p>

        </div>

        <button
          type="button"
          className="generate-btn"
          onClick={fetchReports}
        >
          Refresh Reports
        </button>

      </div>


      {/* ======================================================
          Report History
      ====================================================== */}

      <ReportHistory
        reports={reports}
        loading={loading}
        refreshReports={fetchReports}
      />

    </div>
  );
};


export default Reports;