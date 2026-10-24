import { NavLink } from "react-router-dom"
import css from './Navigation.module.css'

const Navigation = () => {
  const getActiveLInk = ({isActive}) => isActive ? css.active : css.link
  return (
    <nav className={css.nav}>
      <NavLink to={"/"} className={getActiveLInk}>Home</NavLink>
      <NavLink to={"/movies"} className={getActiveLInk}>Movies</NavLink>
    </nav>
  )
}

export default Navigation