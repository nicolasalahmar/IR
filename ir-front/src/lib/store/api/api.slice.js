import { createApi } from "@reduxjs/toolkit/query/react";
import { baseQuery } from "./base-query";

export const apiSlice = createApi({
  reducerPath: "api",
  baseQuery: baseQuery,
  tagTypes: [""],
  endpoints: (builder) => ({}),
});
