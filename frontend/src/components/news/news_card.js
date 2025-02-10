import React from 'react';
import Card from '../common/Card';

const NewsCard = ({ title, description, source, link }) => {
  return <Card title={title} content={description} />;
};

export default NewsCard;
