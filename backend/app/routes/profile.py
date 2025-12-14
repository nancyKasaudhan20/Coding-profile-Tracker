from fastapi import APIRouter
from app.database.db import run_query

router = APIRouter()

@router.get("/profile/{username}")
def get_user_profile(username: str):

    # 1️⃣ Get user id
    user = run_query(
        "SELECT id, username FROM users WHERE username = %s",
        (username,)
    )

    if not user:
        return {"error": "User not found"}

    user_id = user[0]["id"]

    # 2️⃣ Get Codeforces platform id
    platform = run_query(
        "SELECT id FROM platforms WHERE name = %s",
        ("codeforces",)
    )

    if not platform:
        return {"error": "Platform not found"}

    platform_id = platform[0]["id"]

    # 3️⃣ Aggregate submissions
    stats = run_query("""
        SELECT 
            COUNT(*) AS total_solved,
            MAX(solved_at) AS last_solved_at
        FROM submissions
        WHERE user_id = %s AND platform_id = %s
    """, (user_id, platform_id))

    return {
        "username": username,
        "platform": "codeforces",
        "total_solved": stats[0]["total_solved"],
        "last_solved_at": stats[0]["last_solved_at"]
    }
