import { Link } from 'react-router-dom';
import css from './NotFoundPage.module.css';

const NotFoundPage = () => {
  return (
    <div className={css.containerNotFound}>
      <h1>404 - Page Not Found</h1>
      <p>Oops! The page you're looking for does not exist. Try again!</p>
      <Link to="/" className={css.homeLink}>
        Go to Home
      </Link>
    </div>
  );
};

export default NotFoundPage;
