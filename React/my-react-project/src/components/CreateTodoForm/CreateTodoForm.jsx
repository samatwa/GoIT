import { Field, Form, Formik } from "formik";
import { useId } from "react";

const CreateTodoForm = ({ submit }) => {
  const titleID = useId();
  const completedID = useId();
  const handleSubmit = (values, actions) => {
    submit(values);
    actions.resetForm();
  };

  return (
    <Formik
      initialValues={{ title: "", completed: false }}
      onSubmit={handleSubmit}
    >
      <Form>
        <label htmlFor={titleID}>Title: </label>
        <Field type="text" name="title" id={titleID} />
        <br />
        <label htmlFor={completedID}>Is completed? </label>
        <Field type="checkbox" name="completed" id={completedID} />
        <button type="submit">Create</button>
      </Form>
    </Formik>
  );
};

export default CreateTodoForm;
