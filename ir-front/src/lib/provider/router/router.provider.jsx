// @Third-Party
import { BrowserRouter } from "react-router-dom";

// @Modules
import { RoutesModule } from "./routes.module";

export function RouterProvider() {
  return (
    <BrowserRouter basename={import.meta.env.DEV ? "/" : "/"}>
      <RoutesModule />
    </BrowserRouter>
  );
}
