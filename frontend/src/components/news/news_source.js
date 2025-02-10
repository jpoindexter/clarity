// frontend/components/news/news_source.js

import React from 'react';

const NewsSource = ({ source }) => {
  return <div style={sourceStyle}>Source: {source}</div>;
};

const sourceStyle = {
  fontSize: '14px',
  color: '#999',
  marginTop: '5px',
};

export default NewsSource;
