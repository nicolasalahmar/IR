// @Providers
import { StoreProvider } from "./redux/store.provider";
import { RouterProvider } from "./router/router.provider";
import { ToastProvider } from "./toast/toast.provider";

export function RootProvider() {
  return (
    <StoreProvider>
      <ToastProvider />
      <RouterProvider />
    </StoreProvider>
  );
}
