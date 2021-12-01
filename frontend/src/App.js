import logo from './logo.svg';
import './App.css';
import Story from './components/Story'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Story />
      </header>
    </div>
  );
}

export default App;
