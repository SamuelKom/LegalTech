import './App.css';
import AutoTextarea from './components/Input';

function App() {
  return (
    <div className='App'>
      <div className='Header'>
        <div className='Brand'>Bibdate</div>
        Ein LegalTech Hackathon Projekt für Aktualitätsprüfung von Literaturverzeichnissen.
      </div>
      <AutoTextarea/>
      <div className='Footer'>
        <a href='#'>Impressum</a>
      </div>
      <div id="output">
      </div>
    </div>
  );
}

export default App;
