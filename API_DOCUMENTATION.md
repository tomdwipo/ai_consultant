# 📡 API Documentation - AI Media Consultant Platform

## 🎯 Overview

RESTful API documentation untuk AI Media Consultant Platform. API ini menyediakan endpoints untuk content generation, user management, brand profiles, dan analytics.

### Base URL
```
Production: https://api.aimediacons.com/v1
Staging: https://staging-api.aimediacons.com/v1
Development: http://localhost:8000/v1
```

### Authentication
API menggunakan JWT Bearer token authentication.

```http
Authorization: Bearer <your_jwt_token>
```

## 🔐 Authentication Endpoints

### POST /auth/register
Register new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "full_name": "John Doe",
  "company_name": "Acme Corp" // optional
}
```

**Response (201):**
```json
{
  "user": {
    "id": "uuid-string",
    "email": "user@example.com",
    "full_name": "John Doe",
    "subscription_tier": "starter",
    "created_at": "2025-01-31T16:30:00Z"
  },
  "access_token": "jwt-token-string",
  "refresh_token": "refresh-token-string",
  "token_type": "bearer"
}
```

### POST /auth/login
Authenticate user and get access token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response (200):**
```json
{
  "access_token": "jwt-token-string",
  "refresh_token": "refresh-token-string",
  "token_type": "bearer",
  "expires_in": 900
}
```

### POST /auth/refresh
Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "refresh-token-string"
}
```

**Response (200):**
```json
{
  "access_token": "new-jwt-token-string",
  "token_type": "bearer",
  "expires_in": 900
}
```

### POST /auth/logout
Logout user and invalidate tokens.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "message": "Successfully logged out"
}
```

## 👤 User Management

### GET /users/me
Get current user profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "full_name": "John Doe",
  "company_name": "Acme Corp",
  "subscription_tier": "professional",
  "usage_stats": {
    "content_generated_this_month": 45,
    "content_limit": 150,
    "api_calls_today": 12
  },
  "created_at": "2025-01-31T16:30:00Z",
  "updated_at": "2025-01-31T16:30:00Z"
}
```

### PUT /users/me
Update current user profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "full_name": "John Smith",
  "company_name": "New Company Ltd"
}
```

**Response (200):**
```json
{
  "id": "uuid-string",
  "email": "user@example.com",
  "full_name": "John Smith",
  "company_name": "New Company Ltd",
  "subscription_tier": "professional",
  "updated_at": "2025-01-31T17:00:00Z"
}
```

### GET /users/usage
Get detailed usage statistics.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "current_period": {
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "content_generated": 45,
    "content_limit": 150,
    "api_calls": 234
  },
  "usage_by_platform": {
    "instagram": 20,
    "linkedin": 15,
    "tiktok": 10
  },
  "usage_by_content_type": {
    "carousel": 18,
    "single_post": 22,
    "article": 5
  }
}
```

## 🏢 Brand Profile Management

### GET /brands
Get all brand profiles for current user.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "brands": [
    {
      "id": "brand-uuid-1",
      "brand_name": "Tech Startup",
      "industry": "Technology",
      "target_audience": {
        "age_range": "25-40",
        "interests": ["technology", "innovation"],
        "demographics": "professionals"
      },
      "brand_voice": {
        "tone": "professional",
        "style": "informative",
        "personality": ["innovative", "trustworthy"]
      },
      "created_at": "2025-01-31T16:30:00Z"
    }
  ],
  "total": 1
}
```

### POST /brands
Create new brand profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "brand_name": "Fashion Brand",
  "industry": "Fashion",
  "description": "Sustainable fashion for modern women",
  "target_audience": {
    "age_range": "20-35",
    "interests": ["fashion", "sustainability"],
    "demographics": "women"
  },
  "brand_voice": {
    "tone": "friendly",
    "style": "inspirational",
    "personality": ["authentic", "empowering"]
  },
  "brand_guidelines": "Always use inclusive language...",
  "color_palette": ["#FF6B6B", "#4ECDC4", "#45B7D1"],
  "logo_url": "https://example.com/logo.png"
}
```

**Response (201):**
```json
{
  "id": "brand-uuid-2",
  "brand_name": "Fashion Brand",
  "industry": "Fashion",
  "description": "Sustainable fashion for modern women",
  "target_audience": {
    "age_range": "20-35",
    "interests": ["fashion", "sustainability"],
    "demographics": "women"
  },
  "brand_voice": {
    "tone": "friendly",
    "style": "inspirational",
    "personality": ["authentic", "empowering"]
  },
  "brand_guidelines": "Always use inclusive language...",
  "color_palette": ["#FF6B6B", "#4ECDC4", "#45B7D1"],
  "logo_url": "https://example.com/logo.png",
  "created_at": "2025-01-31T17:00:00Z"
}
```

### GET /brands/{brand_id}
Get specific brand profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "id": "brand-uuid-1",
  "brand_name": "Tech Startup",
  "industry": "Technology",
  "description": "AI-powered solutions for businesses",
  "target_audience": {
    "age_range": "25-40",
    "interests": ["technology", "innovation"],
    "demographics": "professionals"
  },
  "brand_voice": {
    "tone": "professional",
    "style": "informative",
    "personality": ["innovative", "trustworthy"]
  },
  "brand_guidelines": "Focus on innovation and reliability...",
  "color_palette": ["#2C3E50", "#3498DB", "#E74C3C"],
  "logo_url": "https://example.com/tech-logo.png",
  "created_at": "2025-01-31T16:30:00Z",
  "updated_at": "2025-01-31T16:30:00Z"
}
```

### PUT /brands/{brand_id}
Update brand profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "brand_name": "Updated Tech Startup",
  "description": "AI-powered solutions for modern businesses",
  "brand_voice": {
    "tone": "professional",
    "style": "informative",
    "personality": ["innovative", "trustworthy", "approachable"]
  }
}
```

**Response (200):**
```json
{
  "id": "brand-uuid-1",
  "brand_name": "Updated Tech Startup",
  "description": "AI-powered solutions for modern businesses",
  "brand_voice": {
    "tone": "professional",
    "style": "informative",
    "personality": ["innovative", "trustworthy", "approachable"]
  },
  "updated_at": "2025-01-31T17:30:00Z"
}
```

### DELETE /brands/{brand_id}
Delete brand profile.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (204):**
```
No content
```

## 🎨 Content Generation

### POST /content/generate
Generate content for specified platforms.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "prompt": "Create content about our new AI-powered analytics dashboard",
  "brand_profile_id": "brand-uuid-1",
  "platforms": ["instagram", "linkedin", "tiktok"],
  "content_types": {
    "instagram": ["carousel", "single_post"],
    "linkedin": ["article", "post"],
    "tiktok": ["script"]
  },
  "additional_context": {
    "target_cta": "Sign up for free trial",
    "key_features": ["Real-time analytics", "AI insights", "Easy integration"],
    "tone_override": "excited" // optional
  }
}
```

**Response (202):**
```json
{
  "request_id": "content-request-uuid",
  "status": "processing",
  "estimated_completion": "2025-01-31T17:05:00Z",
  "message": "Content generation started. Check status using request_id."
}
```

### GET /content/requests/{request_id}
Check content generation status.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "request_id": "content-request-uuid",
  "status": "completed", // processing, completed, failed
  "progress": 100,
  "created_at": "2025-01-31T17:00:00Z",
  "completed_at": "2025-01-31T17:04:30Z",
  "content": {
    "instagram": {
      "carousel": {
        "slides": [
          {
            "slide_number": 1,
            "title": "Introducing Our AI Analytics Dashboard",
            "content": "Transform your data into actionable insights with our new AI-powered analytics dashboard! 📊✨",
            "design_notes": "Use brand colors, include dashboard screenshot"
          },
          {
            "slide_number": 2,
            "title": "Real-time Analytics",
            "content": "Get instant insights as your data changes. No more waiting for reports! ⚡",
            "design_notes": "Show real-time chart animation"
          }
        ],
        "hashtags": ["#AIAnalytics", "#DataInsights", "#TechInnovation", "#BusinessIntelligence"],
        "caption": "Ready to transform your business with AI-powered insights? Our new analytics dashboard is here! 🚀\n\nSwipe to see what makes it special ➡️\n\n#AIAnalytics #DataInsights #TechInnovation"
      },
      "single_post": {
        "content": "🚀 Exciting news! Our AI-powered analytics dashboard is now live!\n\n✨ Real-time insights\n📊 AI-driven recommendations\n🔗 Easy integration\n\nReady to revolutionize your data analysis? Sign up for your free trial today!\n\n#AIAnalytics #DataInsights #TechInnovation #BusinessIntelligence #StartupLife",
        "hashtags": ["#AIAnalytics", "#DataInsights", "#TechInnovation", "#BusinessIntelligence", "#StartupLife"],
        "design_notes": "Include dashboard preview image with brand colors"
      }
    },
    "linkedin": {
      "article": {
        "title": "How AI-Powered Analytics is Transforming Business Decision Making",
        "content": "In today's data-driven world, businesses are drowning in information but starving for insights...",
        "word_count": 1200,
        "reading_time": "5 min read",
        "key_points": [
          "The evolution of business analytics",
          "How AI transforms raw data into insights",
          "Real-world applications and benefits"
        ]
      },
      "post": {
        "content": "🎯 Just launched our AI-powered analytics dashboard!\n\nAfter months of development, we're excited to share a solution that transforms how businesses understand their data.\n\n🔍 What makes it special:\n• Real-time insights that update as your data changes\n• AI-driven recommendations for actionable next steps\n• Seamless integration with your existing tools\n\nThe future of business intelligence is here, and it's more accessible than ever.\n\nInterested in seeing how AI can transform your data analysis? Comment 'DEMO' below or send me a DM.\n\n#AIAnalytics #BusinessIntelligence #DataScience #TechInnovation",
        "engagement_hooks": ["Comment 'DEMO' for a free trial", "What's your biggest data challenge?"]
      }
    },
    "tiktok": {
      "script": {
        "hook": "POV: You just discovered the analytics dashboard that reads your mind 🤯",
        "content_beats": [
          {
            "timestamp": "0-3s",
            "action": "Show confused person looking at complex spreadsheets",
            "text_overlay": "Me trying to understand my business data"
          },
          {
            "timestamp": "3-8s",
            "action": "Transition to clean, AI dashboard interface",
            "text_overlay": "Then I found this AI analytics dashboard"
          },
          {
            "timestamp": "8-15s",
            "action": "Show key features with smooth transitions",
            "text_overlay": "Real-time insights • AI recommendations • Easy setup"
          }
        ],
        "cta": "Link in bio for free trial! 🔗",
        "hashtags": ["#AIAnalytics", "#TechTok", "#BusinessHacks", "#DataScience", "#StartupLife"],
        "trending_sounds": ["Original trending sound about transformation"],
        "estimated_duration": "15 seconds"
      }
    }
  },
  "quality_scores": {
    "overall": 0.92,
    "brand_consistency": 0.95,
    "engagement_potential": 0.89,
    "platform_optimization": 0.94
  }
}
```

### GET /content/history
Get content generation history.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 20, max: 100)
- `platform` (optional): Filter by platform
- `brand_id` (optional): Filter by brand profile
- `date_from` (optional): Filter from date (YYYY-MM-DD)
- `date_to` (optional): Filter to date (YYYY-MM-DD)

**Response (200):**
```json
{
  "content": [
    {
      "id": "content-uuid-1",
      "request_id": "content-request-uuid",
      "prompt": "Create content about our new AI-powered analytics dashboard",
      "platforms": ["instagram", "linkedin", "tiktok"],
      "brand_profile": {
        "id": "brand-uuid-1",
        "name": "Tech Startup"
      },
      "status": "completed",
      "quality_score": 0.92,
      "created_at": "2025-01-31T17:00:00Z",
      "completed_at": "2025-01-31T17:04:30Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 45,
    "total_pages": 3
  }
}
```

### GET /content/{content_id}
Get specific generated content.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "id": "content-uuid-1",
  "request_id": "content-request-uuid",
  "prompt": "Create content about our new AI-powered analytics dashboard",
  "brand_profile_id": "brand-uuid-1",
  "platforms": ["instagram", "linkedin", "tiktok"],
  "content": {
    // Full content object as shown in generation response
  },
  "quality_scores": {
    "overall": 0.92,
    "brand_consistency": 0.95,
    "engagement_potential": 0.89,
    "platform_optimization": 0.94
  },
  "usage_stats": {
    "views": 15,
    "downloads": 3,
    "shares": 1
  },
  "created_at": "2025-01-31T17:00:00Z",
  "updated_at": "2025-01-31T17:04:30Z"
}
```

### PUT /content/{content_id}
Update generated content (for editing).

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "content": {
    "instagram": {
      "single_post": {
        "content": "Updated content text...",
        "hashtags": ["#UpdatedHashtag", "#AIAnalytics"]
      }
    }
  },
  "notes": "Updated caption for better engagement"
}
```

**Response (200):**
```json
{
  "id": "content-uuid-1",
  "content": {
    // Updated content object
  },
  "updated_at": "2025-01-31T18:00:00Z",
  "version": 2
}
```

### DELETE /content/{content_id}
Delete generated content.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (204):**
```
No content
```

## 📊 Analytics & Insights

### GET /analytics/dashboard
Get dashboard analytics overview.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `period` (optional): time period (7d, 30d, 90d, 1y) (default: 30d)
- `brand_id` (optional): Filter by brand profile

**Response (200):**
```json
{
  "period": "30d",
  "summary": {
    "total_content_generated": 45,
    "total_platforms": 3,
    "average_quality_score": 0.91,
    "most_used_platform": "instagram"
  },
  "content_by_platform": {
    "instagram": 20,
    "linkedin": 15,
    "tiktok": 10
  },
  "content_by_type": {
    "carousel": 18,
    "single_post": 22,
    "article": 5
  },
  "quality_trends": [
    {
      "date": "2025-01-01",
      "average_score": 0.88
    },
    {
      "date": "2025-01-15",
      "average_score": 0.91
    },
    {
      "date": "2025-01-31",
      "average_score": 0.93
    }
  ],
  "top_performing_content": [
    {
      "id": "content-uuid-1",
      "prompt": "AI analytics dashboard launch",
      "quality_score": 0.96,
      "platforms": ["instagram", "linkedin"],
      "created_at": "2025-01-31T17:00:00Z"
    }
  ]
}
```

### GET /analytics/content-performance
Get detailed content performance analytics.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `content_id` (optional): Specific content ID
- `platform` (optional): Filter by platform
- `period` (optional): Time period (7d, 30d, 90d)

**Response (200):**
```json
{
  "performance_metrics": {
    "total_content": 45,
    "average_quality_score": 0.91,
    "engagement_prediction": {
      "instagram": {
        "estimated_reach": 2500,
        "estimated_engagement_rate": 0.045,
        "best_posting_time": "18:00"
      },
      "linkedin": {
        "estimated_views": 1200,
        "estimated_engagement_rate": 0.032,
        "best_posting_day": "Tuesday"
      }
    }
  },
  "content_analysis": [
    {
      "content_id": "content-uuid-1",
      "platform": "instagram",
      "content_type": "carousel",
      "quality_score": 0.96,
      "predicted_performance": {
        "reach": 3000,
        "engagement_rate": 0.052,
        "best_time": "19:00"
      },
      "optimization_suggestions": [
        "Consider adding more visual elements",
        "Hashtag mix could include more niche tags"
      ]
    }
  ]
}
```

## 🔧 Platform-Specific Features

### GET /platforms/instagram/hashtags/suggestions
Get hashtag suggestions for Instagram content.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `content` (required): Content text to analyze
- `industry` (optional): Industry category
- `audience_size` (optional): small, medium, large (default: medium)

**Response (200):**
```json
{
  "hashtags": {
    "trending": ["#TechTrends2025", "#AIInnovation", "#StartupLife"],
    "niche": ["#B2BAnalytics", "#DataVisualization", "#BusinessIntelligence"],
    "branded": ["#YourBrandName", "#YourProductName"],
    "community": ["#TechCommunity", "#DataScience", "#Analytics"]
  },
  "recommendations": {
    "optimal_count": 8,
    "mix_suggestion": "3 trending + 3 niche + 1 branded + 1 community",
    "avoid": ["#follow4follow", "#like4like"]
  }
}
```

### GET /platforms/linkedin/topics/trending
Get trending topics for LinkedIn content.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `industry` (optional): Industry filter
- `region` (optional): Geographic region

**Response (200):**
```json
{
  "trending_topics": [
    {
      "topic": "AI in Business",
      "trend_score": 0.95,
      "related_keywords": ["artificial intelligence", "automation", "machine learning"],
      "optimal_content_type": "article"
    },
    {
      "topic": "Remote Work Culture",
      "trend_score": 0.87,
      "related_keywords": ["remote work", "hybrid", "team culture"],
      "optimal_content_type": "post"
    }
  ],
  "content_suggestions": [
    "How AI is reshaping business operations",
    "Building strong remote team culture",
    "The future of workplace technology"
  ]
}
```

### GET /platforms/tiktok/trends
Get current TikTok trends and sounds.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Query Parameters:**
- `category` (optional): Content category
- `region` (optional): Geographic region

**Response (200):**
```json
{
  "trending_sounds": [
    {
      "sound_id": "sound-123",
      "name": "Trending Business Sound",
      "usage_count": 50000,
      "trend_score": 0.92,
      "best_for": ["business", "tech", "education"]
    }
  ],
  "trending_hashtags": [
    {
      "hashtag": "#TechTok",
      "usage_count": 2000000,
      "growth_rate": 0.15,
      "category": "technology"
    }
  ],
  "content_formats": [
    {
      "format": "Before/After Transformation",
      "popularity": 0.89,
      "best_for": ["product demos", "tutorials"]
    }
  ]
}
```

## 💳 Subscription & Billing

### GET /subscription/current
Get current subscription details.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response (200):**
```json
{
  "subscription": {
    "id": "sub-uuid-1",
    "tier": "professional",
    "status": "active",
    "current_period_start": "2025-01-01T00:00:00Z",
    "current_period_end": "2025-02-01T00:00:00Z",
    "cancel_at_period_end": false
  },
  "usage": {
    "content_generated": 45,
    "content_limit": 150,
    "api_calls": 234,
    "api_limit": 1000
  },
  "billing": {
    "amount": 599000,
    "currency": "IDR",
    "interval": "month",
    "next_billing_date": "2025-02-01T00:00:00Z"
  }
}
```

### POST /subscription/upgrade
Upgrade subscription tier.

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "new_tier": "agency",
  "billing_cycle": "monthly" // monthly, yearly
}
```

**Response (200):**
```json
{
  "subscription": {
    "id": "sub-uuid-1",
    "tier": "agency",
    "status": "active",
    "upgraded_at": "2025-01-31T18:00:00Z"
  },
  "billing": {
    "amount": 1200000,
    "currency": "IDR",
    "proration_amount": 200000,
    "next_billing_date": "2025-02-01T00:00:00Z"
  }
}
```

### POST /subscription/cancel
Cancel subscription (at period end).

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "reason": "switching to competitor", // optional
  "feedback": "Need more customization options" // optional
}
```

**Response (200):**
```json
{
  "subscription": {
    "id": "sub-uuid-1",
    "status": "active",
    "cancel_at_period_end": true,
    "canceled_at": "2025-01-31T18:00:00Z",
    "current_period_end": "2025-02-01T00:00:00Z"
  },
  "message": "Subscription will be canceled at the end of current billing period"
}
```

## 📈 Webhooks

### Webhook Events
Configure webhooks to receive real-time notifications about events.

**Available Events:**
- `content.generation.completed`
- `content.generation.failed`
- `subscription.updated`
- `subscription.canceled`
- `usage.limit.reached`

### Webhook Payload Example
```json
{
  "event": "content.generation.completed",
  "timestamp": "2025-01-31T17:04:30Z",
  "data": {
    "request_id": "content-request-uuid",
    "user_id": "user-uuid",
    "content_id": "content-uuid-1",
    "platforms": ["instagram", "linkedin"],
    "quality_score": 0.92
  }
}
```

## ❌ Error Responses

### Error Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request parameters",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ],
    "request_id": "req-uuid-123"
  }
}
```

### Common Error Codes
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Validation Error
- `429` - Rate Limit Exceeded
- `500` - Internal Server Error

### Rate Limiting
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1643723400
```

## 🔧 SDK & Integration Examples

### Python SDK Example
```python
from ai_media_consultant import Client

# Initialize client
client = Client(api_key="your-api-key")

# Generate content
response = client.content.generate(
    prompt="Create content about our new product launch",
    brand_profile_id="brand-uuid-1",
    platforms=["instagram", "linkedin"]
)

print(f"Request ID: {response.request_id}")

# Check status
status = client.content.get_status(response.request_id)
if status.status == "completed":
    print("Content generated successfully!")
    print(status.content)
```

### JavaScript SDK Example
```javascript
import { AIMediaConsultant } from '@ai-media-consultant/sdk';

const client = new AIMediaConsultant({
  apiKey: 'your-api-key'
});

// Generate content
const response = await client.content.generate({
  prompt: 'Create content about our new product launch',
  brandProfileId: 'brand-uuid-1',
  platforms: ['instagram', 'linkedin']
});

console.log('Request ID:', response.requestId);

// Check status
const status = await client.content.getStatus(response.requestId);
if (status.status === 'completed') {
  console.log('Content generated successfully!');
  console.log(status.content);
}
```

### cURL Examples
```bash
# Generate content
curl -X POST "https://api.aimediacons.com/v1/content/generate" \
  -H "Authorization: Bearer your-jwt-token" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Create content about our new product launch",
    "brand_profile_id": "brand-uuid-1",
    "platforms": ["instagram", "linkedin"]
  }'

# Check generation status
curl -X GET "https://api.aimediacons.com/v1/content/requests/content-request-uuid" \
  -H "Authorization: Bearer your-jwt-token"
```

---

**For additional support or questions about the API, please contact our developer support team at api-support@aimediacons.com**
