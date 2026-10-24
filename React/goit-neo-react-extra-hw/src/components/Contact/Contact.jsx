import { IoCall, IoPerson } from 'react-icons/io5';
import css from './Contact.module.css';
import { useState } from 'react';
import ContactEditor from '../ContactEditor/ContactEditor';
import ConfirmModal from '../ConfirmModal/ConfirmModal';

const Contact = ({ name, number, onDelete, id }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  const handleDelete = () => {
    setShowConfirm(true);
  };

  const confirmDelete = () => {
    onDelete();
    setShowConfirm(false);
  };

  const cancelDelete = () => {
    setShowConfirm(false);
  };

  return (
    <div className={css.contact}>
      <div className={css.contactInfo}>
        <div className={css.contactName}>
          <IoPerson className={css.icon} /> {name}
        </div>
        <div className={css.contactNumber}>
          <IoCall className={css.icon} /> {number}
        </div>
      </div>

      <div className={css.buttons}>
        <button className={css.deleteBtn} onClick={handleDelete}>
          Delete
        </button>
        <button className={css.editBtn} onClick={() => setIsEditing(true)}>
          Edit
        </button>
      </div>

      {isEditing && (
        <ContactEditor
          contact={{ id, name, number }}
          onClose={() => setIsEditing(false)}
        />
      )}

      {showConfirm && (
        <ConfirmModal
          message={`Delete contact "${name}"?`}
          onConfirm={confirmDelete}
          onCancel={cancelDelete}
          open={showConfirm}
        />
      )}
    </div>
  );
};

export default Contact;
