import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../../features/auth/authSlice';
import userReducer from '../../features/users/usersSlice';
import authorizationReducer from '../../features/authorization/authorizationSlice'


export const store = configureStore({
    reducer: {
        auth: authReducer,
        users: userReducer,
        authorization: authorizationReducer,
    }
});
