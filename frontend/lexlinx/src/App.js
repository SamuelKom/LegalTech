import './App.css';
import AutoTextarea from './components/Input';

function App() {
  return (
    <div className="App">
      <div className="Header">
        Ein LegalTech Hackathon Projekt für Aktualitätsprüfung von Literaturverzeichnissen.
      </div>
      <div className="Input-Container">
        <AutoTextarea/>
      </div>
    </div>
  );
}

export default App;