import axios from 'axios';

const API_URL = 'http://localhost:3000';

const apiClient = axios.create({
  baseURL: API_URL,
  timeout: 10000, // indicates, 10000ms before timeout
});

export default apiClient;