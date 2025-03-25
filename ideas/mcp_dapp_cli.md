---
# Required fields
title: "MCP Dapp开发脚手架"
description: "一个整合链上数据查询、交互、前端UI代码生成的Mcp服务开发脚手架"
tags:  # Choose from: ZK, DeFi, NFT, Wallet, DAO, Infra, Identity, Gaming, PublicGoods, Privacy, Security or add your own
  - "Dev"
  - "Mcp"
  - "Dapp"
contributors:
  - github: "BiscuitCoder"
status: "[todo]"  # Current status of the idea
---

# MCP Dapp开发脚手架

## What
一个整合链上数据查询、交易、钱包管理、测试币分发、自动化测试、前端UI代码生成的Mcp服务开发脚手架。用户可以通过选择模板项目，通过自然语言描述快速从合约开发到测试，并生成可视化UI部署。

## Why
当前的主流开发工具如Hardhat、Truffle、OpenZeppelin等都提供了丰富的功能，Mcp的出现提供更进一步的可能性：
- 通过自然语言引导与mcp自动化，降低各种工具的配置和使用的门槛。
- 通过自然语言实现自动化测试。
- 一键生成与合约功能契合的UI&前端产物。

## How
1. 调研整理目前普适性的合约、前端、测试工具，并进行模板的整合。
2. 基于 [mcp-clits-sdk](https://github.com/modelcontextprotocol/typescript-sdk) 开发脚手架的核心服务。
3. 上架各IDE插件市场与mcp生态社区。

## Related Materials
https://github.com/base/base-mcp/issues
https://github.com/modelcontextprotocol/typescript-sdk