
from github import Github

g = Github("access_token")
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# /repos/{owner}/{repo}/issues
# github.Repository.Repository.get_issues()

# /repos/{owner}/{repo}/commits
# github.Repository.Repository.get_commits()

