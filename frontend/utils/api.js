import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api/api"; // Ensure this matches FastAPI routes

export const fetchNews = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/news/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching news:", error);
    return [];
  }
};
