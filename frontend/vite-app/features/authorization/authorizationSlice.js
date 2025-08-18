import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const authorizationSlice = createSlice({
    name: 'authorization',
    initialState: {
        data: null,
        loading: null,
        error: null
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchAuthorizationData.pending, (state) => {
                state.loading = true;
            
            })
    }
})