import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  Button,
} from '@mui/material';

const ConfirmModal = ({ message, onConfirm, onCancel, open }) => {
  return (
    <Dialog
      open={open}
      onClose={onCancel}
      aria-labelledby="confirm-dialog"
      aria-describedby="confirm-dialog-description"
    >
      <DialogContent>
        <DialogContentText
          id="confirm-dialog-description"
          sx={{
            fontSize: '18px',
            fontWeight: 'bold',
            color: '#333',
          }}
        >
          {message}
        </DialogContentText>
      </DialogContent>
      <DialogActions
        sx={{
          display: 'flex',
          justifyContent: 'center',
          mb: 2,
          gap: 2,
        }}
      >
        <Button
          onClick={onConfirm}
          variant="contained"
          sx={{
            backgroundColor: '#9e9e9e',
            color: 'black',
            '&:hover': {
              backgroundColor: 'red',
            },
          }}
        >
          Yes
        </Button>
        <Button
          onClick={onCancel}
          variant="contained"
          sx={{
            backgroundColor: '#9e9e9e',
            color: 'black',
            '&:hover': {
              backgroundColor: 'red',
            },
          }}
        >
          No
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default ConfirmModal;