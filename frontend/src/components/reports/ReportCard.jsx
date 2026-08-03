import ReportActions from "./ReportActions";

function ReportCard({
  report,
  refreshReports,
}) {

  const formatDate = (date) => {

    if (!date) return "-";

    return new Date(date).toLocaleString();

  };

  return (

    <tr>

      <td>{report.id}</td>

      <td>{report.report_title}</td>

      <td>{report.ats_score}</td>

      <td>{report.match_score}</td>

      <td>

        <span className={`status ${report.status.toLowerCase()}`}>
          {report.status}
        </span>

      </td>

      <td>{formatDate(report.generated_at)}</td>

      <td>

        <ReportActions
          report={report}
          refreshReports={refreshReports}
        />

      </td>

    </tr>

  );

}

export default ReportCard;