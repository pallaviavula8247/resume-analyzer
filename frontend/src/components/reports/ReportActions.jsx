import {
  downloadReport,
  deleteReport,
  getReportDetail,
} from "../../services/reportService";

function ReportActions({
  report,
  refreshReports,
}) {

  // ==========================================
  // View Report Details
  // ==========================================

  const handleView = async () => {
    try {
      const response = await getReportDetail(report.id);

      console.log("Report Details:", response);

      alert(
        JSON.stringify(
          response,
          null,
          2
        )
      );

    } catch (error) {
      console.error("View report error:", error);

      alert(
        error.response?.data?.message ||
        "Unable to fetch report details."
      );
    }
  };


  // ==========================================
  // Download PDF
  // ==========================================

  const handleDownload = async () => {
    try {
      const response = await downloadReport(report.id);

      const blob = new Blob(
        [response.data],
        {
          type: "application/pdf",
        }
      );

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");

      link.href = url;

      link.download =
        `Resume_Report_${report.id}.pdf`;

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(url);

    } catch (error) {
      console.error("Download report error:", error);

      alert(
        error.response?.data?.message ||
        "Unable to download report."
      );
    }
  };


  // ==========================================
  // Delete Report
  // ==========================================

  const handleDelete = async () => {

    const confirmDelete = window.confirm(
      "Are you sure you want to delete this report?"
    );

    if (!confirmDelete) {
      return;
    }

    try {

      await deleteReport(report.id);

      alert(
        "Report deleted successfully."
      );

      if (refreshReports) {
        refreshReports();
      }

    } catch (error) {

      console.error(
        "Delete report error:",
        error
      );

      alert(
        error.response?.data?.message ||
        "Unable to delete report."
      );
    }
  };


  // ==========================================
  // Buttons
  // ==========================================

  return (
    <div className="report-actions">

      <button
        type="button"
        className="view-btn"
        onClick={handleView}
      >
        View
      </button>

      <button
        type="button"
        className="download-btn"
        onClick={handleDownload}
      >
        Download
      </button>

      <button
        type="button"
        className="delete-btn"
        onClick={handleDelete}
      >
        Delete
      </button>

    </div>
  );
}

export default ReportActions;