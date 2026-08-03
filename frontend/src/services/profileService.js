import api from "./api";

// ===========================================
// Get User Profile
// GET /api/users/profile/
// ===========================================

export const getUserProfile = async () => {
  const response = await api.get("/users/profile/");
  return response.data;
};

// ===========================================
// Update User Profile
// PUT /api/users/profile/
// ===========================================

export const updateUserProfile = async (profileData) => {
  const response = await api.put(
    "/users/profile/",
    profileData
  );

  return response.data;
};

// ===========================================
// Dashboard Statistics
// GET /api/dashboard/
// ===========================================

export const getProfileStatistics = async () => {
  const response = await api.get("/dashboard/");
  return response.data;
};