import React, { useState, useEffect, useRef } from 'react';
import './Input.css';

function AutoresizingTextarea() {
  const [text, setText] = useState('');
  const textareaRef = useRef(null);

  useEffect(() => {
    const textarea = textareaRef.current;
    textarea.style.height = 'auto';  // Reset the height
    textarea.style.height = `${textarea.scrollHeight}px`; // Adjust the height based on the content
  }, [text]);  // Effect runs when text changes

  function handleChange(event) {
    setText(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    console.log(text)
    // fetch('https://yourapi.com/endpoint', { // Your API endpoint URL
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify({ content: text })
    // })
    // .then(response => response.json())
    // .then(data => {
    //   console.log('Success:', data);
    //   // Handle success here, e.g., showing a confirmation message
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    //   // Handle errors here, e.g., showing an error message
    // });
  }

  return (
    <form onSubmit={handleSubmit}>
        <div className='Input-Container'>
            <textarea
            ref={textareaRef}
            value={text}
            onChange={handleChange}
            autoFocus
            placeholder='Literaturverzeichnis einfügen...'
            className='Input'
            />
        </div>
        <input type='submit' value='Suchen' className='Submit-Button'/>
    </form>
  );
}

export default AutoresizingTextarea;
