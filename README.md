# 🧠 LifeOS AI

### Personal Productivity Intelligence System

A modular, AI-powered life management backend that doesn't just store your data — it **thinks about it**. LifeOS AI combines habit streaks, financial discipline, and goal progress into a unified scoring engine with personalized AI-generated daily briefings.

> Built with Django REST Framework · JWT Auth · Service Layer Architecture · Event-Driven Analytics

---

## 🚀 Live Demo

| Endpoint | Description |
|---|---|
| `POST /api/token/` | Get JWT access token |
| `GET /api/analytics_app/dashboard/` | Full productivity dashboard |
| `GET /api/analytics_app/briefing/` | AI daily briefing |
| `POST /api/habits/complete/` | Complete a habit + update streak |
| `POST /api/goals/update/` | Update goal progress |

---

## ✨ Features

### 🎯 Productivity Scoring Engine
A weighted algorithm that synthesizes three life pillars into one score:
```
Overall Score = (Habit Score × 0.4) + (Finance Score × 0.3) + (Goal Score × 0.3)
```

### 🤖 AI Daily Briefing
Personalized recommendations generated per user based on their current scores and recent activity patterns.

### 📊 Event-Driven Activity System
Every meaningful action — habit completed, goal updated, transaction logged — fires an event that feeds the analytics layer and AI engine.

### 🔐 JWT Authentication
Secure token-based auth with access + refresh token flow using SimpleJWT.

### 📈 Real-Time Analytics Dashboard
One API call returns productivity scores, recent activity, and trend data — ready to power any frontend.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                   API Layer                      │
│         (Django REST Framework Views)            │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│                Service Layer                     │
│  productivity_engine  │  recommendation_engine   │
│  activity_feed        │  activity_logger         │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│                  Data Layer                      │
│   Habits │ Goals │ Finance │ Analytics │ Users   │
└─────────────────────────────────────────────────┘
```

### Design Principles
- **Thin Views** — views authenticate, call a service, return a response. Nothing more.
- **Service Layer** — all business logic lives in `services/`, decoupled from the web framework
- **Event-Driven** — every user action logs to a unified activity stream
- **Modular Apps** — each domain (habits, goals, finance) is an independent Django app

---

## 🛠️ Tech Stack

| | Technology |
|---|---|
| **Framework** | Django 4.x + Django REST Framework |
| **Auth** | SimpleJWT (access + refresh tokens) |
| **Database** | SQLite (dev) · PostgreSQL-ready (prod) |
| **AI Layer** | Custom recommendation engine |
| **Language** | Python 3.14 |
| **Frontend** | React Native + Expo *(in progress)* |

---

## 📁 Project Structure

```
lifeos_ai/
├── apps/
│   ├── accounts/           # Custom user model + registration
│   ├── analytics_app/      # Dashboard, scoring APIs, activity feed
│   ├── goals/              # Goal management + progress tracking
│   ├── habits/             # Habit tracking + streak engine
│   └── finance/            # Transaction logging + finance scoring
│
├── services/
│   ├── productivity_engine.py      # Core weighted scoring algorithm
│   ├── recommendation_engine.py    # AI briefing generation
│   ├── activity_feed_service.py    # Unified activity stream builder
│   └── activity_logger.py          # Event logging utility
│
├── core/
│   └── urls.py             # Root URL configuration
│
└── manage.py
```

---

## 📡 Full API Reference

### Authentication
```http
POST /api/token/
Content-Type: application/json

{ "username": "your_username", "password": "your_password" }
```
```json
{ "access": "<token>", "refresh": "<token>" }
```

### Analytics Dashboard
```http
GET /api/analytics_app/dashboard/
Authorization: Bearer <token>
```
```json
{
  "scores": {
    "habit_score": 62.0,
    "finance_score": 95.7,
    "goal_score": 75.0,
    "overall_score": 76.01
  },
  "activities": [
    {
      "event_type": "habit_completed",
      "timestamp": "2026-05-11 09:00:00",
      "metadata": { "habit_name": "Morning Run", "streak": 7 }
    }
  ]
}
```

### Habits
```http
GET  /api/habits/                        # List habits
POST /api/habits/                        # Create habit
POST /api/habits/complete/               # Complete habit + update streak
     Body: { "habit_id": 1 }
```

### Goals
```http
POST /api/goals/update/
     Body: { "goal_id": 1, "progress": 75 }
```

### Finance
```http
POST /api/finance/create/
     Body: { "amount": 500, "category_id": 2, "note": "Groceries" }
```

### Other Analytics
```http
GET /api/analytics_app/score/        # Productivity score only
GET /api/analytics_app/briefing/     # AI daily briefing
GET /api/analytics_app/feed/         # Full activity feed (last 20)
GET /api/analytics_app/live/         # Live activity (last 5 minutes)
```

---

## ⚡ Getting Started

### Prerequisites
- Python 3.10+
- pip

### Setup
```bash
# Clone the repo
git clone https://github.com/MEENAKSHI042004/LIfeOS.git
cd LIfeOS

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### Test the API
```bash
# 1. Get token
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'

# 2. Hit dashboard
curl http://127.0.0.1:8000/api/analytics_app/dashboard/ \
  -H "Authorization: Bearer <your_access_token>"
```

---

## 🗺️ Roadmap

- [x] JWT Authentication
- [x] Productivity Scoring Engine
- [x] Habit Tracking + Streak System
- [x] Goal Progress Tracking
- [x] Finance Transaction Logging
- [x] AI Daily Briefing
- [x] Event-Driven Activity Feed
- [x] Analytics Dashboard API
- [ ] React Native Frontend
- [ ] Celery + Redis for async scoring
- [ ] PostgreSQL for production
- [ ] Deployment on Render
- [ ] Weekly productivity report generation
- [ ] Push notifications for habit reminders

---

## 💡 Engineering Decisions

**Why a service layer?**
Keeps views thin and business logic independently testable. The scoring engine can be unit tested without spinning up a web server.

**Why event-driven activity logging?**
Decouples the analytics layer from individual app logic. Adding a new event type requires zero changes to the analytics system.

**Why JWT over sessions?**
Stateless auth makes the backend ready for React Native and other non-browser clients from day one.

**How would you scale this?**
Move scoring to Celery background tasks, cache dashboard results in Redis, swap SQLite for PostgreSQL, containerize with Docker.

---

## 👩‍💻 Author

**Meenakshi S**

Backend engineering project demonstrating modular Django architecture, AI service integration, and event-driven system design.

[![GitHub](https://img.shields.io/badge/GitHub-MEENAKSHI042004-black?style=flat&logo=github)](https://github.com/MEENAKSHI042004)

---

*LifeOS AI — because your life deserves an intelligent backend.*
