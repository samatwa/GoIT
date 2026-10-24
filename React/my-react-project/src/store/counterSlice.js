// import { createAction, createReducer,  } from "@reduxjs/toolkit";
import { createSlice } from "@reduxjs/toolkit";

export const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 1000 },
  reducers: {
    increment: (state, { payload }) => {
      state.value += payload;
    },

    // increment: (state, action) => {
    //   state.value += action.payload;

    // return {
    //   ...state,
    //   value: state.value + action.payload
    // }
    decrement: (state, { payload }) => {
      state.value -= payload;
    },
    // decrement: (state, action) => {
    //   state.value -= action.payload;

    // return {
    //   ...state,
    //   value: state.value - action.payload
    // }
  },
});

export const counterReducer = counterSlice.reducer;
export const { increment, decrement } = counterSlice.actions;

// const initialState = { value: 1000 };

// export const increment = createAction("counter/increment");

// export const increment = (value) => ({
//   payload: value,
//   type: "counter/increment",
// });

// export const decrement = createAction("counter/decrement");

// export const decrement = (value) => ({
//   payload: value,
//   type: "counter/decrement",
// });

// export const counterReducer = createReducer(initialState, (builder) => {
//   builder
//     .addCase(increment, (state, action) => {
//       return {
//         ...state,
//         value: state.value + action.payload,
//       }
//     })
//     .addCase(decrement, (state, action) => {
//       return {
//         ...state,
//         value: state.value - action.payload,
//       }
//     })
// })

// export const counterReducer = (state = initialState, action) => {
//   switch (action.type) {
//     case "counter/increment":
//       return {
//         ...state,
//         value: state.value + action.payload,
//       }

//     case "counter/decrement":
//       return {
//         ...state,
//         value: state.value - action.payload,
//       }

//     default:
//       return state
//   }
// }
