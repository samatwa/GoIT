import { useDispatch, useSelector } from 'react-redux';
import Contact from '../Contact/Contact';
import css from './ContactList.module.css';
import { deleteContact } from '../../redux/contacts/operations';
import { selectError, selectFilteredContacts, selectLoading } from '../../redux/contacts/selectors';

const ContactList = () => {
  const contacts = useSelector(selectFilteredContacts);
  const loading = useSelector(selectLoading);
  const error = useSelector(selectError);
  const dispatch = useDispatch();

  return (
    <div className={css.contactList}>
      {loading && <p className={css.loadingText}>Loading...</p>}

      {!loading && error && <p className={css.errorText}>Error: {error}</p>}

      {!loading &&
        !error &&
        (contacts.length > 0 ? (
          contacts.map(contact => (
            <Contact
              key={contact.id}
              id={contact.id}
              name={contact.name}
              number={contact.number}
              onDelete={() => dispatch(deleteContact(contact.id))}
            />
          ))
        ) : (
          <p className={css.noContacts}>No contacts found</p>
        ))}
    </div>
  );
};

export default ContactList;
