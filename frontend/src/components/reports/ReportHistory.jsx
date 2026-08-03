import ReportTable from "./ReportTable";

function ReportHistory({
  reports,
  loading,
  refreshReports,
}) {

  if (loading) {
    return (
      <div className="report-loading">
        <h3>Loading reports...</h3>
      </div>
    );
  }

  if (!reports || reports.length === 0) {
    return (
      <div className="report-empty">
        <h3>No reports available.</h3>
        <p>
          Generate your first AI Resume Report.
        </p>
      </div>
    );
  }

  return (

    <div className="report-history">

      <h2>Report History</h2>

      <ReportTable
        reports={reports}
        refreshReports={refreshReports}
      />

    </div>

  );

}

export default ReportHistory;