import requests
import pandas as pd
import re

# Constants
GITHUB_TOKEN = ""
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_users_in_basel():
    users = []
    page = 1
    while True:
        query = "location:Basel followers:>10"
        url = f"https://api.github.com/search/users?q={query}&page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if "items" not in data:
            break
        users.extend(data["items"])
        if len(data["items"]) < 100:
            break
        page += 1
    return users

def clean_company_name(name):
    if not name:
        return ""
    name = name.strip()
    name = re.sub(r'^@', '', name)
    return name.upper()

def get_user_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos

if __name__ == "__main__":
    users = get_users_in_basel()
    user_data = []
    repo_data = []

    for user in users:
        user_details = requests.get(user["url"], headers=HEADERS).json()
        user_data.append({
            "login": user_details.get("login", ""),
            "name": user_details.get("name", ""),
            "company": clean_company_name(user_details.get("company", "")),
            "location": user_details.get("location", ""),
            "email": user_details.get("email", ""),
            "hireable": user_details.get("hireable", False),
            "bio": user_details.get("bio", ""),
            "public_repos": user_details.get("public_repos", 0),
            "followers": user_details.get("followers", 0),
            "following": user_details.get("following", 0),
            "created_at": user_details.get("created_at", "")
        })

        repos = get_user_repos(user_details["login"])
        for repo in repos[:500]:
            repo_data.append({
                "login": user_details["login"],
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": repo.get("has_projects", False),
                "has_wiki": repo.get("has_wiki", False),
                "license_name": repo.get("license").get("key", "") if repo.get("license") else ""
            })

    pd.DataFrame(user_data).to_csv("users.csv", index=False)
    pd.DataFrame(repo_data).to_csv("repositories.csv", index=False)
    print("Data saved to users.csv and repositories.csv")

