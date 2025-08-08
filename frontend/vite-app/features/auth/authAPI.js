import axios from 'axios';

export const loginRequest = async (credentials) => {
    const response = await axios.post('http://0.0.0.0:8000/user/login', credentials);
    return response.data;
}