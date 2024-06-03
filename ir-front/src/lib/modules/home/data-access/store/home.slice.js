//@Third Party
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  selectedDataSet: null,
};

export const homeSlice = createSlice({
  name: "home",
  initialState: initialState,
  reducers: {
    setSelectedDataSetRed: (state, action) => {
      state.selectedDataSet = action.payload.selectedDataSet;
    },
  },
  selectors: {
    selectSelectedDataSet: (sliceState) => sliceState.selectedDataSet,
  },
});

export const { setSelectedDataSetRed } = homeSlice.actions;
export const { selectSelectedDataSet } = homeSlice.selectors;
export default homeSlice.reducer;
