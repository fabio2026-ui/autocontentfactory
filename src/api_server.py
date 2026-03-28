#!/usr/bin/env python3
"""
AutoContentFactory API Server
快速变现版本 - 核心内容生成API
"""

from flask import Flask, request, jsonify
import os
import json
import time
from datetime import datetime

app = Flask(__name__)

# 模拟内容生成函数
def generate_content(topic, content_type="article", length="medium"):
    """生成内容的核心函数"""
    
    templates = {
        "article": {
            "title": f"如何通过{topic}实现每月$10,000被动收入",
            "introduction": f"在当今数字时代，{topic}已成为最赚钱的领域之一。本文将揭示三个简单步骤，帮助你在30天内开始赚钱。",
            "sections": [
                {
                    "heading": "第一步：市场研究",
                    "content": f"首先，你需要了解{topic}市场的需求。使用Google Trends分析搜索量，查看竞争对手的定价策略。"
                },
                {
                    "heading": "第二步：内容创建",
                    "content": f"创建关于{topic}的高质量内容。可以是博客文章、视频教程或社交媒体帖子。关键是提供真实价值。"
                },
                {
                    "heading": "第三步：变现策略",
                    "content": f"通过联盟营销、数字产品销售或咨询服务将{topic}内容变现。每月收入目标：$10,000。"
                }
            ],
            "conclusion": f"通过系统化执行这三个步骤，你可以在{topic}领域建立稳定的收入流。关键是立即开始，持续优化。",
            "call_to_action": "立即开始：访问我们的网站获取免费模板和工具。"
        },
        "video_script": {
            "title": f"{topic}赚钱指南 - 完整视频脚本",
            "hook": f"想知道如何通过{topic}每月赚取$10,000吗？观看这个视频，我将揭示三个秘密策略。",
            "sections": [
                {"time": "0:00-0:30", "content": "介绍和问题陈述"},
                {"time": "0:30-2:00", "content": f"策略1：{topic}市场分析"},
                {"time": "2:00-4:00", "content": f"策略2：{topic}内容创建"},
                {"time": "4:00-5:30", "content": f"策略3：{topic}变现方法"},
                {"time": "5:30-6:00", "content": "总结和行动号召"}
            ]
        },
        "social_media": {
            "platforms": ["LinkedIn", "Twitter", "Instagram", "TikTok"],
            "posts": [
                f"🔥 刚刚发现通过{topic}每月赚$10,000的方法！\n\n步骤1：市场研究\n步骤2：内容创建\n步骤3：变现\n\n完整指南：链接",
                f"💡 {topic}赚钱秘诀：提供真实价值，建立信任，然后变现。\n\n#被动收入 #数字营销",
                f"📈 我的{topic}收入增长300%！\n\n关键：一致性 + 质量 + 价值\n\n想学习？评论'教程'"
            ]
        }
    }
    
    return templates.get(content_type, templates["article"])

# API路由
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "AutoContentFactory API",
        "version": "1.0.0",
        "endpoints": {
            "/generate": "POST - 生成内容",
            "/health": "GET - 健康检查",
            "/stats": "GET - 使用统计"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "uptime": time.time() - app_start_time
    })

@app.route('/generate', methods=['POST'])
def generate():
    """生成内容API"""
    try:
        data = request.json
        topic = data.get('topic', '数字营销')
        content_type = data.get('content_type', 'article')
        length = data.get('length', 'medium')
        
        # 生成内容
        content = generate_content(topic, content_type, length)
        
        # 记录使用
        usage_log.append({
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "content_type": content_type,
            "length": length
        })
        
        return jsonify({
            "success": True,
            "content": content,
            "metadata": {
                "topic": topic,
                "content_type": content_type,
                "length": length,
                "generated_at": datetime.now().isoformat(),
                "word_count": len(str(content).split())
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/stats', methods=['GET'])
def stats():
    """使用统计"""
    return jsonify({
        "total_requests": len(usage_log),
        "recent_requests": usage_log[-10:] if usage_log else [],
        "popular_topics": get_popular_topics()
    })

def get_popular_topics():
    """获取热门话题"""
    topics = {}
    for log in usage_log:
        topic = log.get('topic', 'unknown')
        topics[topic] = topics.get(topic, 0) + 1
    
    # 按使用次数排序
    sorted_topics = sorted(topics.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_topics[:5])

# 全局变量
app_start_time = time.time()
usage_log = []

if __name__ == '__main__':
    print("🚀 AutoContentFactory API 启动中...")
    print("📝 服务：内容生成API")
    print("💰 目标：快速变现")
    print("🔗 端点：")
    print("  - GET  /health - 健康检查")
    print("  - POST /generate - 生成内容")
    print("  - GET  /stats - 使用统计")
    print("")
    print("🌐 访问 http://localhost:5000 查看API文档")
    
    # 启动服务器
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)