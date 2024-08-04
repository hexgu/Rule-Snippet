# Rule Snippet

为 subconverter 和 Adguard Home 设计，为 Clash 、 Quantumult X 、 Adguard Home 单独优化，针对桌面端移动端单独适配，且适用于全平台全软件的个人自用规则集

## 项目鸣谢

本项目数据来源以下作者及其项目

[SukkaW](https://github.com/SukkaW)
的 [Surge](https://github.com/SukkaW/Surge)（[AGPL-3.0](https://github.com/SukkaW/Surge/blob/master/LICENSE)
）及其 [Ruleset Server](https://ruleset.skk.moe/)

[Misaka Network, Inc.](https://github.com/misakaio)
的 [chnroutes2](https://github.com/misakaio/chnroutes2) （[CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)）

[VirgilClyne](https://github.com/VirgilClyne/GetSomeFries)
的 [DNS 分流模块](https://github.com/VirgilClyne/GetSomeFries/wiki/%F0%9F%8C%90-DNS)（[GPL-3.0](https://github.com/VirgilClyne/GetSomeFries#GPL-3.0-1-ov-file)）

## 为什么要额外添加 Clash 规则集？

https://github.com/tindy2013/subconverter/issues/751#issue-2278998619

> 在 mihomo (Clash.Meta) 系应用中，rule-provider 可以处理的 domainset
>
>在尝试 subconverter 转化的时候却无法通过 clash-domain: 展开到 rules 中，即便没有报错：
>
>简单溯源发现 SukkaW/Surge 提供的 Clash Premium 版本 domainset 每条域名规则单独一行且开头没有 payload
>
>而在 src/generator/config/ruleconvert.cpp#L31 仅仅通过文件开头 payload 判断为 Clash。

SukkaW/Surge 在当前 subconverter 中无法正常转换，因此额外添加 Clash 规则集
