 
 "use client";
 
 import React from "react";
 
 interface TimelineCardProps {
   title: string;
   summary: string;
  tags?: string[] | null;
   time: string;
 }
 
 export default function TimelineCard({ title, summary, tags, time }: TimelineCardProps) {
   return (
     <div className="w-80 bg-card rounded-lg shadow-sm p-4 flex flex-col justify-between">
       <div className="mb-3">
         <h3 className="text-base font-semibold leading-snug line-clamp-2">{title}</h3>
         <p className="text-sm text-muted-foreground mt-1 line-clamp-4">{summary}</p>
       </div>
       <div className="flex flex-wrap gap-1 mb-2">
         {(tags || []).map((tag) => (
           <span
             key={tag}
             className="text-xs bg-muted text-muted-foreground px-2 py-0.5 rounded-md whitespace-nowrap"
           >
             {tag}
           </span>
         ))}
       </div>
       <div className="text-xs text-muted-foreground mt-auto truncate">
         {new Date(time).toLocaleDateString()}
       </div>
     </div>
   );
 }  