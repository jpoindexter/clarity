#!/bin/bash

# Seed summarized_articles table with test data
echo "🌱 Seeding articles into the database..."
python backend/database/seeds/seed_articles.py
echo "✅ Seeding complete."
