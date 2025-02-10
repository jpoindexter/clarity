// frontend/components/ui/inputs.js

import React from 'react';

const Input = ({ placeholder, value, onChange, type = 'text' }) => {
  return (
    <input
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      style={inputStyle}
    />
  );
};

const inputStyle = {
  padding: '10px',
  fontSize: '16px',
  border: '1px solid #ccc',
  borderRadius: '4px',
  width: '100%',
};

export default Input;
