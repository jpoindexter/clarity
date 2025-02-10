// frontend/components/ui/modals.js

import React from 'react';

const Modal = ({ isOpen, closeModal, content }) => {
  if (!isOpen) return null;

  return (
    <div style={overlayStyle} onClick={closeModal}>
      <div style={modalStyle} onClick={(e) => e.stopPropagation()}>
        <div>{content}</div>
        <button onClick={closeModal} style={buttonStyle}>
          Close
        </button>
      </div>
    </div>
  );
};

const overlayStyle = {
  position: 'fixed',
  top: 0,
  left: 0,
  width: '100%',
  height: '100%',
  backgroundColor: 'rgba(0, 0, 0, 0.5)',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

const modalStyle = {
  backgroundColor: '#fff',
  padding: '20px',
  borderRadius: '4px',
  width: '300px',
  textAlign: 'center',
};

export default Modal;
