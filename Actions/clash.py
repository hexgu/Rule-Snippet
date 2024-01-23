import requests

# 获取文件并处理
def process_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        processed_lines = [f"  - '{line.strip()}'" for line in lines if line.strip() and not line.strip().startswith('#')]
        return processed_lines
    else:
        return None

# 处理并写入文件
def write_to_file(filename, processed_content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("payload:\n")
        file.write('\n'.join(processed_content))

# 获取并处理两个文件
reject_url = "https://ruleset.skk.moe/Clash/domainset/reject.txt"
cdn_url = "https://ruleset.skk.moe/Clash/domainset/cdn.txt"
apple_cdn_url = "https://ruleset.skk.moe/Clash/domainset/apple_cdn.txt"
download_url = "https://ruleset.skk.moe/Clash/domainset/download.txt"
downloadip_url = "https://ruleset.skk.moe/Clash/non_ip/download.txt"

reject_processed = process_file(reject_url)
cdn_processed = process_file(cdn_url)
apple_cdn_processed = process_file(apple_cdn_url)
download_processed = process_file(download_url)
downloadip_processed = process_file(downloadip_url)
# 写入文件
if reject_processed is not None:
    write_to_file("reject.yaml", reject_processed)
if cdn_processed is not None:
    write_to_file("cdn.yaml", cdn_processed)


if apple_cdn_processed is not None:
    write_to_file("apple_cdn.yaml", apple_cdn_processed)

if download_processed is not None:
    write_to_file("download.yaml", download_processed)

if downloadip_processed is not None:
    write_to_file("downloadip.yaml", downloadip_processed)
