import { useDispatch } from 'react-redux';
import { logIn } from '../../redux/auth/operations';
import css from './LoginForm.module.css';
import { Formik, Form, Field } from 'formik';
import toast from 'react-hot-toast';

export const LoginForm = () => {
  const dispatch = useDispatch();

  const handleSubmit = (values, { resetForm, setSubmitting }) => {
    dispatch(logIn(values))
      .unwrap()
      .then(() => {
        toast.success('Login successful!');
        resetForm();
      })
      .catch(() => {
        toast.error('Login failed. Please check credentials.');
      })
      .finally(() => {
        setSubmitting(false);
      });
  };

  return (
    <Formik initialValues={{ email: '', password: '' }} onSubmit={handleSubmit}>
      {({ isSubmitting }) => (
        <Form className={css.form} autoComplete="off">
          <label className={css.label}>
            Email
            <Field type="email" name="email" required />
          </label>
          <label className={css.label}>
            Password
            <Field type="password" name="password" required />
          </label>
          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? 'Logging in...' : 'Log In'}
          </button>
        </Form>
      )}
    </Formik>
  );
};