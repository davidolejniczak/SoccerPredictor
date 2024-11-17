import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000', // Backend Flask API URL
});

export const fetchPrediction = async (features: number[]) => {
  const response = await API.post('/predict', { features });
  return response.data;
};

export default API;
