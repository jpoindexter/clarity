import { cn } from "@/lib/utils";

type Props = {
  children: React.ReactNode;
  variant?: "default" | "tone" | "danger" | "neutral";
};

export default function Tag({ children, variant = "default" }: Props) {
  const base = "text-xs px-2 py-0.5 rounded border transition";
  const styles = {
    default: "bg-zinc-950 border-zinc-800 text-zinc-400 hover:text-white",
    tone: "bg-indigo-900 border-indigo-700 text-indigo-300",
    danger: "bg-red-900 border-red-700 text-red-300",
    neutral: "bg-zinc-800 border-zinc-600 text-white",
  };

  return <span className={cn(base, styles[variant])}>{children}</span>;
}