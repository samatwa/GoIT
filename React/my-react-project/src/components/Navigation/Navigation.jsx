import { NavLink } from "react-router-dom";
import css from "./Navigation.module.css";

const getActiveLink = ({ isActive }) => {
  return isActive ? css.active : null;
};

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/" className={getActiveLink}>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink className={getActiveLink} to="/articles">
            Articles
          </NavLink>
        </li>
        <li>
          <NavLink className={getActiveLink} to="/products">
            Products
          </NavLink>
        </li>
        <li>
          <NavLink className={getActiveLink} to="/todos">
            Todos
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;