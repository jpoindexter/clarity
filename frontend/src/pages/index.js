import React, { useEffect, useState } from 'react';
import Modal from '../components/ui/modals'; // Add this import

export default function Home() {
  const [data, setData] = useState(null);
  const [selectedNews, setSelectedNews] = useState(null); // Add this state
  const [isModalOpen, setIsModalOpen] = useState(false); // Add this state

  useEffect(() => {
    fetch('http://127.0.0.1:8000/fetch')
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const openModal = (newsItem) => {
    setSelectedNews(newsItem);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setSelectedNews(null);
    setIsModalOpen(false);
  };

  return (
    <div>
      <h1>News Aggregator</h1>
      {data ? (
        <div>
          {data.map((newsItem, index) => (
            <div key={index} onClick={() => openModal(newsItem)}>
              <h2>{newsItem.title}</h2>
              <p>{newsItem.description}</p>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading data...</p>
      )}
      <Modal
        isOpen={isModalOpen}
        closeModal={closeModal}
        content={
          selectedNews && (
            <div>
              <h2>{selectedNews.title}</h2>
              <p>{selectedNews.description}</p>
              <p>{selectedNews.content}</p>
            </div>
          )
        }
      />
    </div>
  );
}
