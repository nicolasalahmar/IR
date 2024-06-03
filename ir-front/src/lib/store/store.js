//@Core
import { configureStore } from "@reduxjs/toolkit";

//@Third Party
import { combineReducers } from "@reduxjs/toolkit";

//@Api Slice
import { apiSlice } from "./api/api.slice";
import { homeSlices } from "@/modules/home";

//@Normal Slice

// # Home

const rootReducer = combineReducers({
  //* @API slice
  [apiSlice.reducerPath]: apiSlice.reducer,

  //* @Normal slice
  ...homeSlices,
});

export const makeStore = () => {
  const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware().concat(apiSlice.middleware),
  });

  return { store };
};
