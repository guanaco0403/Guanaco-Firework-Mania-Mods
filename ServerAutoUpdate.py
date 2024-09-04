import argparse
import requests
import os
import zipfile
from github import Github

print(" ")
print(" ")
print("\u001B[32m====================================\u001B[0m")
print("  \u001B[36mGuanaco Auto Server Updater V1.5\u001B[0m")
print("\u001B[32m====================================\u001B[0m")
print(" ")

def download_asset(asset, asset_name, github_token):
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/octet-stream'
    }
    response = requests.get(asset.url, headers=headers, stream=True)

    if response.status_code == 200:
        with open(asset_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f'Downloaded: {asset_name}')
    else:
        print(f'Failed to download asset: {response.status_code}')
        print(response.text)

def extract_zip(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        extract_path = os.path.dirname(os.path.abspath(__file__))
        zip_ref.extractall(extract_path)
        print(f'Extracted files to: {extract_path}')

def main(github_token):
    # Initialize Github instance
    g = Github(github_token)
    
    # Print the token and repo details for debugging
    print(f'Using GitHub Token: {github_token[:4]}...{github_token[-4:]}')
    repo_owner = 'Laumania'
    repo_name = 'FireworksMania.DedicatedServer'
    print(f'Repository: {repo_owner}/{repo_name}')

    try:
        # Get the repository
        repo = g.get_repo(f"{repo_owner}/{repo_name}")
        print(f'Accessed repository: {repo.full_name}')
    except Exception as e:
        print(f'Error accessing repository: {e}')
        return

    # Get releases
    try:
        releases = repo.get_releases()
        print(f'Found {releases.totalCount} releases')
    except Exception as e:
        print(f'Error fetching releases: {e}')
        return

    if releases:
        for release in releases:
            for asset in release.get_assets():
                if 'Linux' in asset.name and asset.name.endswith('.zip'):
                    print(f'Found asset: {asset.name}')
                    download_asset(asset, asset.name, github_token)
                    extract_zip(asset.name)
                    print("=========================================")
                    print("  Dedicated Server Successfully Updated")
                    print("=========================================")
                    return
        print('No matching asset found.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and update Dedicated Server from GitHub')
    parser.add_argument('github_token', type=str, help='Your GitHub access token')
    args = parser.parse_args()

    main(args.github_token)
