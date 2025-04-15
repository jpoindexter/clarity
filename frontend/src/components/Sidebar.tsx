import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="h-screen bg-zinc-950 border-r border-zinc-800 p-4 flex flex-col gap-6">
      <div className="text-lg font-semibold tracking-tight">Clarity</div>
      <nav className="flex flex-col gap-2 text-sm">
        <Link href="/graph" className="hover:text-white text-zinc-400">Semantic Map</Link>
        <Link href="/timeline" className="hover:text-white text-zinc-400">Timeline</Link>
        <Link href="/ingest" className="hover:text-white text-zinc-400">Ingest</Link>
      </nav>
    </aside>
  );
}