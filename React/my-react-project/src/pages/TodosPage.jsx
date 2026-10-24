import { useDispatch, useSelector } from "react-redux";
import TodoList from "../components/TodoList/TodoList";
import CreateTodoForm from "../components/CreateTodoForm/CreateTodoForm";
import { addTodo, changeStatusTodo, removeTodo } from "../store/todoSlice";
import { nanoid } from "@reduxjs/toolkit";

const TodosPage = () => {
  const todos = useSelector((state) => state.todos.todo);
  const dispatch = useDispatch();
  const createTodo = (payload) => {
    const todo = {
      ...payload,
      id: nanoid(),
    };
    dispatch(addTodo(todo));
  };

  const handleRemove = (id) => {
    dispatch(removeTodo(id));
  };

  const handleChange = (id) => {
    dispatch(changeStatusTodo(id));
  };

  return (
    <div>
      <h1>TodosPage</h1>
      <CreateTodoForm submit={createTodo} />
      <hr />
      {todos?.length > 0 ? (
        <TodoList
          items={todos}
          handleRemove={handleRemove}
          handleChange={handleChange}
        />
      ) : (
        <h3>No items...</h3>
      )}
    </div>
  );
};

export default TodosPage;
