# 🌐 云服务部署指南

## 阿里云部署（推荐）

### 1️⃣ 购买云服务器
- 登录 [阿里云](https://www.aliyun.com/)
- 选择："轻量应用服务器" 或 "ECS"
- 配置：1 核 1GB 内存，Ubuntu 20.04/22.04
- 价格：约 ¥10-20/月

### 2️⃣ 连接到服务器
```bash
# Windows 用 PuTTY，Mac/Linux 用 Terminal
ssh root@your_server_ip
```

### 3️⃣ 一键部署
```bash
# 下载部署脚本
curl -O https://raw.githubusercontent.com/bflc888/crypto-grid-trading-bot/main/deploy.sh

# 执行部署
bash deploy.sh

# 启动机器人
cd ~/freqtrade
source venv/bin/activate
freqtrade start
```

### 4️⃣ 配置 API（重要！）
编辑 `config.json`：
```json
{
  "exchange": {
    "key": "your_api_key",
    "secret": "your_api_secret"
  }
}
```

### 5️⃣ 后台运行
使用 `screen` 或 `systemd` 让机器人后台运行：
```bash
# 方式 A：使用 screen
screen -S bot
freqtrade start

# Ctrl+A+D 分离，稍后可以 screen -r bot 恢复

# 方式 B：使用 systemd（推荐）
sudo systemctl enable freqtrade
sudo systemctl start freqtrade
```

## 腾讯云部署

过程基本相同，只是服务商不同。

## 常见问题

**Q: 如何查看日志？**
```bash
tail -f ~/freqtrade/user_data/logs/freqtrade.log
```

**Q: 如何停止机器人？**
```bash
freqtrade stop
```

**Q: 如何更新代码？**
```bash
cd ~/freqtrade
git pull
pip install -r requirements.txt
freqtrade start
```