import React from 'react';
import { useAuthStore } from '../store/authStore';
import { useNavigate } from 'react-router-dom';

export const DashboardPage = () => {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div>
      <h2>Dashboard</h2>
      {user && <p>Welcome, {user.username}! (Role: {user.role})</p>}
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};
