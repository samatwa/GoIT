import { Field, Form, Formik } from "formik";
import { useId } from "react";

const CreateArticlesForm = ({ submit }) => {
  const titleID = useId();
  const handleSubmit = (values, actions) => {
    submit(values);
    actions.resetForm();
  };

  return (
    <Formik initialValues={{ title: "" }} onSubmit={handleSubmit}>
      <Form>
        <label htmlFor={titleID}>Title: </label>
        <Field type="text" name="title" id={titleID} />
        <br />
        <button type="submit">Create</button>
      </Form>
    </Formik>
  );
};

export default CreateArticlesForm;
