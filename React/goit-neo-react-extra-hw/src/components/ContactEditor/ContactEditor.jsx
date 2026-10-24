import { useDispatch } from 'react-redux';
import { updateContact } from '../../redux/contacts/operations';
import css from './ContactEditor.module.css';

export const ContactEditor = ({ contact,  onClose }) => {
  const dispatch = useDispatch();

  const handleSubmit = e => {
    e.preventDefault();
    const form = e.currentTarget;
    const name = form.elements.name.value.trim();
    const number = form.elements.number.value.trim();

    if (name === '' || number === '') {
      alert('Both fields are required!');
      return;
    }

    dispatch(
      updateContact({
        id: contact.id,
        updatedData: { name, number },
      })
    )
      .unwrap()
      .then(() => {
        onClose();
      })
      .catch(() => {
        alert('Failed to update contact');
      });

    form.reset();
  };

  return (
    <form className={css.form} onSubmit={handleSubmit}>
      <label className={css.label}>
        Name:
        <input
          type="text"
          name="name"
          defaultValue={contact.name}
          className={css.input}
        />
      </label>
      <label className={css.label}>
        Phone:
        <input
          type="text"
          name="number"
          defaultValue={contact.number}
          className={css.input}
        />
      </label>
      <div className={css.buttons}>
        <button type="submit" className={css.button}>
          Save
        </button>
        <button type="button" onClick={onClose} className={css.button}>
          Cancel
        </button>
      </div>
    </form>
  );
};

export default ContactEditor;