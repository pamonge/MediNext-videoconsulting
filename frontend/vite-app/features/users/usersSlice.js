import { createSlice } from '@reduxjs/toolkit';
import { fetchUsers } from './usersThunks';

const initialState = {
  list: [],      // Lista de usuarios
  loading: false,
  error: null,
};

const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {}, // Por ahora no tenemos acciones sync
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.list = action.payload; // Guardamos la lista de usuarios
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default usersSlice.reducer;