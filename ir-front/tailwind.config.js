import "@tailwindcss/line-clamp";

/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "node_modules/flowbite-react/lib/esm/**/*.js",
  ],
  darkMode: "selector",
  theme: {
    screens: {
      xl: { max: "1279px" },
      lg: { max: "1023px" },
      md: { max: "768px" },
      sm: { max: "600px" },
      xs: { max: "400px" },
    },
    colors: {
      primary: {
        light: "#3497E8",
        DEFAULT: "#277BC0",
        dark: "#226DAB",
      },
      secondary: {
        light: "#FFF4CF",
        DEFAULT: "#FFCB42",
        dark: "#7A5800",
      },
      error: {
        light: "#EB5757",
        DEFAULT: "#D83232",
        dark: "#E61601",
      },
      gray: {
        light: "#E9E9E9",
        DEFAULT: "#8B8B8B",
      },
      darkGray: {
        light: "#F6F6F6",
        DEFAULT: "#A4A4A4",
        dark: "#4F4F4F",
      },
      black: {
        DEFAULT: "#333333",
      },
      white: {
        DEFAULT: "#FFFFFF",
        dark: "#E4E7E9",
      },
      green: {
        DEFAULT: "#2AA952",
      },
    },
    extend: {},
  },
  plugins: ["@tailwindcss/line-clamp"],
};
