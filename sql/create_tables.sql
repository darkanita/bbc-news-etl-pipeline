CREATE TABLE IF NOT EXISTS {{SCHEMA_NAME}}.news_articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    url TEXT,
    published_at TIMESTAMP,
    scraped_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS {{SCHEMA_NAME}}.etl_logs (
    id SERIAL PRIMARY KEY,
    run_id UUID,
    step VARCHAR(50),
    status VARCHAR(20),
    message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
