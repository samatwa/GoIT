import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

axios.defaults.baseURL = "https://676a8938863eaa5ac0debe88.mockapi.io/";

// export const getBooks = createAsyncThunk(
//   "books/getBooks",
//   async (_, thunkAPI) => {
//     try {
//       const { data } = await axios("books122");
//       return data;
//     } catch (error) {
//       console.log("error", error);
//       // return thunkAPI.rejectWithValue(error.response.data);
//       return thunkAPI.rejectWithValue(error.message);
//     }
//   }
// );

export const getBooks = createAsyncThunk("books/getBooks", async () => {
  const { data } = await axios("books");
  return data;
});

export const createBook = createAsyncThunk("books/createBook", async (body) => {
  const { data } = await axios.post("books", body);
  return data;
});

export const deleteBook = createAsyncThunk("books/deleteBook", async (id) => {
  const { data } = await axios.delete(`books/${id}`);
  return data;
});