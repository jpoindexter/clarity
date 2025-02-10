// frontend/components/ui/buttons.js

import React from 'react';

const Button = ({ text, onClick, style }) => {
  return (
    <button onClick={onClick} style={{ ...buttonStyle, ...style }}>
      {text}
    </button>
  );
};

const buttonStyle = {
  padding: '10px 20px',
  fontSize: '16px',
  cursor: 'pointer',
  border: 'none',
  backgroundColor: '#007BFF',
  color: '#fff',
  borderRadius: '4px',
};

export default Button;
