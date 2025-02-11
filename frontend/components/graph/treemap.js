import React from "react";
import { Treemap, Tooltip, ResponsiveContainer } from "recharts";

const sampleData = [
  { name: "Tech", size: 400, source: "TechCrunch" },
  { name: "Politics", size: 300, source: "BBC" },
  { name: "Health", size: 200, source: "WebMD" },
  { name: "Finance", size: 250, source: "Bloomberg" },
];

const formatData = (data) =>
  data.map((item, index) => ({
    name: item.name,
    size: item.size,
    source: item.source,
    value: item.size, // Required for Recharts
    fill: `hsl(${index * 60}, 70%, 60%)`, // Dynamic color for readability
  }));

const TreemapGraph = ({ data = sampleData }) => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <Treemap
        data={formatData(data)}
        dataKey="size"
        aspectRatio={4 / 3}
        stroke="#fff"
        fill="#F5A"
      >
        <Tooltip formatter={(value, name, props) => [`${props.payload.source}`, name]} />
      </Treemap>
    </ResponsiveContainer>
  );
};

export default TreemapGraph;
