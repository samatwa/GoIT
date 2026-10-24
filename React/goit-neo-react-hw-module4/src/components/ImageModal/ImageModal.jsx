import Modal from "react-modal"
import css from "./ImageModal.module.css"
import { useEffect, useState } from "react";

const ImageModal = ({ image, onClose }) => {
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    if (image) {
      setIsOpen(true);
    }
  }, [image]);

  const handleClose = () => {
    setIsOpen(false);
    onClose();
  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={handleClose}
      className={css.modal}
      overlayClassName={css.overlay}
      contentLabel="Image Modal"
      shouldCloseOnOverlayClick={true}
      shouldCloseOnEsc={true}
    >
      {image && (
        <>
          <img
            src={image.urls?.regular}
            alt={image.alt_description || "Image"}
            className={css.image}
          />
          <p className={css.details}>
            Author: {image.user.name} | ❤️ {image.likes}
          </p>
        </>
      )}
    </Modal>
  );
};

export default ImageModal