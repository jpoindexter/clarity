import React from 'react';

const NewsTopicTag = ({ topic }) => {
  return <div style={tagStyle}>#{topic}</div>;
};

const tagStyle = {
  backgroundColor: '#007BFF',
  color: '#fff',
  padding: '5px 10px',
  borderRadius: '20px',
  fontSize: '12px',
  marginRight: '5px',
};

export default NewsTopicTag;
