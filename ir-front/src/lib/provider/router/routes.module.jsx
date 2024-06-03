//@Third-Party
import { Routes, Route } from "react-router-dom";

//@Modules

// # Home
import { HomeModule } from "@/modules/home";

// # Search Engine
import { SearchEngineModule } from "@/modules/search-engine";

export function RoutesModule() {
  return (
    <Routes>
      <Route path="/" element={<HomeModule />} />
      <Route path="/search-engine" element={<SearchEngineModule />} />
    </Routes>
  );
}
