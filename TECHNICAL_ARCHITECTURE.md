# 🏗️ Technical Architecture - AI Media Consultant Platform

## 🎯 System Overview

AI Media Consultant menggunakan arsitektur microservices berbasis cloud dengan multi-agent AI system untuk menghasilkan konten media sosial yang optimal untuk berbagai platform.

### Core Principles
- **Scalability**: Horizontal scaling untuk handle traffic growth
- **Modularity**: Loosely coupled services untuk maintainability
- **Reliability**: 99.9% uptime dengan fault tolerance
- **Security**: Enterprise-grade security dan data protection

## 🏛️ High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend Layer                           │
├─────────────────────────────────────────────────────────────────┤
│  Web App (React)  │  Mobile App (React Native)  │  Admin Panel │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway (Kong)                        │
├─────────────────────────────────────────────────────────────────┤
│  Authentication  │  Rate Limiting  │  Load Balancing  │  Logging │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Microservices Layer                         │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│  User Service   │  Content Service│  AI Agent Hub   │  Billing  │
│  (FastAPI)      │  (FastAPI)      │  (Python)       │  Service  │
└─────────────────┴─────────────────┴─────────────────┴───────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data Layer                                │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│  PostgreSQL     │  Redis Cache    │  S3 Storage     │  Vector DB│
│  (User Data)    │  (Sessions)     │  (Assets)       │  (Embeddings)│
└─────────────────┴─────────────────┴─────────────────┴───────────┘
```

## 🤖 AI Agent Architecture

### Multi-Agent System Design

```
                    ┌─────────────────┐
                    │   Agent Hub     │
                    │   Orchestrator  │
                    └─────────────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
    ┌───────▼────┐  ┌──────▼──────┐  ┌─────▼─────┐
    │ Content    │  │ Platform    │  │ Brand     │
    │ Strategist │  │ Specialists │  │ Voice     │
    │ Agent      │  │ Agent       │  │ Agent     │
    └────────────┘  └─────────────┘  └───────────┘
            │               │               │
            └───────────────┼───────────────┘
                            │
                    ┌───────▼────┐
                    │ Quality    │
                    │ Assurance  │
                    │ Agent      │
                    └────────────┘
```

### Agent Specifications

#### 1. Content Strategist Agent
**Framework**: OpenAI Agents SDK
```python
agent = Agent(
    name="ContentStrategist",
    instructions="""
    You are a content strategy expert. Analyze user input and:
    1. Identify target audience
    2. Determine content pillars
    3. Suggest content themes
    4. Recommend posting frequency
    """,
    model="gpt-4o",
    tools=[audience_analyzer, trend_detector, competitor_analyzer]
)
```

#### 2. Platform Specialist Agents
**Framework**: CrewAI for multi-agent coordination

**Instagram Agent**:
```python
instagram_agent = Agent(
    role="Instagram Content Creator",
    goal="Create engaging Instagram content optimized for the platform",
    backstory="Expert in Instagram trends, hashtags, and visual storytelling",
    tools=[hashtag_generator, carousel_creator, story_template]
)
```

**LinkedIn Agent**:
```python
linkedin_agent = Agent(
    role="LinkedIn Content Creator", 
    goal="Create professional LinkedIn content for B2B engagement",
    backstory="Expert in professional networking and thought leadership",
    tools=[article_writer, professional_post_creator, industry_analyzer]
)
```

**TikTok Agent**:
```python
tiktok_agent = Agent(
    role="TikTok Content Creator",
    goal="Create viral TikTok content with trending elements",
    backstory="Expert in short-form video content and viral trends",
    tools=[script_writer, trend_tracker, sound_selector]
)
```

#### 3. Brand Voice Agent
```python
brand_voice_agent = Agent(
    name="BrandVoice",
    instructions="""
    Maintain consistent brand voice across all content:
    1. Analyze brand guidelines
    2. Extract tone and style preferences
    3. Apply voice consistency
    4. Ensure brand alignment
    """,
    model="gpt-4o-mini",
    tools=[brand_analyzer, tone_detector, style_enforcer]
)
```

#### 4. Quality Assurance Agent
```python
qa_agent = Agent(
    name="QualityAssurance",
    instructions="""
    Review and optimize all generated content:
    1. Check grammar and spelling
    2. Verify platform compliance
    3. Ensure engagement optimization
    4. Validate brand consistency
    """,
    model="gpt-4o",
    tools=[grammar_checker, engagement_optimizer, compliance_validator]
)
```

## 🛠️ Technology Stack

### Backend Services
- **Language**: Python 3.11+
- **Framework**: FastAPI
- **AI Framework**: OpenAI Agents SDK, CrewAI
- **Task Queue**: Celery with Redis
- **API Gateway**: Kong
- **Authentication**: JWT with refresh tokens

### Frontend Applications
- **Web App**: React 18 with TypeScript
- **Mobile App**: React Native
- **Admin Panel**: Next.js with Tailwind CSS
- **State Management**: Redux Toolkit

### Databases & Storage
- **Primary Database**: PostgreSQL 15
- **Cache**: Redis 7
- **File Storage**: AWS S3
- **Vector Database**: Pinecone (for embeddings)
- **Search**: Elasticsearch

### Infrastructure
- **Cloud Provider**: AWS
- **Container**: Docker + Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack

### External APIs
- **AI Models**: OpenAI GPT-4, Claude, Gemini
- **Design**: Canva API
- **Social Media**: Instagram Basic Display, LinkedIn API
- **Payment**: Stripe, Midtrans
- **Email**: SendGrid

## 📊 Database Schema

### Core Tables

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    subscription_tier VARCHAR(50) DEFAULT 'starter',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Brand profiles
CREATE TABLE brand_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    brand_name VARCHAR(255) NOT NULL,
    brand_voice JSONB,
    brand_guidelines TEXT,
    target_audience JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Content requests
CREATE TABLE content_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    brand_profile_id UUID REFERENCES brand_profiles(id),
    prompt TEXT NOT NULL,
    platforms TEXT[] NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Generated content
CREATE TABLE generated_content (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    request_id UUID REFERENCES content_requests(id),
    platform VARCHAR(50) NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    content_data JSONB NOT NULL,
    quality_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Usage tracking
CREATE TABLE usage_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## 🔄 Content Generation Workflow

### 1. Request Processing Flow
```python
async def process_content_request(request: ContentRequest):
    # Step 1: Initialize agent hub
    agent_hub = AgentHub()
    
    # Step 2: Content strategy analysis
    strategy = await agent_hub.content_strategist.analyze(
        prompt=request.prompt,
        brand_profile=request.brand_profile,
        target_platforms=request.platforms
    )
    
    # Step 3: Platform-specific generation
    content_tasks = []
    for platform in request.platforms:
        specialist = agent_hub.get_platform_specialist(platform)
        task = specialist.generate_content.delay(
            strategy=strategy,
            platform=platform,
            brand_voice=request.brand_profile.voice
        )
        content_tasks.append(task)
    
    # Step 4: Quality assurance
    generated_content = await asyncio.gather(*content_tasks)
    qa_results = await agent_hub.qa_agent.review_content(generated_content)
    
    # Step 5: Return optimized content
    return qa_results
```

### 2. Agent Coordination with CrewAI
```python
from crewai import Crew, Task

# Define content creation crew
content_crew = Crew(
    agents=[
        content_strategist_agent,
        instagram_agent,
        linkedin_agent,
        tiktok_agent,
        brand_voice_agent,
        qa_agent
    ],
    tasks=[
        Task(
            description="Analyze content requirements and create strategy",
            agent=content_strategist_agent
        ),
        Task(
            description="Generate platform-specific content",
            agent=platform_agents,
            context=[strategy_task]
        ),
        Task(
            description="Ensure brand voice consistency",
            agent=brand_voice_agent,
            context=[content_tasks]
        ),
        Task(
            description="Quality assurance and optimization",
            agent=qa_agent,
            context=[all_previous_tasks]
        )
    ],
    verbose=True
)

# Execute content generation
result = content_crew.kickoff(inputs=request_data)
```

## 🔐 Security Architecture

### Authentication & Authorization
- **JWT Tokens**: Access (15 min) + Refresh (7 days)
- **Role-Based Access Control (RBAC)**
- **API Rate Limiting**: Per user/IP limits
- **OAuth Integration**: Google, LinkedIn SSO

### Data Protection
- **Encryption at Rest**: AES-256
- **Encryption in Transit**: TLS 1.3
- **PII Handling**: GDPR compliant
- **API Security**: OWASP guidelines

### Infrastructure Security
- **VPC**: Private subnets for databases
- **WAF**: Web Application Firewall
- **DDoS Protection**: CloudFlare
- **Secrets Management**: AWS Secrets Manager

## 📈 Scalability & Performance

### Horizontal Scaling
- **Load Balancers**: Application Load Balancer
- **Auto Scaling**: Based on CPU/memory metrics
- **Database Scaling**: Read replicas + connection pooling
- **Cache Strategy**: Multi-level caching

### Performance Optimization
- **CDN**: CloudFront for static assets
- **Database Indexing**: Optimized queries
- **Async Processing**: Celery for heavy tasks
- **Connection Pooling**: pgbouncer for PostgreSQL

### Monitoring & Observability
```python
# Performance monitoring
from prometheus_client import Counter, Histogram, Gauge

# Metrics
content_generation_counter = Counter('content_generated_total', 'Total content generated')
generation_time_histogram = Histogram('content_generation_duration_seconds', 'Time spent generating content')
active_users_gauge = Gauge('active_users', 'Number of active users')

# Usage in code
@generation_time_histogram.time()
async def generate_content(request):
    content = await ai_agent.generate(request)
    content_generation_counter.inc()
    return content
```

## 🚀 Deployment Architecture

### Container Strategy
```dockerfile
# Multi-stage build for optimization
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-consultant-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-consultant-api
  template:
    metadata:
      labels:
        app: ai-consultant-api
    spec:
      containers:
      - name: api
        image: ai-consultant:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
```

## 🔧 Development Workflow

### Local Development Setup
```bash
# Clone repository
git clone https://github.com/your-org/ai-consultant.git
cd ai-consultant

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your API keys

# Run database migrations
alembic upgrade head

# Start development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Testing Strategy
```python
# Unit tests with pytest
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_content_generation():
    response = client.post("/api/v1/content/generate", json={
        "prompt": "Create content about sustainable fashion",
        "platforms": ["instagram", "linkedin"],
        "brand_profile_id": "test-brand-id"
    })
    assert response.status_code == 200
    assert "content" in response.json()

# Integration tests for AI agents
@pytest.mark.asyncio
async def test_agent_coordination():
    agent_hub = AgentHub()
    result = await agent_hub.process_request(test_request)
    assert result.quality_score > 0.8
```

## 📊 Performance Benchmarks

### Target Performance Metrics
- **API Response Time**: < 200ms (95th percentile)
- **Content Generation**: < 30 seconds
- **System Uptime**: 99.9%
- **Concurrent Users**: 10,000+
- **Database Queries**: < 100ms average

### Load Testing
```python
# Locust load testing
from locust import HttpUser, task, between

class ContentGenerationUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def generate_content(self):
        self.client.post("/api/v1/content/generate", json={
            "prompt": "Create engaging social media content",
            "platforms": ["instagram"]
        })
    
    @task(3)
    def get_user_content(self):
        self.client.get("/api/v1/content/history")
```

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest
    - name: Run tests
      run: pytest
    
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to production
      run: |
        kubectl apply -f k8s/
        kubectl rollout status deployment/ai-consultant-api
```

---

**This technical architecture serves as the foundation for building a scalable, reliable, and maintainable AI Media Consultant platform.**
