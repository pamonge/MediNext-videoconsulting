import axios from 'axios';

export const loginRequest = async (credentials) => {
    const response = await axios.post('http://localhost:8000/api/login', credentials);
    return response.data;
}