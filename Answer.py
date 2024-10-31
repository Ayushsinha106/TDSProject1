import pandas as pd
import statsmodels.api as sm
from collections import Counter

users_df = pd.read_csv("users.csv")
repos_df = pd.read_csv("repositories.csv")


# top_users_df = users_df.sort_values(by="followers", ascending=False).head(5)
# top_users_logins = ", ".join(top_users_df["login"])
# print("Top 5 users by followers:", top_users_logins)

users_df['created_at'] = pd.to_datetime(users_df['created_at'])
earliest_users_df = users_df.sort_values(by="created_at", ascending=True)
earliest_users_logins = ", ".join(earliest_users_df["login"].head(5))
print(earliest_users_df)
pd.DataFrame(earliest_users_df).to_csv("earliest_user.csv", index=False)
print("5 earliest registered users:", earliest_users_logins)

# repos_with_license = repos_df[repos_df["license_name"].notna() & (repos_df["license_name"] != "")]
# top_licenses = repos_with_license["license_name"].value_counts().head(3)
# top_licenses_names = ", ".join(top_licenses.index)
# print("3 most popular licenses:", top_licenses_names)

# users_with_company = users_df[users_df["company"].notna() & (users_df["company"] != "")]
# most_common_company = users_with_company["company"].value_counts().idxmax()
# print("Company with the most developers:", most_common_company)

# repos_with_language = repos_df[repos_df["language"].notna() & (repos_df["language"] != "")]
# most_common_language = repos_with_language["language"].value_counts().idxmax()
# print("Most popular programming language:", most_common_language)

# users_df["created_at"] = pd.to_datetime(users_df["created_at"])
# recent_users = users_df[users_df["created_at"].dt.year > 2020]
# recent_user_repos = repos_df[repos_df["login"].isin(recent_users["login"])]
# recent_user_repos_with_language = recent_user_repos[recent_user_repos["language"].notna() & (recent_user_repos["language"] != "")]
# language_counts = recent_user_repos_with_language["language"].value_counts()
# print(language_counts)

# repos_with_language = repos_df[repos_df["language"].notna() & (repos_df["language"] != "")]
# repos_with_language = repos_with_language[repos_with_language["stargazers_count"].notna()]
# avg_stars_per_language = repos_with_language.groupby("language")["stargazers_count"].mean()
# most_popular_language_by_stars = avg_stars_per_language.idxmax()
# highest_avg_stars = avg_stars_per_language.max()
# print("Language with the highest average stars per repository:", most_popular_language_by_stars)
# print("Average stars:", highest_avg_stars)

# users_df["leader_strength"] = users_df["followers"] / (1 + users_df["following"])
# top_leaders = users_df.sort_values(by="leader_strength", ascending=False).head(5)
# print(top_leaders)

# correlation = users_df["followers"].corr(users_df["public_repos"])
# print("Correlation between followers and public repositories:", round(correlation, 3))

# X = users_df["public_repos"]
# y = users_df["followers"]
# X = sm.add_constant(X)
# model = sm.OLS(y, X).fit()
# slope = model.params["public_repos"]
# print("Regression slope of followers on public repositories:", round(slope, 3))

# repos_df['has_projects'] = repos_df['has_projects'].astype(int)  
# repos_df['has_wiki'] = repos_df['has_wiki'].astype(int)          
# correlation = repos_df['has_wiki'].corr(repos_df['has_projects'])
# print(correlation)

# hireable_avg_following = users_df[users_df["hireable"] == True]["following"]
# non_hireable_avg_following = users_df[users_df["hireable"] != True]["following"]
# print(hireable_avg_following.head(5))
# print(non_hireable_avg_following.sum())
# hTotal =67
# nhTotal = 283  
# print(hireable_avg_following.mean() - non_hireable_avg_following.mean())

# users_df['bio_word_count'] = users_df['bio'].apply(lambda x: len(str(x).split()) if pd.notna(x) and str(x).strip() != '' else 0)
# filtered_users = users_df[users_df['bio_word_count'] > 0]
# X = filtered_users['bio_word_count']
# y = filtered_users['followers']
# X = sm.add_constant(X)
# model = sm.OLS(y, X).fit()
# slope = model.params['bio_word_count']
# print("Regression slope of followers on bio word count:", round(slope, 3))

# repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])
# weekend_repos = repos_df[repos_df['created_at'].dt.dayofweek >= 5]
# user_repo_counts = weekend_repos['login'].value_counts()
# top_users = user_repo_counts.head(5).index.tolist()
# print("Top 5 users who created the most repositories on weekends:", ','.join(top_users))

# hireable_with_email = users_df[users_df["hireable"] == True]["email"].notna().sum()
# total_hireable = users_df[users_df["hireable"] == True]["email"].shape[0]
# fraction_hireable = hireable_with_email / total_hireable
# print(hireable_with_email, total_hireable, fraction_hireable)
# non_hireable_with_email = users_df[users_df["hireable"] != True]["email"].notna().sum()
# total_non_hireable = users_df[users_df["hireable"] != True]["email"].shape[0]
# fraction_non_hireable = non_hireable_with_email / total_non_hireable 
# print(non_hireable_with_email, total_non_hireable, fraction_non_hireable)
# email_fraction_difference = fraction_hireable - fraction_non_hireable
# print("Fraction of users with email (hireable - non-hireable):", round(email_fraction_difference, 3))

# users_df['surname'] = users_df['name'].dropna().apply(lambda x: str(x).strip().split()[-1])
# surname_counts = Counter(users_df['surname'].dropna())
# most_common_count = max(surname_counts.values())
# most_common_surnames = [surname for surname, count in surname_counts.items() if count == most_common_count]
# most_common_surnames.sort()
# print(','.join(most_common_surnames))
