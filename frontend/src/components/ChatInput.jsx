import React, { useState } from 'react';

const inputStyle = {
  backgroundColor: 'var(--card-input)',
  color: 'var(--text-primary)',
  border: '1px solid var(--text-secondary)',
  borderRadius: '0.5rem',
  padding: '0.75rem 1rem',
  fontSize: '1rem',
  flexGrow: 1,
};

const buttonStyle = {
  backgroundColor: 'var(--primary-button)',
  color: 'var(--text-primary)',
  border: 'none',
  borderRadius: '0.5rem',
  padding: '0.75rem 1.5rem',
  fontSize: '1rem',
  cursor: 'pointer',
  fontWeight: 'bold',
};

const ChatInput = ({ onSend, loading }) => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      onSend(inputValue);
      setInputValue('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '1rem', width: '100%' }}>
      <input
        type="text"
        style={inputStyle}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="What’s the weather of Pune today?"
        disabled={loading}
      />
      <button type="submit" style={buttonStyle} disabled={loading}>
        {loading ? 'Thinking...' : 'Send'}
      </button>
    </form>
  );
};

export default ChatInput;
