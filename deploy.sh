#!/bin/bash
# AutoContentFactory 一键部署脚本
# 支持: Railway, Render, Heroku, PythonAnywhere

echo "🚀 AutoContentFactory 部署脚本"
echo "================================"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要Python3，请先安装"
    exit 1
fi

# 创建requirements.txt
echo "创建依赖文件..."
cat > requirements.txt << EOF
Flask==2.3.3
gunicorn==20.1.0
python-dotenv==1.0.0
EOF

# 创建runtime.txt (Python版本)
echo "python-3.11.0" > runtime.txt

# 创建Procfile
echo "创建Procfile..."
cat > Procfile << EOF
web: gunicorn api_server:app
EOF

# 创建.env.example
echo "创建环境变量示例..."
cat > .env.example << EOF
# AutoContentFactory 配置
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
API_KEY=your-api-key-here

# 部署配置
PORT=5000
HOST=0.0.0.0
DEBUG=false
EOF

echo ""
echo "✅ 部署文件创建完成！"
echo ""
echo "🎯 部署选项："
echo "1. Railway (推荐) - railway.app"
echo "2. Render - render.com"
echo "3. Heroku - heroku.com"
echo "4. PythonAnywhere - pythonanywhere.com"
echo ""
echo "📦 包含文件："
echo "  - api_server.py (主程序)"
echo "  - requirements.txt (依赖)"
echo "  - Procfile (进程文件)"
echo "  - runtime.txt (Python版本)"
echo "  - .env.example (环境变量)"
echo ""
echo "🚀 快速部署到Railway："
echo "1. 访问 https://railway.app"
echo "2. 点击 'New Project'"
echo "3. 选择 'Deploy from GitHub repo'"
echo "4. 选择这个仓库"
echo "5. 等待部署完成"
echo ""
echo "💰 开始赚钱："
echo "部署完成后，API即可使用："
echo "  - POST /generate - 生成内容"
echo "  - GET /health - 健康检查"
echo ""
echo "🎉 部署完成即可开始收费："
echo "  - 基础计划: $29/月 (1000次API调用)"
echo "  - 专业计划: $99/月 (10000次API调用)"
echo "  - 企业计划: $299/月 (无限调用)"
echo ""
echo "⏰ 预计部署时间：5-10分钟"
echo "💵 预计收入时间：部署后24小时内"