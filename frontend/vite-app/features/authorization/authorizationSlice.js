import { createSlice } from "@reduxjs/toolkit";
import { fetchAuthorizationData } from "./authorizationThunk";

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
            .addCase(fetchAuthorizationData.fulfilled, (state, action) => {
                state.loading = false;
                state.data = action.payload;
            })
            .addCase(fetchAuthorizationData.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message;
            });
    }
})

export default authorizationSlice.reducer;