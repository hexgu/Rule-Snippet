import requests


def process_file(url):
    """
    从给定的URL获取文件，并对其进行处理。

    参数:
    url (str): 文件的URL。

    返回:
    list: 处理后的文件内容，每一行都被格式化为 "  - 'line'"。
    None: 如果请求的状态码不是200，则返回None。
    """
    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        processed_lines = []
        for line in lines:
            if line.strip() and not line.strip().startswith('#'):
                processed_lines.append(f"  - '{line.strip()}'")
        return processed_lines
    else:
        return None


def write_to_file(filename, processed_content):
    """
    将处理后的内容写入文件。

    参数:
    filename (str): 要写入的文件的名称。
    processed_content (list): 处理后的文件内容。
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("payload:\n")
        for line in processed_content:
            file.write(line + '\n')


# 获取文件并处理
reject_url = "https://ruleset.skk.moe/Clash/domainset/reject.txt"
cdn_url = "https://ruleset.skk.moe/Clash/domainset/cdn.txt"
apple_cdn_url = "https://ruleset.skk.moe/Clash/domainset/apple_cdn.txt"
download_url = "https://ruleset.skk.moe/Clash/domainset/download.txt"
downloadip_url = "https://ruleset.skk.moe/Clash/non_ip/download.txt"
china_ip = "https://ruleset.skk.moe/Clash/ip/china_ip.txt"

reject_processed = process_file(reject_url)
cdn_processed = process_file(cdn_url)
apple_cdn_processed = process_file(apple_cdn_url)
download_processed = process_file(download_url)
downloadip_processed = process_file(downloadip_url)
china_ip_processed = process_file(china_ip)

# 写入文件
if reject_processed is not None:
    write_to_file("./Clash/domainset/reject.yaml", reject_processed)
if cdn_processed is not None:
    write_to_file("./Clash/domainset/cdn.yaml", cdn_processed)
if apple_cdn_processed is not None:
    write_to_file("./Clash/domainset/apple_cdn.yaml", apple_cdn_processed)
if download_processed is not None:
    write_to_file("./Clash/domainset/download.yaml", download_processed)
if downloadip_processed is not None:
    write_to_file("./Clash/non_ip/downloadip.yaml", downloadip_processed)
if china_ip_processed is not None:
    write_to_file("./Clash/ip/china_ip.yaml", china_ip_processed)
