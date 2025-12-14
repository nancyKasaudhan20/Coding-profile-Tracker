from fastapi import APIRouter
from app.database.db import run_query
from app.utils.extract import extract_username
from app.services.codeforces import fetch_codeforces_submissions

router = APIRouter()

@router.post("/track")
def track_profiles(payload: dict):
    username = payload.get("username")
    email = payload.get("email")
    # 1️⃣ Create user
    # user = run_query(
    #     "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
    #     (username, email)
    # )
    # user_id = user[0]["id"]
    user_id = 2
    # 2️⃣ Codeforces
    cf_url = payload.get("codeforces_url")
    if cf_url:
        cf_username = extract_username(cf_url)

        platform = run_query(
            "SELECT id FROM platforms WHERE name = %s",
            ("codeforces",)
        )
        platform_id = platform[0]["id"]

        submissions = fetch_codeforces_submissions(cf_username)

        for s in submissions:
            run_query("""
                INSERT INTO submissions
                (user_id, platform_id, problem_name, status, solved_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                user_id,
                platform_id,
                s["problem_name"],
                s["status"],
                s["solved_at"]
            ))

    return {"message": "Profile tracked successfully"}
