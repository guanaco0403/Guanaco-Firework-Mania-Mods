import argparse
import requests
import os
import zipfile
from github import Github

print(".")
print("\u001B[32m====================================\u001B[0m")
print("  \u001B[36mGuanaco Auto Server Updater V1.5\u001B[0m")
print("\u001B[32m====================================\u001B[0m")

def download_asset(asset, asset_name, github_token):
    print(f'Downloading Asset: {asset_name}...')
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
        print("\u001B[32mDownload Success\u001B[0m")
    else:
        print(f'\u001B[31mFailed to download asset: {response.status_code}\u001B[0m')
        print(response.text)

def extract_zip(file_path):
    print("Extracting Archive...")
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        extract_path = os.path.dirname(os.path.abspath(__file__))
        zip_ref.extractall(extract_path)
        print("\u001B[32mExtraction Success\u001B[0m")
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
        print(f'\u001B[31mError accessing repository: {e}\u001B[0m')
        return

    # Get releases
    try:
        releases = repo.get_releases()
        print(f'Found {releases.totalCount} releases')
    except Exception as e:
        print(f'\u001B[31mError fetching releases: {e}\u001B[0m')
        return

    if releases:
        for release in releases:
            for asset in release.get_assets():
                if 'Linux' in asset.name and asset.name.endswith('.zip'):
                    print(f'Found asset: {asset.name}')
                    download_asset(asset, asset.name, github_token)
                    extract_zip(asset.name)
                    print("\u001B[32m=================================================\u001B[0m")
                    print("  \u001B[36mFireworks Mania Server Successfully Installed\u001B[0m")
                    print("\u001B[32m=================================================\u001B[0m")
                    return
        print("\u001B[31mNo matching asset found.\u001B[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and update Dedicated Server from GitHub')
    parser.add_argument('github_token', type=str, help='Your GitHub access token')
    args = parser.parse_args()

    main(args.github_token)
