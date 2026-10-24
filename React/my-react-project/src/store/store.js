// import { combineReducers } from "redux";
// import { composeWithDevTools } from "@redux-devtools/extension";
// import {createStore} from "redux"
import { counterReducer } from "./counterSlice";
import { localeReducer } from "./localeSlice";
import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { todoReducer } from "./todoSlice";
import {
  persistStore,
  persistReducer,
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from "redux-persist";
import storage from "redux-persist/lib/storage";
import { articlesReducer } from "./articles/articlesSlice";

// const rootReducer = combineReducers({
//   counter: counterReducer,
//   locale: localeReducer,
// })

// const rootReducer ={}
const rootReducer = combineReducers({
  counter: counterReducer,
  locale: localeReducer,
  todos: todoReducer,
  articles: articlesReducer,
})

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

// export const store = createStore(rootReducer, composeWithDevTools());
export const store = configureStore({
  // reducer: rootReducer,
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
});

export const persistor = persistStore(store);