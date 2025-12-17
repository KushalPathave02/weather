import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.PROD ? import.meta.env.VITE_API_URL : '/api',
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
