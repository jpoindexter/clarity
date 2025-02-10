import psycopg2

DATABASE_URL = "postgresql://jpoindexter:dontforgetme@localhost:5432/ai_news_db"

def get_db_connection():
    """Establish database connection"""
    return psycopg2.connect(DATABASE_URL)

def create_rss_table():
    """Ensure the RSS feed table exists"""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rss_feeds (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    url TEXT NOT NULL UNIQUE,
                    category VARCHAR(100),
                    language VARCHAR(50),
                    region VARCHAR(50),
                    source_type VARCHAR(50),
                    author VARCHAR(100),  # New column added
                    active BOOLEAN DEFAULT TRUE
                );
            """)
            conn.commit()

def get_rss_feeds():
    """Retrieve active RSS feeds from the database"""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT name, url, category, language, region, source_type
                FROM rss_feeds WHERE active = TRUE;
            """)
            return [
                {
                    "name": row[0],
                    "url": row[1],
                    "category": row[2],
                    "language": row[3],
                    "region": row[4],
                    "source_type": row[5]
                }
                for row in cursor.fetchall()
            ]

# Run table creation at startup
if __name__ == "__main__":
    create_rss_table()
    print("✅ RSS Table Initialized")
