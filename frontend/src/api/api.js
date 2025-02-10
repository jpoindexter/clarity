import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getNews = async () => {
  try {
    const response = await api.get('/api/news');
    return response.data;
  } catch (error) {
    console.error('There was an error fetching the news:', error);
    throw error;
  }
};

export const createNews = async (newsData) => {
  try {
    const response = await api.post('/news/', newsData);
    return response.data;
  } catch (error) {
    console.error('There was an error creating the news:', error);
    throw error;
  }
};
