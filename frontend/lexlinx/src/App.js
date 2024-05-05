import './App.css';
import AutoTextarea from './components/Input';

function App() {
  return (
    <div className='App'>
      <div className='Header'>
        <div className='Brand'>Ref Reviser</div>
      </div>
      <div className="grid-container">

      <div className="grid-item1"> <AutoTextarea/> </div>

      <div className="grid-item2">
        <div className="Output-Container">
          <div className="Output"></div>
        </div>
      </div>

      </div>
      <div className='Footer'>
        <a href='#'>Impressum</a>
      </div>
    </div>
  );
}

export default App;
