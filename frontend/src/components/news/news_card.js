// frontend/components/news/news_card.js

import React from 'react';
import Card from '../ui/cards';

const NewsCard = ({ title, description, source, link }) => {
  return <Card title={title} description={description} link={link} />;
};

export default NewsCard;
