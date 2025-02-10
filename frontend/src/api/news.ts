import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

export const getNews = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/news/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching news:', error);
    throw error;
  }
};
