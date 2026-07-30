import api from "./api";

// ===================================
// Register User
// ===================================
export const registerUser = async (userData) => {
  const response = await api.post("/users/register/", userData);
  return response.data;
};

// ===================================
// Login User
// ===================================
export const loginUser = async (credentials) => {
  const response = await api.post("/users/login/", credentials);

  if (response.data.access && response.data.refresh) {
    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);

    // Store user details
    if (response.data.user) {
      localStorage.setItem(
        "user",
        JSON.stringify(response.data.user)
      );
    }
  }

  return response.data;
};

// ===================================
// Get Logged-in User Profile
// ===================================
export const getProfile = async () => {
  const response = await api.get("/users/profile/");
  return response.data;
};

// ===================================
// Get Logged-in User from Local Storage
// ===================================
export const getCurrentUser = () => {
  const user = localStorage.getItem("user");

  return user ? JSON.parse(user) : null;
};

// ===================================
// Check Login Status
// ===================================
export const isAuthenticated = () => {
  return !!localStorage.getItem("access_token");
};

// ===================================
// Logout User
// ===================================
export const logoutUser = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("user");
};