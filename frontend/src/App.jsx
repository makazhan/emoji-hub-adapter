import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import EmojiList from "./pages/EmojiList";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/emojis" element={<EmojiList />} />
      </Routes>
    </Router>
  );
}

export default App;
