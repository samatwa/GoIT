import TodoItem from "../TodoItem/TodoItem";

const TodoList = ({ items, handleChange, handleRemove }) => {
  return (
    <ul>
      {items.map((item) => (
        <TodoItem
          key={item.id}
          item={item}
          handleChange={handleChange}
          handleRemove={handleRemove}
        />
      ))}
    </ul>
  );
};

export default TodoList;
