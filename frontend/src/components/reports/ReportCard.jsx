import ReportActions from "./ReportActions";

function ReportCard({
  report,
  refreshReports,
}) {

  const formatDate = (date) => {

    if (!date) {
      return "-";
    }

    return new Date(date).toLocaleString();
  };


  const atsScore =
    report.ats_score ?? 0;

  const matchScore =
    report.match_score ?? 0;

  const status =
    report.status || "Unknown";


  return (
    <tr>

      <td>
        {report.id}
      </td>


      <td>
        {report.report_title ||
          "AI Resume Analyzer Report"}
      </td>


      <td>
        <strong>
          {atsScore}%
        </strong>
      </td>


      <td>
        {matchScore}%
      </td>


      <td>

        <span
          className={`status ${status.toLowerCase()}`}
        >
          {status}
        </span>

      </td>


      <td>
        {formatDate(
          report.generated_at
        )}
      </td>


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