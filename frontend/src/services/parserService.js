import api from "./api";

// ==========================================
// Upload Resume
// ==========================================
export const uploadResume = async (file) => {
  const formData = new FormData();

  formData.append("resume_file", file);

  const response = await api.post(
    "/parser/upload/",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

// ==========================================
// Get Resume Details (Optional)
// ==========================================
export const getResume = async (resumeId) => {
  const response = await api.get(`/parser/${resumeId}/`);
  return response.data;
};