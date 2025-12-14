import requests
from datetime import datetime

def fetch_codeforces_submissions(username):
    url = f"https://codeforces.com/api/user.status?handle={username}"
    response = requests.get(url).json()

    if response["status"] != "OK":
        return []

    submissions = []

    for s in response["result"]:
        if s.get("verdict") == "OK":
            submissions.append({
                "problem_name": s["problem"]["name"],
                "status": "AC",
                "solved_at": datetime.fromtimestamp(s["creationTimeSeconds"])
            })

    return submissions
