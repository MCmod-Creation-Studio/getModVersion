import requests

def process_json(data):
    result = {}

    for entry in data:
        loaders = entry["loaders"]
        versions = entry["game_versions"]

        for loader in loaders:
            if loader not in result:
                result[loader] = set(versions)
            else:
                result[loader].update(versions)

    for loader, versions in result.items():
        print(f"{loader}: {', '.join(sorted(versions))}")

def get_mod_versions(project_id):
    url = f"https://api.modrinth.com/v2/project/{project_id}/version"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for project_id: {project_id}")
        return None

if __name__ == "__main__":
    project_id = input("Enter the project ID: ")
    data = get_mod_versions(project_id)

    if data:
        process_json(data)
