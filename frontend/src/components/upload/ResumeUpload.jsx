function UploadResume() {
  return (
    <div className="upload-page">

      <h1>Upload Resume</h1>

      <p>Upload your resume to get ATS score and AI recommendations.</p>

      <input
        type="file"
        accept=".pdf,.doc,.docx"
      />

      <button>Upload Resume</button>

    </div>
  );
}

export default UploadResume;