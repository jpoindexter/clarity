// frontend/components/filters/source_filter.js

import React, { useState } from 'react';

const SourceFilter = () => {
  const [selectedSource, setSelectedSource] = useState('');

  const handleChange = (e) => {
    setSelectedSource(e.target.value);
  };

  return (
    <div style={filterStyle}>
      <label htmlFor="source">Source</label>
      <select
        id="source"
        value={selectedSource}
        onChange={handleChange}
        style={selectStyle}
      >
        <option value="">All Sources</option>
        <option value="source1">Source 1</option>
        <option value="source2">Source 2</option>
        <option value="source3">Source 3</option>
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

export default SourceFilter;
