import { createAsyncThunk } from '@reduxjs/toolkit';
import { fetchUsersRequest } from '../users/usersAPI';

// Crear una funcion que maneja el async/await de manera automatica
export const fetchUsers = createAsyncThunk(
    'users/fetchUsers', 
    async (_, thunkAPI) => {
        try {
            const data = await fetchUsersRequest();
            return data;
        } catch (error) {
            return thunkAPI.rejectWithValue(error.response?.data || 'Error al obtener usuarios.')
        }
    }
)