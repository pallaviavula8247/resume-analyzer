import ReportCard from "./ReportCard";

function ReportTable({
  reports,
  refreshReports,
}) {

  return (

    <div className="report-table-container">

      <table className="report-table">

        <thead>

          <tr>

            <th>ID</th>

            <th>Title</th>

            <th>ATS Score</th>

            <th>Match Score</th>

            <th>Status</th>

            <th>Generated</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          {reports.map((report) => (

            <ReportCard
              key={report.id}
              report={report}
              refreshReports={refreshReports}
            />

          ))}

        </tbody>

      </table>

    </div>

  );

}

export default ReportTable;