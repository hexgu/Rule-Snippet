# Rule Snippet

为 subconverter 和 Adguard Home 设计，为 Clash 、 Quantumult X 、 Adguard Home 单独优化，针对桌面端移动端单独适配，且适用于全平台全软件的个人自用规则集

github actions 每天自动更新，保持上游同步

## 使用指南

### 通用

请使用 subconverter 引入下方配置

桌面端：https://sub.xeton.dev/?config=https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/pc.ini 包含完整去广告规则，吃性能

移动端：https://sub.xeton.dev/?config=https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/mobile.ini
不包含去广告规则，轻量化，建议搭配 Adguard Home 使用

### Clash

> https://github.com/tindy2013/subconverter/issues/751#issue-2278998619
>
> subconverter 通过文件开头 payload 判断是否为 Clash 规则，而 SukkaW/Surge 的 domainset 每条域名规则单独一行且开头没有
> payload
>
>所以 subconverter 无法正确处理 SukkaW/Surge Clash 规则集格式,需要额外添加规则集以确保兼容性
>

~~~
clash-domain:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/domainset/reject.yaml

clash-domain:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/domainset/cdn.yaml

clash-domain:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/domainset/apple_cdn.yaml

clash-domain:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/domainset/download.yaml

clash-domain:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/non_ip/download.yaml

clash-ipcidr:https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/Clash/ip/china_ip.yaml
~~~
### Adguard Home

~~~
https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/AdGuard/adguard-reject_extra.txt

https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/AdGuard/adguard-reject.txt

https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/AdGuard/adguard-non_ip_reject-no-drop.txt

https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/AdGuard/adguard-non_ip_reject-drop.txt

https://raw.githubusercontent.com/hexgu/Rule-Snippet/main/AdGuard/adguard-non_ip_reject.txt
~~~
## 项目鸣谢

本项目数据来源以下作者及其项目

[SukkaW](https://github.com/SukkaW)
的 [Surge](https://github.com/SukkaW/Surge)（[AGPL-3.0](https://github.com/SukkaW/Surge/blob/master/LICENSE)）

[Misaka Network, Inc.](https://github.com/misakaio)
的 [chnroutes2](https://github.com/misakaio/chnroutes2) （[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)）

[VirgilClyne](https://github.com/VirgilClyne/GetSomeFries)
的 [DNS 分流模块](https://github.com/VirgilClyne/GetSomeFries/wiki/%F0%9F%8C%90-DNS)（[GPL-3.0](https://github.com/VirgilClyne/GetSomeFries#GPL-3.0-1-ov-file)）

