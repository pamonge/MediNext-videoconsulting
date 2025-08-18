import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const fetchAuthorizationData = createAsyncThunk(
    'authorization/fetchData',
    async (_, { getState }) => {
        const token = getState().auth.token;
        const { data } = await axios.get('http://0.0.0.0:8000/authorization', {
            headers: {Authorization: 'Bearer ${token}'}
        })
        return data;
    }
)