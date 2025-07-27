import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import axios from 'axios';

interface User {
  id: number;
  username: string;
  role: string;
}

interface AuthState {
  accessToken: string | null;
  user: User | null;
  isAuthenticated: boolean;
  login: (credentials: { username?: string; password?: string }) => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      accessToken: null,
      user: null,
      isAuthenticated: false,
      login: async (credentials) => {
        try {
          const response = await axios.post('http://localhost:8000/api/v1/auth/login/', credentials);
          const { access } = response.data;

          // For now, we decode the user from the token. A better approach is a /profile call.
          const userPayload = JSON.parse(atob(access.split('.')[1]));
          const user: User = { id: userPayload.user_id, username: userPayload.username || 'user', role: userPayload.role };

          set({ accessToken: access, user, isAuthenticated: true });
        } catch (error) {
          console.error('Login failed:', error);
          set({ accessToken: null, user: null, isAuthenticated: false });
          throw error;
        }
      },
      logout: () => {
        set({ accessToken: null, user: null, isAuthenticated: false });
      },
    }),
    {
      name: 'auth-storage', // name of the item in the storage (must be unique)
    }
  )
);
