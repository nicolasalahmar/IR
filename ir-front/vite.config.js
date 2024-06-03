// @Vite-Core
import { defineConfig } from "vite";

// @Plugins
import react from "@vitejs/plugin-react";
import tailwindcss from "tailwindcss";

// @Third-Party
import * as path from "path";

// https://vitejs.dev/config/
export default defineConfig(({ command }) => {
  const config = {
    plugins: [react()],
    css: {
      postcss: {
        plugins: [tailwindcss()],
      },
    },
    base: "/",
    server: {
      open: true,
    },
    resolve: {
      alias: [{ find: "@", replacement: path.resolve(__dirname, "./src/lib") }],
    },
  };

  if (command !== "serve") {
    config.base = "/";
  }

  return config;
});
