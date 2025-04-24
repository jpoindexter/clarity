'use client'

import { useEffect, useState } from 'react'
import { useSearchParams, useRouter } from 'next/navigation'

type Article = {
  title: string
  summary: string
  date: string
  source: string
  tone?: string
  manipulation_risk?: number
}

const TONES = ['neutral', 'cautious', 'urgent']
const SOURCES = ['TechNews', 'EarthDaily', 'MarketWatch']
const PAGE_SIZE = 3

export default function ResultsPage() {
  const searchParams = useSearchParams()
  const router = useRouter()

  const [articles, setArticles] = useState<Article[]>([])
  const [loading, setLoading] = useState(true)
  const [page, setPage] = useState(0)
  const [totalCount, setTotalCount] = useState(0)
  const [sort, setSort] = useState(searchParams.get('sort') || 'desc')

  const query = searchParams.get('query') || ''
  const tone = searchParams.get('tone') || ''
  const source = searchParams.get('source') || ''

  useEffect(() => {
    const fetchArticles = async () => {
      setLoading(true)
      const params = new URLSearchParams({
        query,
        limit: PAGE_SIZE.toString(),
        offset: (page * PAGE_SIZE).toString(),
      })
      if (tone) params.append('tone', tone)
      if (source) params.append('source', source)
      if (sort) params.append('sort', sort)

      try {
        const res = await fetch(`/articles?${params.toString()}`)
        const data = await res.json()
        setArticles(data.articles)
        setTotalCount(data.total_count || 0)
      } catch (err) {
        console.error('Failed to fetch articles', err)
      } finally {
        setLoading(false)
      }
    }

    fetchArticles()
  }, [query, tone, source, page, sort])

  const updateFilter = (key: string, value: string) => {
    const newParams = new URLSearchParams(window.location.search)
    if (value) newParams.set(key, value)
    else newParams.delete(key)
    router.push(`/results?${newParams.toString()}`)
  }

  if (loading) return <div className="p-8 text-gray-600">Loading...</div>

  return (
    <div className="p-8 space-y-6 text-gray-900">
      <div className="flex items-center space-x-4 mb-4">
        <select
          value={tone}
          onChange={(e) => updateFilter('tone', e.target.value)}
          className="border px-2 py-1 rounded text-sm"
        >
          <option value="">All Tones</option>
          {TONES.map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <select
          value={source}
          onChange={(e) => updateFilter('source', e.target.value)}
          className="border px-2 py-1 rounded text-sm"
        >
          <option value="">All Sources</option>
          {SOURCES.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
        <select
          value={sort}
          onChange={(e) => {
            setSort(e.target.value)
            updateFilter('sort', e.target.value)
          }}
          className="border px-2 py-1 rounded text-sm"
        >
          <option value="desc">Newest</option>
          <option value="asc">Oldest</option>
          <option value="risk">Risk Score</option>
        </select>
      </div>

      {articles.length === 0 ? (
        <div>No results found.</div>
      ) : (
        <>
          <div className="text-sm text-gray-500">
            Showing {page * PAGE_SIZE + 1}–{Math.min((page + 1) * PAGE_SIZE, totalCount)} of {totalCount} results
          </div>
          {articles.map((article, index) => (
            <div key={index} className="border p-4 rounded shadow-sm bg-white">
              <h2 className="text-lg font-semibold">{article.title}</h2>
              <p className="mt-2 text-sm text-gray-700">{article.summary}</p>
              <div className="mt-4 text-xs text-gray-500 space-x-4">
                <span>📅 {new Date(article.date).toLocaleDateString()}</span>
                <span>📰 {article.source}</span>
                {article.tone && <span>🗣️ {article.tone}</span>}
                {article.manipulation_risk !== undefined && (
                  <span>⚠️ Risk: {article.manipulation_risk.toFixed(2)}</span>
                )}
              </div>
            </div>
          ))}

          <div className="flex justify-between mt-6">
            <button
              onClick={() => setPage((p) => Math.max(0, p - 1))}
              disabled={page === 0}
              className="px-3 py-1 text-sm border rounded disabled:opacity-50"
            >
              ⬅ Previous
            </button>
            <button
              onClick={() => setPage((p) => p + 1)}
              disabled={(page + 1) * PAGE_SIZE >= totalCount}
              className="px-3 py-1 text-sm border rounded disabled:opacity-50"
            >
              Next ➡
            </button>
          </div>
        </>
      )}
    </div>
  )
}