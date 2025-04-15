"use client";

import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

type Article = {
  title: string;
  url: string;
  summary: string;
  tags?: string[];
};

export default function IngestForm() {
  const [input, setInput] = useState("");
  const [source, setSource] = useState<"url" | "rss">("url");
  const [results, setResults] = useState<Article[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setResults([]);

    try {
      const res = await fetch("/api/articles/ingest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input, source }),
      });

      if (!res.ok) throw new Error("Ingest failed");

      const data = await res.json();
      setResults(data);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Unknown error");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl space-y-6">
      <div className="space-y-2">
        <Label htmlFor="input">Paste a URL or RSS feed</Label>
        <Input id="input" value={input} onChange={(e) => setInput(e.target.value)} />
      </div>

      <div className="space-y-2">
        <Label>Choose source type</Label>
        <Select value={source} onValueChange={(val) => setSource(val as "url" | "rss")}>
          <SelectTrigger>
            <SelectValue placeholder="Source type" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="url">URL</SelectItem>
            <SelectItem value="rss">RSS Feed</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <Button onClick={handleSubmit} disabled={loading}>
        {loading ? "Ingesting..." : "Ingest"}
      </Button>

      {error && <p className="text-red-500">{error}</p>}

      {results.length > 0 && (
        <div className="space-y-4">
          {results.map((article, idx) => (
            <Card key={idx}>
              <CardContent className="space-y-2 p-4">
                <div className="text-lg font-semibold">{article.title}</div>
                <div className="text-sm text-zinc-400">{article.url}</div>
                <p className="text-sm">{article.summary}</p>
                {article.tags && (
                  <div className="flex flex-wrap gap-2 text-xs text-zinc-400">
                    {article.tags.map((tag, i) => (
                      <span key={i} className="border px-2 py-0.5 rounded border-zinc-700 bg-zinc-900">
                        {tag}
                      </span>
                    ))}
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}