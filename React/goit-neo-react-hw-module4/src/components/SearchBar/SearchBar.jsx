import { Formik, Form, Field } from "formik";
import { FaSearch } from "react-icons/fa";
import css from "./SearchBar.module.css";

const SearchBar = ({ onSubmit }) => {
  return (
    <header className={css.searchHeader}>
      <Formik
        initialValues={{ query: "" }}
        onSubmit={(values, { resetForm }) => {
          onSubmit(values.query);
          resetForm();
        }}
      >
        {({ submitForm }) => (
          <Form className={css.searchForm}>
            <FaSearch className={css.searchIcon} onClick={submitForm} />
            <Field
              type="text"
              name="query"
              autoComplete="off"
              autoFocus
              placeholder="Search images and photos"
              className={css.searchInput}
            />
          </Form>
        )}
      </Formik>
    </header>
  );
};

export default SearchBar;