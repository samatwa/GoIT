import { Formik, Form, Field } from 'formik';
import css from './SearchForm.module.css';

const SearchForm = ({ onSubmit }) => {
  return (
    <Formik
      initialValues={{ query: '' }}
      onSubmit={(values, { resetForm }) => {
        if (!values.query.trim()) return;
        onSubmit(values.query);
        resetForm();
      }}
    >
      {() => (
        <Form className={css.form}>
          <Field
            type="text"
            name="query"
            className={css.input}
          />
          <button type="submit" className={css.button}>
            Search
          </button>
        </Form>
      )}
    </Formik>
  );
};

export default SearchForm;