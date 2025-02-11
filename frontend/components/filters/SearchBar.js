// frontend/components/filters/date_filter.js

import React, { useState } from 'react';

const DateFilter = () => {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleStartChange = (e) => setStartDate(e.target.value);
  const handleEndChange = (e) => setEndDate(e.target.value);

  return (
    <div style={filterStyle}>
      <label htmlFor="start-date">Start Date</label>
      <input
        type="date"
        id="start-date"
        value={startDate}
        onChange={handleStartChange}
        style={inputStyle}
      />
      <label htmlFor="end-date">End Date</label>
      <input
        type="date"
        id="end-date"
        value={endDate}
        onChange={handleEndChange}
        style={inputStyle}
      />
    </div>
  );
};

const filterStyle = {
  marginBottom: '15px',
};

const inputStyle = {
  padding: '8px',
  marginTop: '5px',
  width: '100%',
  fontSize: '16px',
  border: '1px solid #ccc',
  borderRadius: '4px',
};

export default DateFilter;
