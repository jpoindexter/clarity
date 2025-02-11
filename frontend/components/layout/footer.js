// frontend/components/layout/footer.js

import React from 'react';

const Footer = () => {
  return (
    <footer style={footerStyle}>
      <p>&copy; 2025 Your Company</p>
      <div>
        <a href="/privacy-policy">Privacy Policy</a> |{' '}
        <a href="/terms">Terms of Service</a>
      </div>
    </footer>
  );
};

const footerStyle = {
  padding: '10px',
  backgroundColor: '#f1f1f1',
  textAlign: 'center',
};

export default Footer;
