import React from 'react';

const responseStyle = {
  backgroundColor: 'var(--card-input)',
  padding: '1.5rem',
  borderRadius: '0.5rem',
  border: '1px solid var(--primary-button)',
  width: '100%',
  boxSizing: 'border-box',
  whiteSpace: 'pre-wrap', /* To respect newlines in the response */
  color: 'var(--text-primary)',
};

const placeholderStyle = {
  ...responseStyle,
  color: 'var(--text-secondary)',
  textAlign: 'center',
};

const ChatResponse = ({ response, loading, error }) => {
  if (error) {
    return <div style={responseStyle}>Error: Could not fetch response. Please try again.</div>;
  }

  if (loading) {
    return <div style={placeholderStyle}>Thinking...</div>;
  }

  if (!response) {
    return <div style={placeholderStyle}>The AI's response will appear here.</div>;
  }

  return <div style={responseStyle}>{response}</div>;
};

export default ChatResponse;
