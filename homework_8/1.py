from github import Github

github_token = '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'

g = Github(github_token)

user = g.get_user()

following = user.get_following()

repositories_data = {}

for friend in following:
    friend_name = friend.login
    repositories = friend.get_repos()

    repositories_data[friend_name] = []
    for repo in repositories:
        repo_data = {
            'name': repo.name,
            'description': repo.description,
            'url': repo.html_url,
            'created_at': repo.created_at,
            'updated_at': repo.updated_at,
            'language': repo.language,
            'forks_count': repo.forks_count,
            'stargazers_count': repo.stargazers_count,
        }
        repositories_data[friend_name].append(repo_data)


import json

with open('repositories_data.json', 'w') as file:
    json.dump(repositories_data, file, indent=2)
