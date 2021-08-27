# SacnNer

## 简介

网络扫描工具，提供方便的一键扫描

## 计划实现的功能

1. 信息收集

   1. 端口扫描 [¹][1]

      1. TCP 连接扫描
      2. TCP SYN 扫描(也称为半开放扫描或 stealth 扫描)
      3. TCP 圣诞树(Xmas Tree)扫描
      4. TCP FIN 扫描
      5. TCP 空扫描(Null)
      6. TCP ACK 扫描
      7. TCP 窗口扫描

   2. Ping\ICMP 扫描
   3. 系统类型
   4. 域控查询

2. 口令爆破

   1. SSH
   2. SMB
   3. MySQL
   4. Redis
   5. PostgreSQL

3. 漏洞扫描

   1. MS17-010

4. 漏洞利用
5. Web 探测
6. 数据保存

## 文件、目录含义

1. `main.py` - 主文件：承担与用户的交互和与其他组件的调用
2. `infoCollection.py` - 信息搜集：实现信息搜集
3. `tools.py` - 实用工具：在控制台打印红色等

[1]: (https://xiaix.me/duan-kou-sao-miao-yuan-li-ji-shi-xian/) "端口扫描原理及实现"
