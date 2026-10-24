import { NavLink } from 'react-router-dom';
import css from './AuthNav.module.css';

export const AuthNav = () => {
  return (
    <div>
      <NavLink
        to="/register"
        className={({ isActive }) =>
          isActive ? `${css.authNavLink} ${css.active}` : css.authNavLink
        }
      >
        Register
      </NavLink>
      <NavLink
        to="/login"
        className={({ isActive }) =>
          isActive ? `${css.authNavLink} ${css.active}` : css.authNavLink
        }
      >
        Log In
      </NavLink>
    </div>
  );
};