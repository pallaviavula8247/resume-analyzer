import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { uploadResume } from "../services/parserService";

const UploadResume = () => {
  const navigate = useNavigate();

  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  // ==============================
  // Handle File Selection
  // ==============================
  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
    setMessage("");
    setError("");
  };

  // ==============================
  // Upload Resume
  // ==============================
  const handleUpload = async () => {
    if (!selectedFile) {
      setError("Please select a resume file.");
      return;
    }

    setLoading(true);
    setMessage("");
    setError("");

    try {
      const response = await uploadResume(selectedFile);

      console.log("Upload Response:", response);

      if (!response.success) {
        throw new Error(response.message || "Upload failed.");
      }

      const resumeId = response.data.resume_id;

      localStorage.setItem("resume_id", resumeId);

      setMessage(response.message);

      setTimeout(() => {
        navigate("/analysis");
      }, 1000);

    } catch (err) {
      console.error("Upload Error:", err);

      setError(
        err.response?.data?.message ||
        err.message ||
        "Upload failed."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "700px",
        margin: "40px auto",
        background: "#ffffff",
        padding: "30px",
        borderRadius: "10px",
        boxShadow: "0px 0px 10px rgba(0,0,0,0.1)"
      }}
    >
      <h2>Upload Resume</h2>

      <p>
        Upload your Resume (PDF, DOC or DOCX)
      </p>

      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={handleFileChange}
      />

      <br />
      <br />

      {selectedFile && (
        <div>
          <strong>Selected File:</strong>
          <br />
          {selectedFile.name}
        </div>
      )}

      <br />

      <button
        onClick={handleUpload}
        disabled={loading}
        style={{
          padding: "10px 20px",
          background: "#4F46E5",
          color: "#ffffff",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      >
        {loading ? "Uploading..." : "Upload Resume"}
      </button>

      {message && (
        <p
          style={{
            color: "green",
            marginTop: "20px",
            fontWeight: "bold"
          }}
        >
          {message}
        </p>
      )}

      {error && (
        <p
          style={{
            color: "red",
            marginTop: "20px",
            fontWeight: "bold"
          }}
        >
          {error}
        </p>
      )}
    </div>
  );
};

export default UploadResume;