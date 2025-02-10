// frontend/src/components/common/Card.js

import React from 'react';

const Card = ({ title, content, style }) => {
  return (
    <div style={{ ...cardStyle, ...style }}>
      <h4>{title}</h4>
      <p>{content}</p>
    </div>
  );
};

const cardStyle = {
  padding: '15px',
  border: '1px solid #ddd',
  borderRadius: '4px',
  backgroundColor: '#fff',
  boxShadow: '0 0 10px rgba(0,0,0,0.1)',
};

export default Card;
