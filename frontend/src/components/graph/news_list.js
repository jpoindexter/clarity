// news_list.js
import React from 'react';

const NewsList = ({ newsItems }) => {
  return (
    <div>
      <h3>News List</h3>
      <ul>
        {newsItems && newsItems.length > 0 ? (
          newsItems.map((newsItem, index) => (
            <li key={index}>
              <h4>{newsItem.title}</h4>
              <p>{newsItem.description}</p>
            </li>
          ))
        ) : (
          <p>No news available.</p>
        )}
      </ul>
    </div>
  );
};

export default NewsList;
