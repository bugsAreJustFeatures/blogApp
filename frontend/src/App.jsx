import { useRoutes } from 'react-router-dom'

import './App.css'
import Navbar from './Navbar/Navbar';
import HomePage from './HomePage/HomePage';
import LoginPage from './LoginPage/LoginPage';
import RegisterPage from './RegisterPage/RegisterPage';
import LogoutPage from './LogoutPage/LogoutPage';
import SettingsPage from "./SettingsPage/SettingsPage"
import BlogPage from "./BlogPage/BlogPage"
import UserBlogsPage from "./UserBlogsPage/UserBlogsPage"

function App() {

  const routes = useRoutes([
    {
      path: "/",
      element: < Navbar />,
      children: [
        {
          index: true,
          element: < HomePage />,
        },
        {
          path: "/register",
          element: < RegisterPage />,
        },
        {
          path: "/login",
          element: < LoginPage />,
        },
        {
          path: "/logout",
          element: < LogoutPage />,
        },
        {
          path: "/settings",
          element: < SettingsPage />,
        },
        {
          path: "/blogs/:blogId",
          element: < BlogPage />,
        },
        {
          path: "/users/:username",
          element: < UserBlogsPage />,
        }
      ]
    }
  ])

  return routes;
}

export default App
