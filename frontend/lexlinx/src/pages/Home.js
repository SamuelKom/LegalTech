import React, { useState, useEffect, useRef } from 'react';
import './styles/Home.css';

function Home() {
  const [text, setText] = useState('');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const textareaRef = useRef(null);

  useEffect(() => {
    if (!loading) {
      const textarea = textareaRef.current;
      // textarea.style.height = 'auto';
      // textarea.style.height = `${textarea.scrollHeight}px`;
    }
  }, [text, loading]);

  function handleChange(event) {
    setText(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    fetch('http://127.0.0.1:5000/check', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ bibliography: text }),
    })
      .then(response => response.json())
      .then(data => {
        setData(data.response); // Assuming the response is an array with { book, result }
        setLoading(false);
      })
      .catch(error => {
        console.error('Error:', error);
        setLoading(false);
      });
  }
  

  function getResultStyle(code) {
    if (code === 1) {
      return { backgroundColor: 'red', color: 'black' };
    } else if (code === 2) {
      return { backgroundColor: 'green', color: 'black' };
    } else {
      return { backgroundColor: 'blue', color: 'black' };
    }
  }

  return (
    <div className='App'>
      <div className='Header'>
        <div className='Brand'>Ref Reviser<img src="logo.png" alt="logo"/></div>
      </div>
      <div className="grid-container">
        <div className="grid-item1">
          <div>
            <form onSubmit={handleSubmit}>
              <input type='submit' value='Überprüfen' className='Submit-Button' disabled={loading} />
              <div className='Input-Container'>
                <textarea
                  ref={textareaRef}
                  value={text}
                  onChange={handleChange}
                  autoFocus
                  placeholder='Literaturverzeichnis einfügen...'
                  className='Input'
                  disabled={loading}
                />
              </div>
            </form>
            {loading && <div className="Loading-Indicator">Loading...</div>}
            {data && <div>
              {data.map((item, index) => (
                <div key={index}>
                  <p>{item.title}</p>
                </div>
              ))}
            </div>}
          </div>
        </div>

        <div className="grid-item2">
        <div className="Output-Container">
        {data && (
          <div>
            {data.map((item, index) => (
              <p key={index} style={getResultStyle(item.code)}>
                {item.book}: {item.result}
              </p>
            ))}
          </div>
        )}
      </div>
        </div>
      </div>
      <div className='Footer'>
        <p>Copyright © 2024 Ref Reviser</p>
        <div>
          <a href='/impressum'>Impressum</a>
          |
          <a href='/datenschutz'>Datenschutzerklärung</a>
        </div>
      </div>
    </div>
  );
};

export default Home;
