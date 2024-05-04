import React, { useState, useEffect, useRef } from 'react';

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

  return (
    <textarea
      ref={textareaRef}
      value={text}
      onChange={handleChange}
      autoFocus
      placeholder='Literaturverzeichnis einfügen...'
      style={{
        minHeight: '15rem',
        width: '50rem',
        maxHeight: '30rem',
        overflow: 'auto',
        resize: 'none'
      }}
    />
  );
}

export default AutoresizingTextarea;
