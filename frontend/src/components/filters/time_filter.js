// frontend/components/filters/time_filter.js

import React, { useState } from 'react';

const TimeFilter = () => {
  const [selectedTime, setSelectedTime] = useState('');

  const handleChange = (e) => {
    setSelectedTime(e.target.value);
  };

  return (
    <div style={filterStyle}>
      <label htmlFor="time">Time</label>
      <select
        id="time"
        value={selectedTime}
        onChange={handleChange}
        style={selectStyle}
      >
        <option value="">All Times</option>
        <option value="last-24-hours">Last 24 Hours</option>
        <option value="last-week">Last Week</option>
        <option value="last-month">Last Month</option>
      </select>
    </div>
  );
};

const filterStyle = {
  marginBottom: '15px',
};

const selectStyle = {
  padding: '8px',
  width: '100%',
  fontSize: '16px',
  border: '1px solid #ccc',
  borderRadius: '4px',
};

export default TimeFilter;
