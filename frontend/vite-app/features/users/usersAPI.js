import axios from 'axios';

export const fetchUserRequest = async () => {
    const response = await axios.get('http://0.0.0.0:8000/user/');
    return response.data;
}