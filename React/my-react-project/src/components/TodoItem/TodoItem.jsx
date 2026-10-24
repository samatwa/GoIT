const TodoItem = ({ item, handleChange, handleRemove }) => {
  return (
    <li>
      {item.title}
      <input
        type="checkbox"
        checked={item.completed}
        onChange={() => handleChange(item.id)}
      />
      <button onClick={() => handleRemove(item.id)}>Remove</button>
    </li>
  );
};

export default TodoItem;
