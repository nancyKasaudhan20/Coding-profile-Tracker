# Coding-profile-Tracker
# Coding Profile Tracker

A unified platform to aggregate and analyze coding activity across
multiple competitive programming platforms like LeetCode, Codeforces,
and GeeksforGeeks in one place.

## Problem Statement
Developers solve problems across multiple platforms, but there is no
single place to track overall progress, consistency, and topic-wise
strengths. This project aims to solve that.

## Architecture Overview
- Frontend: Next.js dashboard
- Backend: FastAPI REST APIs
- Data Collection: Platform-specific fetchers (GraphQL, REST, Scraping)
- Database: PostgreSQL (time-series snapshots)
- Background Jobs: Scheduled sync workers

## Tech Stack
- Frontend: Next.js, Tailwind CSS
- Backend: FastAPI, SQLAlchemy
- Database: PostgreSQL
- Cache / Queue (future): Redis
