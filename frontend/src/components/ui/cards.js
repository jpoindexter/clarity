// frontend/components/ui/cards.js

import React from 'react';

const Card = ({ title, description, link }) => {
  return (
    <div style={cardStyle}>
      <h3>{title}</h3>
      <p>{description}</p>
      <a href={link}>Read More</a>
    </div>
  );
};

const cardStyle = {
  border: '1px solid #ddd',
  padding: '15px',
  borderRadius: '4px',
  boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  marginBottom: '15px',
};

export default Card;
