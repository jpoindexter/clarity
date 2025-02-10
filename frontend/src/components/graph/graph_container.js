// frontend/components/graph/graph_container.js

import React from 'react';
import ForceGraph from './force_graph'; // changed

const GraphContainer = () => {
  return (
    <div style={containerStyle}>
      <ForceGraph /> {/* changed */}
    </div>
  );
};

const containerStyle = {
  padding: '20px',
  backgroundColor: '#fff',
  borderRadius: '4px',
  boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
};

export default GraphContainer;
