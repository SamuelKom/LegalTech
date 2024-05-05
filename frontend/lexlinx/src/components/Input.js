import React, { useState, useEffect, useRef } from 'react';
import './Input.css';

function AutoresizingTextarea() {
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
    // Simulated API call
    fetch('http://127.0.0.1:5000/check', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ bibliography : text }),
    }).then(response => response.json())
    .then(data => {
      console.log(data);
    }).catch((error) => {
      console.error('Error:', error);
      setLoading(false);
    });
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type='submit' value='Überprüfen' className='Submit-Button' disabled={loading}/>
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
  );
}

export default AutoresizingTextarea;
