// frontend/components/filters/keyword_filter.js

import React, { useState } from 'react';

const KeywordFilter = () => {
  const [keywords, setKeywords] = useState('');

  const handleChange = (e) => setKeywords(e.target.value);

  return (
    <div style={filterStyle}>
      <label htmlFor="keywords">Keywords</label>
      <input
        type="text"
        id="keywords"
        value={keywords}
        onChange={handleChange}
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
  width: '100%',
  fontSize: '16px',
  border: '1px solid #ccc',
  borderRadius: '4px',
};

export default KeywordFilter;
