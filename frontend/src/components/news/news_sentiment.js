// frontend/components/news/news_sentiment.js

import React from 'react';

const NewsSentiment = ({ sentiment }) => {
  const sentimentStyle = {
    color:
      sentiment === 'positive'
        ? 'green'
        : sentiment === 'negative'
        ? 'red'
        : 'gray',
  };

  return <div style={sentimentStyle}>Sentiment: {sentiment}</div>;
};

export default NewsSentiment;
