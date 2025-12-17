import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://weather-backend-19gt.onrender.com',
});

export const postQuery = async (message) => {
  try {
    const response = await apiClient.post('/chat', { message });
    return response.data;
  } catch (error) {
    console.error("Error fetching response from backend:", error);
    throw error;
  }
};
