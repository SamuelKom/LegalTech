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
      textarea.style.height = 'auto';
      textarea.style.height = `${textarea.scrollHeight}px`;
    }
  }, [text, loading]);

  function handleChange(event) {
    setText(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    // Simulated API call
    // fetch('https://yourapi.com/endpoint', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({ content: text })
    // })
    // .then(response => response.json())
    // .then(data => {
    //   setData(data);
    //   setLoading(false);
    //   setText('');
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    //   setLoading(false);
    // });
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type='submit' value='Suchen' className='Submit-Button' disabled={loading}/>
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
      {loading && <div className='Loading-Indicator'>Loading...</div>}
      {data && (
        <div className='Data-Table'>
          {data.map((item, index) => (
            <div key={index} className='Data-Row'>
              <div className='Data-Cell'>{item}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default AutoresizingTextarea;
