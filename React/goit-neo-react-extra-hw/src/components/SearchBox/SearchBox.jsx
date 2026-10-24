import { useDispatch, useSelector } from 'react-redux';
import css from './SearchBox.module.css';
import { selectNameFilter } from '../../redux/filters/selectors';
import { changeFilter } from '../../redux/filters/slice';
import { TextField } from '@mui/material';

const SearchBox = () => {
  const filter = useSelector(selectNameFilter);
  const dispatch = useDispatch();

  return (
    <div className={css.searchBox}>
      <TextField
        label="Find contacts by name"
        variant="outlined"
        size="small"
        value={filter}
        onChange={e => dispatch(changeFilter(e.target.value))}
        className={css.inputField}
      />
    </div>
  );
};

export default SearchBox;
