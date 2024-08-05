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
        "reject": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/domainset/reject.txt",
                   "./Clash/domainset/reject.yaml"),
        "cdn": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/domainset/cdn.txt",
                "./Clash/domainset/cdn.yaml"),
        "apple_cdn": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/domainset/apple_cdn.txt",
                      "./Clash/domainset/apple_cdn.yaml"),
        "download": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/domainset/download.txt",
                     "./Clash/domainset/download.yaml"),
        "downloadip": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/non_ip/download.txt",
                       "./Clash/non_ip/download.yaml"),
        "china_ip": ("https://raw.githubusercontent.com/SukkaLab/ruleset.skk.moe/master/Clash/ip/china_ip.txt",
                     "./Clash/ip/china_ip.yaml")
    }

    for name, (url, output_file) in urls.items():
        processed_content = process_file(url)
        if processed_content:
            write_to_file(output_file, processed_content)
        else:
            print(f"Failed to process {name} from {url}")


if __name__ == "__main__":
    main()
