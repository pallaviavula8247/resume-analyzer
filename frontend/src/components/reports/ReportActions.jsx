import {
  downloadReport,
  deleteReport,
  getReportDetail,
} from "../../services/reportService";

function ReportActions({
  report,
  refreshReports,
}) {

  // ==========================
  // View Report Details
  // ==========================
  const handleView = async () => {

    try {

      const response =
        await getReportDetail(report.id);

      console.log("Report Details:", response);

      alert(
        JSON.stringify(
          response.data,
          null,
          2
        )
      );

    } catch (error) {

      console.error(error);

      alert("Unable to fetch report details.");

    }

  };

  // ==========================
  // Download PDF
  // ==========================
  const handleDownload = async () => {

    try {

      const response =
        await downloadReport(report.id);

      const url =
        window.URL.createObjectURL(
          new Blob([response.data])
        );

      const link =
        document.createElement("a");

      link.href = url;

      link.download =
        `Report_${report.id}.pdf`;

      document.body.appendChild(link);

      link.click();

      document.body.removeChild(link);

      window.URL.revokeObjectURL(url);

    } catch (error) {

      console.error(error);

      alert("Unable to download report.");

    }

  };

  // ==========================
  // Delete Report
  // ==========================
  const handleDelete = async () => {

    const confirmDelete =
      window.confirm(
        "Are you sure you want to delete this report?"
      );

    if (!confirmDelete) return;

    try {

      await deleteReport(report.id);

      alert("Report deleted successfully.");

      refreshReports();

    } catch (error) {

      console.error(error);

      alert("Unable to delete report.");

    }

  };

  return (

    <div className="report-actions">

      <button
        className="view-btn"
        onClick={handleView}
      >
        👁 View
      </button>

      <button
        className="download-btn"
        onClick={handleDownload}
      >
        📥 Download
      </button>

      <button
        className="delete-btn"
        onClick={handleDelete}
      >
        🗑 Delete
      </button>

    </div>

  );

}

export default ReportActions;