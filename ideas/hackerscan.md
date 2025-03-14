---
# Required fields
title: "Hackerscan"
description: "轻量级 EVM 区块链浏览器，专为本地测试网设计，提供简单的界面，支持通过单一 RPC 接口查询区块链数据"
tags:  # Choose from: ZK, DeFi, NFT, Wallet, DAO, Infra, Identity, Gaming, PublicGoods, Privacy, Security or add your own
  - "Infra"
  - "PublicGoods"
contributors:
  - github: "brucexu-eth"
status: "[todo]"  # Current status of the idea
---

# Detailed Introduction

## What
轻量级 EVM 区块链浏览器，专为本地测试网设计，提供简单的界面，支持通过单一 RPC 接口查询区块链数据

## Why
当前在本地搭建的 EVM 测试网中，开发者通常只有一个 RPC 接口，但缺乏直观的界面来查询区块、交易、账户余额等数据。现有的区块链浏览器（如 Etherscan）功能复杂且难以在本地环境中部署。Hackerscan 通过提供一个简单的界面，帮助开发者快速查询和调试数据，降低开发门槛，提高测试效率，尤其适合个人开发者或小型团队。

## How
- **前端界面**：
支持用户输入 RPC 方法和参数，显示 JSON 格式的查询结果。
- **后端服务**：
    
    使用 Node.js 或 Python 搭建一个轻量级服务，接收前端请求，转发到本地测试网的 RPC 接口，并返回结果。
    
- **基础功能**：
    - 支持账户余额查询、区块信息查询、交易详情查询等常用功能。
    - 提供自定义 RPC 请求输入框，便于调试。
- **部署**：
    
    提供一个简单的本地运行方式（如直接运行脚本或 Docker 镜像），方便开发者快速启动。

## Related Materials
https://github.com/kovan-testnet/faucet