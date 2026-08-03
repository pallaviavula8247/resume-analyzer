import api from "./api";

/**
 * Get complete dashboard data
 */
export const getDashboard = async () => {
  try {
    const response = await api.get("/dashboard/");
    return response.data;
  } catch (error) {
    console.error("Dashboard API Error:", error);
    throw error;
  }
};