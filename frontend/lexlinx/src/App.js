import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Impressum from './pages/Impressum';
import Home from './pages/Home';
import Datenschutz from './pages/Datenschutz';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/impressum" element={<Impressum />} />
        <Route path="/datenschutz" element={<Datenschutz />} />
      </Routes>
    </Router>
  );
}

export default App;
