import requests
from typing import List, Optional
import os


def process_file(url: str) -> Optional[List[str]]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return [f"  - '{line.strip()}'" for line in response.text.splitlines()
                if line.strip() and not line.strip().startswith('#')]
    except requests.RequestException:
        return None


def write_to_file(filename: str, processed_content: List[str]) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("payload:\n")
        file.writelines(f"{line}\n" for line in processed_content)


def main():
    urls = {
        "reject": ("https://ruleset.skk.moe/Clash/domainset/reject.txt", "./Clash/domainset/reject.yaml"),
        "cdn": ("https://ruleset.skk.moe/Clash/domainset/cdn.txt", "./Clash/domainset/cdn.yaml"),
        "apple_cdn": ("https://ruleset.skk.moe/Clash/domainset/apple_cdn.txt", "./Clash/domainset/apple_cdn.yaml"),
        "download": ("https://ruleset.skk.moe/Clash/domainset/download.txt", "./Clash/domainset/download.yaml"),
        "downloadip": ("https://ruleset.skk.moe/Clash/non_ip/download.txt", "./Clash/non_ip/download.yaml"),
        "china_ip": ("https://ruleset.skk.moe/Clash/ip/china_ip.txt", "./Clash/ip/china_ip.yaml")
    }

    for name, (url, output_file) in urls.items():
        processed_content = process_file(url)
        if processed_content:
            write_to_file(output_file, processed_content)
        else:
            print(f"Failed to process {name} from {url}")


if __name__ == "__main__":
    main()
