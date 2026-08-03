import { downloadReport } from "../services/reportService";

const handleDownload = async () => {
    try {

        const file = await downloadReport(1);

        const url = window.URL.createObjectURL(file);

        const link = document.createElement("a");

        link.href = url;

        link.download = "AI_Resume_Analysis_Report.pdf";

        link.click();

    } catch (error) {

        console.error(error);

        alert("Download failed");

    }
};