// frontend/components/layout/header.js

import React from 'react';

const Header = () => {
  return (
    <header style={headerStyle}>
      <div style={logoStyle}>Logo</div>
      <input type="text" placeholder="Search..." style={searchInputStyle} />
    </header>
  );
};

const headerStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: '20px',
  backgroundColor: '#f1f1f1',
};

const logoStyle = {
  fontSize: '24px',
  fontWeight: 'bold',
};

const searchInputStyle = {
  padding: '10px',
  fontSize: '16px',
  border: '1px solid #ccc',
  borderRadius: '4px',
  width: '300px',
};

export default Header;
