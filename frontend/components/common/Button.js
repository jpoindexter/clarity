// frontend/src/components/common/Button.js

import React from 'react';

const Button = ({ label, onClick, style }) => {
  return (
    <button onClick={onClick} style={{ ...defaultStyle, ...style }}>
      {label}
    </button>
  );
};

const defaultStyle = {
  padding: '10px 20px',
  backgroundColor: '#007BFF',
  color: '#fff',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',
};

export default Button;
