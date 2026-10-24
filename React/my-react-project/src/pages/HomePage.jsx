import { useDispatch, useSelector } from "react-redux"
import { decrement, increment } from "../store/counterSlice"
import { language } from "../store/localeSlice"

const HomePage = () => {
  const value = useSelector((state) => state.counter.value)
  const lang = useSelector((state) => state.locale.lang)
  const dispatch = useDispatch()
    
  const handleIncrement = () => {
    dispatch(increment(100));
  }
  
  const handleDecrement = () => {
    dispatch(decrement(100));
  }

  const handleChangeLang = ({ target: { value } }) => {
    dispatch(language(value));
  }
  
  return (
    <div>
      <button onClick={handleIncrement}>Increment</button>
      <h1>{value}</h1>
      <button onClick={handleDecrement}>Decrement</button>
      <br />
      <br />
      <select value={lang} onChange={handleChangeLang}>
        <option value="en">EN</option>
        <option value="ua">UA</option>
      </select>
    </div>
  );
}

export default HomePage