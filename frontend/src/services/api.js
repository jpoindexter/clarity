const API_BASE_URL = "http://127.0.0.1:8000/api";

export async function fetchNews() {
  const response = await fetch(`${API_BASE_URL}/news/`);
  if (!response.ok) {
    throw new Error("Failed to fetch news");
  }
  return response.json();
}
