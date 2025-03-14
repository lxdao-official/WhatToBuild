---
# Required fields
title: "tempaddr generator"
description: "一个支持生成临时钱包地址的工具，自动生成私钥和公钥，并根据用户需求转入指定数量和类型的测试币"
tags:  # Choose from: ZK, DeFi, NFT, Wallet, DAO, Infra, Identity, Gaming, PublicGoods, Privacy, Security or add your own
  - "Infra"
  - "PublicGoods"
contributors:
  - github: "brucexu-eth"
  - github: "Coooder-Crypto"
status: "[todo]"  # Current status of the idea
---

# Detailed Introduction

## What
一个支持生成临时钱包地址的工具，自动生成私钥和公钥，并根据用户需求转入指定数量和类型的测试币，同时支持每天续期功能，未续期时自动将剩余测试币返还国库。还可以通过API实现自动化测试功能。

## Why
当前在区块链开发和测试中，开发者需要频繁申请测试币，手动生成钱包地址并管理私钥，这不仅耗时且容易出错。这个工具通过自动化生成钱包和分发测试币，极大地简化了开发者的工作流程，提高了效率。此外，未续期时自动回收测试币的机制还能避免测试币的浪费，优化测试网络的资源分配。

## How
1. **钱包生成模块**：使用加密算法（如ECDSA）生成钱包的私钥和公钥。
2. **测试币分发模块**：集成测试网络的水龙头服务，根据用户需求转入指定数量和类型的测试币。
3. **续期与回收机制**：
    - 设置每日续期提醒，用户需点击续期按钮。
    - 未续期时，自动触发回收逻辑，将剩余测试币返还至国库地址。
4. **API接口**：设计RESTful API，支持开发者通过接口调用生成钱包、分发测试币和续期操作，实现自动化测试。
5. **安全性与日志管理**：确保私钥生成和存储的安全性，同时记录所有操作日志以便追踪和审计。

## Related Materials
https://github.com/kovan-testnet/faucet