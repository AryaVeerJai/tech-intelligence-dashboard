import requests
import matplotlib.pyplot as plt

url = "https://api.github.com/search/repositories?q=stars:>10000&sort=stars"

response = requests.get(url)
data = response.json()

repos = []
stars = []

for repo in data["items"][:10]:
    repos.append(repo["name"])
    stars.append(repo["stargazers_count"])

plt.figure(figsize=(10,6))
plt.barh(repos, stars)

plt.xlabel("Stars")
plt.title("Top Trending GitHub Repositories")

plt.tight_layout()
plt.savefig("assets/github-trends.png")

print("GitHub trends chart updated.")
