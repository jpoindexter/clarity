import React from 'react';

const NewsSummary = ({ summary }) => {
  return <div style={summaryStyle}>{summary}</div>;
};

const summaryStyle = {
  fontStyle: 'italic',
  color: '#555',
  marginTop: '10px',
};

export default NewsSummary;
