import axios from 'axios';

const API_URL = '/api';

export const postQuery = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/chat`, { message });
    return response.data;
  } catch (error) {
    console.error("Error fetching response from backend:", error);
    throw error;
  }
};
