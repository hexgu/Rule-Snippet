import requests


def fetch_content(url):
    response = requests.get(url)
    return response.text.splitlines()


def convert_to_adblock(lines, rule_type):
    adblock_rules = []
    current_rule_type = None

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('!'):
            continue

        if rule_type == 'DOMAIN-SET':
            if line.startswith('+.'):
                adblock_rules.append(f"||{line[2:]}^")
            elif line.startswith('.'):
                adblock_rules.append(f"||{line[1:]}^")
            elif '*' in line:
                adblock_rules.append(f"||{line.replace('*', '')}^")
            else:
                adblock_rules.append(f"||{line}^")
        elif rule_type == 'RULE-SET':
            if ',' in line:
                parts = line.split(',')
                current_rule_type = parts[0]
                value = ','.join(parts[1:])
            else:
                value = line

            if current_rule_type == 'DOMAIN':
                adblock_rules.append(f"||{value}^")
            elif current_rule_type == 'DOMAIN-SUFFIX':
                adblock_rules.append(f"||*.{value}^")
            elif current_rule_type == 'DOMAIN-KEYWORD':
                adblock_rules.append(f"*{value}*")
            elif current_rule_type == 'DOMAIN-REGEX':
                adblock_rules.append(f"/{value}/")
            # IP-CIDR, IP-CIDR6, GEOIP 和其他不支持的规则类型都被忽略

    return adblock_rules


def main():
    urls = [
        ('https://ruleset.skk.moe/List/domainset/reject.conf', 'DOMAIN-SET', 'reject'),
        ('https://ruleset.skk.moe/List/domainset/reject_extra.conf', 'DOMAIN-SET', 'reject_extra'),
        ('https://ruleset.skk.moe/List/non_ip/reject.conf', 'RULE-SET', 'non_ip_reject'),
        ('https://ruleset.skk.moe/List/non_ip/reject-no-drop.conf', 'RULE-SET', 'non_ip_reject-no-drop'),
        ('https://ruleset.skk.moe/List/non_ip/reject-drop.conf', 'RULE-SET', 'non_ip_reject-drop'),
        ('https://ruleset.skk.moe/List/non_ip/sogouinput.conf', 'RULE-SET', 'non_ip_sogouinput')
    ]

    for url, rule_type, file_name in urls:
        content = fetch_content(url)
        rules = convert_to_adblock(content, rule_type)

        # Remove duplicates while preserving order
        unique_rules = list(dict.fromkeys(rules))

        output_file = f'AdGuard/adguard-{file_name}.txt'
        with open(output_file, 'w') as f:
            f.write('\n'.join(unique_rules))

        print(f"Conversion complete for {file_name}. {len(unique_rules)} rules written to {output_file}")


if __name__ == "__main__":
    main()