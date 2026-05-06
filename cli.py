#!/usr/bin/env python3
"""
嵌入式竞赛全链路智能开发与验证 Agent 系统 - CLI 入口

使用方法:
    python cli.py <command> [options]

命令:
    init      - 初始化新项目
    generate  - 生成项目代码
    monitor   - 启动串口监控
    test      - 生成测试用例
    docs      - 生成项目文档
    run       - 运行完整流程
    status    - 查看系统状态

示例:
    python cli.py init --project "智能环境监测系统" --board esp32
    python cli.py generate --project "智能环境监测系统"
    python cli.py monitor --port COM3 --baud 115200
    python cli.py run --project "智能环境监测系统" --board esp32
"""

import os
import sys

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli import cli

if __name__ == "__main__":
    cli()
