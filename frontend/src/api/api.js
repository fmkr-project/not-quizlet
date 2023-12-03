import axios from 'axios';

const API_URL = 'http://localhost:5001'; // Replace with your backend API URL

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getSomeData = () => {
  return api.get('/api/endpoint');
};

export const postSomeData = (data) => {
  return api.post('/api/endpoint', data);
};
