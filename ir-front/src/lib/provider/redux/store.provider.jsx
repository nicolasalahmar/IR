// @Core
import { useRef } from "react";

// @Third-Party
import { Provider } from "react-redux";
import { setupListeners } from "@reduxjs/toolkit/query";

// @Store
import { makeStore } from "@/store/store.js";

export function StoreProvider({ children }) {
  const storeRef = useRef();

  if (!storeRef.current) {
    storeRef.current = makeStore();
    setupListeners(storeRef.current.store.dispatch);
  }

  return <Provider store={storeRef.current.store}>{children}</Provider>;
}
