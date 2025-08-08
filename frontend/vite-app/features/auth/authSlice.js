import { createSlice } from '@reduxjs/toolkit';

const initialState = {
    isAuthenticated: false,
    user: null,
    token: null,
}

export const authSlice = createSlice({
    name: 'auth',
    reducers: {
        login(state, action) {
            const { user, token} = action.payload;
            state.isAuthenticated = true;
            state.user = user;
            state.token = token;
        },
        logout(state) {
            state.isAuthenticated = false;
            state.user = null;
            state.token = null;
        }
    }
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;