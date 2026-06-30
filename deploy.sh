#!/bin/bash

echo "========================================="
echo "🚀 Freqtrade 网格交易机器人部署脚本"
echo "========================================="

# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Python 和依赖
sudo apt install -y python3.9 python3-pip python3-venv git

# 创建项目目录
cd ~ && mkdir -p freqtrade && cd freqtrade

# 克隆项目
git clone https://github.com/bflc888/crypto-grid-trading-bot.git .

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 创建用户数据目录
freqtrade create-userdir --userdir user_data

echo "========================================="
echo "✅ 部署完成！"
echo "========================================="
echo ""
echo "📝 下一步："
echo "1. 编辑 config.json，填入你的币安 API Key"
echo "2. 运行: freqtrade start"
echo "3. 访问: http://your-server-ip:8080"
echo ""
echo "⚠️  记得设置 API 权限为仅现货交易！"