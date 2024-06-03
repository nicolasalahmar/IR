//@Core
import React from "react";
import ReactDOM from "react-dom/client";

//@APP
import App from "./App.jsx";

//@Global Style
import "./global.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
