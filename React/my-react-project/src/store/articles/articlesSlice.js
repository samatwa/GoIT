import { createSlice } from "@reduxjs/toolkit";
import { createBook, deleteBook, getBooks } from "./articlesOptions";

const articlesSlice = createSlice({
  name: "books",
  initialState: {
    items: [],
    loading: false,
    error: false,
    errorMessage: "",
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getBooks.fulfilled, (state, { payload }) => {
        state.items = payload;
      })
      .addCase(createBook.fulfilled, (state, { payload }) => {
        state.items.push(payload);
      })
      .addCase(deleteBook.fulfilled, (state, { payload }) => {
        state.items = state.items.filter((el) => el.id !== payload.id);
      })
      .addMatcher(
        ({ type }) => type.endsWith("/pending"),
        (state) => {
          state.error = false;
          state.loading = true;
        }
      )
      .addMatcher(
        ({ type }) => type.endsWith("/rejected"),
        (state) => {
          state.error = true;
          state.loading = false;
        }
      )
      .addMatcher(
        ({ type }) => type.endsWith("/fulfilled"),
        (state) => {
          state.loading = false;
          state.error = false;
        }
      );
    // .addCase(getBooks.pending, (state) => {
    //   state.loading = true;
    //   state.error = false;
    // })
    // .addCase(getBooks.rejected, (state, { payload }) => {
    //   state.error = true;
    //   state.errorMessage = payload;
    //   state.loading = false;
    //   state.items = [];
    // })
    // .addCase(getBooks.rejected, (state, action) => {
    //   state.error = true;
    //   state.loading = false;
    //   state.errorMessage = action.error.message;
    //   state.items = [];
    // })
    // .addCase(createBook.pending, (state) => {
    //   state.loading = true;
    //   state.error = false;
    // })
    // .addCase(createBook.rejected, (state) => {
    //   state.error = true;
    //   state.loading = false;
    //   state.items = [];
    // })
    // .addCase(deleteBook.pending, (state) => {
    //   state.loading = true;
    //   state.error = false;
    // })
    // .addCase(deleteBook.rejected, (state) => {
    //   state.error = true;
    //   state.loading = false;
    //   state.items = [];
    // })
  },
});

export const articlesReducer = articlesSlice.reducer;
