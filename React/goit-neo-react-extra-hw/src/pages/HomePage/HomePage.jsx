import DocumentTitle from '../../components/DocumentTitle';
import css from './HomePage.module.css';

export default function HomePage() {
  return (
    <>
      <DocumentTitle>Home</DocumentTitle>

      <div className={css.container}>
        <h1 className={css.title}>
          Welcome to the Contact Manager{' '}
          <span role="img" aria-label="Greeting icon">
            📞
          </span>
        </h1>
        <h3 className={css.text}>
          Please log in or register to manage your contacts.
        </h3>
      </div>
    </>
  );
}