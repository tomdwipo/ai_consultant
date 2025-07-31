# 🤖 Agent Specifications - AI Media Consultant Platform

## 🎯 Overview

Detailed specifications untuk setiap AI agent dalam multi-agent system AI Media Consultant Platform, termasuk roles, capabilities, tools, dan interaction patterns.

## 🏗️ Agent Architecture

### Agent Hierarchy
```
Agent Hub (Orchestrator)
├── Content Strategist Agent (Primary)
├── Platform Specialist Agents
│   ├── Instagram Agent
│   ├── LinkedIn Agent
│   └── TikTok Agent
├── Brand Voice Agent (Cross-cutting)
└── Quality Assurance Agent (Final)
```

## 🎨 Content Strategist Agent

### Role & Responsibilities
**Primary Function**: Strategic content planning and audience analysis

**Core Responsibilities**:
- Analyze user prompts and extract key insights
- Identify target audience characteristics
- Determine optimal content themes and pillars
- Suggest content calendar strategies
- Provide competitive analysis insights

### Agent Configuration
```python
content_strategist = Agent(
    name="ContentStrategist",
    role="Content Strategy Expert",
    goal="Create comprehensive content strategies that align with brand objectives and audience needs",
    backstory="""You are a seasoned content strategist with 10+ years of experience 
    in digital marketing. You understand audience psychology, content trends, and 
    brand positioning. You excel at translating business objectives into actionable 
    content strategies.""",
    model="gpt-4o",
    temperature=0.7,
    max_tokens=2000,
    tools=[
        audience_analyzer,
        trend_detector,
        competitor_analyzer,
        content_calendar_planner
    ]
)
```

### Input Processing
**Expected Inputs**:
- User prompt (text)
- Brand profile data (JSON)
- Target platforms (array)
- Additional context (optional)

**Input Validation**:
```python
def validate_strategist_input(data):
    required_fields = ['prompt', 'brand_profile', 'platforms']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    if len(data['prompt']) < 10:
        raise ValueError("Prompt too short, minimum 10 characters")
    
    valid_platforms = ['instagram', 'linkedin', 'tiktok']
    for platform in data['platforms']:
        if platform not in valid_platforms:
            raise ValueError(f"Invalid platform: {platform}")
```

### Output Structure
```json
{
  "strategy": {
    "content_theme": "Product launch announcement",
    "target_audience": {
      "primary": "Tech-savvy professionals aged 25-40",
      "secondary": "Early adopters and innovators"
    },
    "key_messages": [
      "Innovation and efficiency",
      "Cost-effective solution",
      "User-friendly interface"
    ],
    "content_pillars": [
      "Educational content",
      "Behind-the-scenes",
      "User testimonials"
    ],
    "tone_recommendations": {
      "primary_tone": "professional",
      "secondary_tone": "approachable",
      "avoid": ["overly technical", "salesy"]
    }
  },
  "platform_guidance": {
    "instagram": {
      "content_types": ["carousel", "single_post"],
      "optimal_timing": "18:00-20:00",
      "hashtag_strategy": "mix of trending and niche"
    },
    "linkedin": {
      "content_types": ["article", "professional_post"],
      "optimal_timing": "09:00-11:00",
      "engagement_strategy": "thought leadership"
    },
    "tiktok": {
      "content_types": ["educational_video"],
      "optimal_timing": "19:00-21:00",
      "trend_integration": "business transformation"
    }
  },
  "success_metrics": [
    "engagement_rate",
    "reach",
    "brand_awareness",
    "lead_generation"
  ]
}
```

### Tools & Capabilities

#### 1. Audience Analyzer Tool
```python
def audience_analyzer(brand_profile, industry_data):
    """
    Analyze target audience based on brand profile and industry trends
    """
    return {
        "demographics": analyze_demographics(brand_profile),
        "psychographics": analyze_psychographics(brand_profile),
        "pain_points": identify_pain_points(industry_data),
        "content_preferences": get_content_preferences(brand_profile)
    }
```

#### 2. Trend Detector Tool
```python
def trend_detector(platforms, industry):
    """
    Detect current trends relevant to the brand and platforms
    """
    return {
        "trending_topics": get_trending_topics(platforms, industry),
        "hashtag_trends": get_hashtag_trends(platforms),
        "content_format_trends": get_format_trends(platforms),
        "seasonal_trends": get_seasonal_trends()
    }
```

#### 3. Competitor Analyzer Tool
```python
def competitor_analyzer(brand_profile, competitors):
    """
    Analyze competitor content strategies and identify opportunities
    """
    return {
        "competitor_content_analysis": analyze_competitor_content(competitors),
        "content_gaps": identify_content_gaps(competitors),
        "differentiation_opportunities": find_differentiation_opportunities(brand_profile, competitors),
        "best_practices": extract_best_practices(competitors)
    }
```

## 📱 Instagram Agent

### Role & Responsibilities
**Primary Function**: Instagram-optimized content creation

**Core Responsibilities**:
- Generate Instagram carousel posts
- Create single post content with captions
- Suggest Instagram Stories content
- Optimize hashtag strategies
- Provide visual composition guidance

### Agent Configuration
```python
instagram_agent = Agent(
    name="InstagramSpecialist",
    role="Instagram Content Creator",
    goal="Create engaging Instagram content that maximizes reach and engagement",
    backstory="""You are an Instagram marketing expert with deep understanding of 
    the platform's algorithm, visual storytelling, and community engagement. You 
    know how to create content that stops the scroll and drives meaningful interactions.""",
    model="gpt-4o-mini",
    temperature=0.8,
    max_tokens=1500,
    tools=[
        hashtag_generator,
        carousel_creator,
        story_template_generator,
        visual_composition_advisor
    ]
)
```

### Content Generation Patterns

#### Carousel Post Structure
```python
def generate_carousel_post(strategy, brand_voice):
    """
    Generate Instagram carousel post with multiple slides
    """
    return {
        "post_type": "carousel",
        "slides": [
            {
                "slide_number": 1,
                "type": "hook_slide",
                "title": "Eye-catching headline",
                "content": "Compelling opening statement",
                "design_notes": "Bold typography, brand colors"
            },
            {
                "slide_number": 2,
                "type": "content_slide",
                "title": "Main point 1",
                "content": "Detailed explanation",
                "design_notes": "Visual hierarchy, easy to read"
            },
            # ... more slides
            {
                "slide_number": -1,
                "type": "cta_slide",
                "title": "Call to action",
                "content": "Next steps for audience",
                "design_notes": "Clear CTA button, contact info"
            }
        ],
        "caption": generate_caption(strategy, brand_voice),
        "hashtags": generate_hashtags(strategy),
        "posting_tips": get_posting_tips()
    }
```

#### Single Post Structure
```python
def generate_single_post(strategy, brand_voice):
    """
    Generate Instagram single post with caption
    """
    return {
        "post_type": "single_post",
        "content": {
            "main_text": "Engaging post content",
            "hook": "Attention-grabbing opening",
            "body": "Main message and value",
            "cta": "Clear call to action"
        },
        "hashtags": generate_hashtags(strategy),
        "visual_suggestions": {
            "image_type": "product_showcase",
            "composition": "rule_of_thirds",
            "colors": "brand_palette",
            "text_overlay": "minimal_and_readable"
        },
        "engagement_tactics": [
            "Ask question in caption",
            "Use relevant emojis",
            "Tag relevant accounts",
            "Post at optimal time"
        ]
    }
```

### Tools & Capabilities

#### 1. Hashtag Generator
```python
def hashtag_generator(content, industry, audience_size="medium"):
    """
    Generate optimized hashtag mix for Instagram content
    """
    return {
        "trending_hashtags": get_trending_hashtags(industry),
        "niche_hashtags": get_niche_hashtags(content, industry),
        "branded_hashtags": get_branded_hashtags(),
        "community_hashtags": get_community_hashtags(industry),
        "optimal_mix": create_hashtag_mix(audience_size),
        "hashtag_tips": [
            "Use 8-12 hashtags for optimal reach",
            "Mix popular and niche hashtags",
            "Avoid banned or flagged hashtags",
            "Create branded hashtag for campaigns"
        ]
    }
```

#### 2. Visual Composition Advisor
```python
def visual_composition_advisor(content_type, brand_guidelines):
    """
    Provide visual composition guidance for Instagram content
    """
    return {
        "layout_suggestions": get_layout_suggestions(content_type),
        "color_palette": apply_brand_colors(brand_guidelines),
        "typography": get_typography_recommendations(brand_guidelines),
        "visual_hierarchy": create_visual_hierarchy(content_type),
        "accessibility": ensure_accessibility_compliance()
    }
```

## 💼 LinkedIn Agent

### Role & Responsibilities
**Primary Function**: LinkedIn professional content creation

**Core Responsibilities**:
- Generate professional LinkedIn articles
- Create engaging LinkedIn posts
- Develop thought leadership content
- Optimize for professional networking
- Suggest industry-specific insights

### Agent Configuration
```python
linkedin_agent = Agent(
    name="LinkedInSpecialist",
    role="LinkedIn Content Creator",
    goal="Create professional LinkedIn content that builds authority and generates business leads",
    backstory="""You are a LinkedIn marketing strategist who understands professional 
    networking, B2B communication, and thought leadership. You know how to create 
    content that resonates with business professionals and decision makers.""",
    model="gpt-4o",
    temperature=0.6,
    max_tokens=2500,
    tools=[
        article_writer,
        professional_post_creator,
        industry_analyzer,
        networking_optimizer
    ]
)
```

### Content Generation Patterns

#### LinkedIn Article Structure
```python
def generate_linkedin_article(strategy, brand_voice):
    """
    Generate comprehensive LinkedIn article
    """
    return {
        "article": {
            "title": "Compelling professional headline",
            "subtitle": "Supporting description",
            "introduction": {
                "hook": "Attention-grabbing opening",
                "context": "Industry relevance",
                "preview": "What readers will learn"
            },
            "body": [
                {
                    "section": "Main Point 1",
                    "content": "Detailed explanation with examples",
                    "supporting_data": "Statistics or case studies"
                },
                {
                    "section": "Main Point 2",
                    "content": "Additional insights",
                    "supporting_data": "Industry trends"
                }
            ],
            "conclusion": {
                "summary": "Key takeaways",
                "cta": "Professional call to action",
                "engagement_prompt": "Discussion starter"
            }
        },
        "metadata": {
            "word_count": 1200,
            "reading_time": "5 minutes",
            "target_audience": "Business professionals",
            "industry_tags": ["marketing", "technology", "business"]
        },
        "engagement_strategy": {
            "posting_time": "Tuesday 9:00 AM",
            "follow_up_comments": "Engage with commenters within 2 hours",
            "cross_promotion": "Share in relevant LinkedIn groups"
        }
    }
```

#### Professional Post Structure
```python
def generate_professional_post(strategy, brand_voice):
    """
    Generate LinkedIn professional post
    """
    return {
        "post": {
            "hook": "Professional attention-grabber",
            "main_content": "Value-driven content",
            "insights": "Industry-specific insights",
            "cta": "Professional call to action"
        },
        "formatting": {
            "line_breaks": "Use for readability",
            "emojis": "Professional and minimal",
            "bullet_points": "For key information",
            "hashtags": "3-5 industry-relevant tags"
        },
        "engagement_tactics": [
            "Ask thought-provoking question",
            "Share personal experience",
            "Provide actionable advice",
            "Tag relevant industry leaders"
        ]
    }
```

### Tools & Capabilities

#### 1. Industry Analyzer
```python
def industry_analyzer(industry, target_audience):
    """
    Analyze industry trends and professional interests
    """
    return {
        "industry_trends": get_industry_trends(industry),
        "professional_challenges": identify_professional_challenges(industry),
        "thought_leadership_topics": get_thought_leadership_topics(industry),
        "networking_opportunities": find_networking_opportunities(industry),
        "content_preferences": analyze_professional_content_preferences(target_audience)
    }
```

#### 2. Networking Optimizer
```python
def networking_optimizer(content, target_audience):
    """
    Optimize content for professional networking
    """
    return {
        "networking_hooks": create_networking_hooks(content),
        "discussion_starters": generate_discussion_starters(content),
        "collaboration_opportunities": identify_collaboration_opportunities(content),
        "thought_leadership_positioning": position_as_thought_leader(content)
    }
```

## 🎵 TikTok Agent

### Role & Responsibilities
**Primary Function**: TikTok viral content creation

**Core Responsibilities**:
- Generate TikTok video scripts
- Suggest trending sounds and music
- Create viral content hooks
- Optimize for TikTok algorithm
- Provide timing and pacing guidance

### Agent Configuration
```python
tiktok_agent = Agent(
    name="TikTokSpecialist",
    role="TikTok Content Creator",
    goal="Create viral TikTok content that maximizes views and engagement",
    backstory="""You are a TikTok content strategist who understands viral mechanics, 
    trending formats, and Gen Z communication. You know how to create content that 
    captures attention in the first 3 seconds and keeps viewers engaged.""",
    model="gpt-4o-mini",
    temperature=0.9,
    max_tokens=1000,
    tools=[
        script_writer,
        trend_tracker,
        sound_selector,
        viral_optimizer
    ]
)
```

### Content Generation Patterns

#### TikTok Script Structure
```python
def generate_tiktok_script(strategy, brand_voice):
    """
    Generate TikTok video script with timing
    """
    return {
        "script": {
            "hook": {
                "timestamp": "0-3s",
                "content": "Attention-grabbing opening",
                "visual": "Eye-catching visual element",
                "text_overlay": "Compelling text hook"
            },
            "content_beats": [
                {
                    "timestamp": "3-8s",
                    "content": "Main point introduction",
                    "visual": "Supporting visual",
                    "text_overlay": "Key message"
                },
                {
                    "timestamp": "8-12s",
                    "content": "Value delivery",
                    "visual": "Demonstration or example",
                    "text_overlay": "Benefit statement"
                },
                {
                    "timestamp": "12-15s",
                    "content": "Call to action",
                    "visual": "Clear next step",
                    "text_overlay": "CTA text"
                }
            ],
            "outro": {
                "timestamp": "15s",
                "content": "Final hook for replay",
                "visual": "Loop-friendly ending",
                "text_overlay": "Follow for more"
            }
        },
        "production_notes": {
            "total_duration": "15 seconds",
            "pacing": "Fast-paced with quick cuts",
            "transitions": "Smooth and engaging",
            "captions": "Auto-generated with manual review"
        },
        "hashtags": generate_tiktok_hashtags(strategy),
        "sound_suggestions": suggest_trending_sounds(strategy)
    }
```

### Tools & Capabilities

#### 1. Trend Tracker
```python
def trend_tracker(category="business"):
    """
    Track current TikTok trends and viral formats
    """
    return {
        "trending_sounds": get_trending_sounds(category),
        "viral_formats": get_viral_formats(category),
        "trending_hashtags": get_trending_hashtags(category),
        "challenge_opportunities": find_challenge_opportunities(category),
        "trend_predictions": predict_upcoming_trends(category)
    }
```

#### 2. Viral Optimizer
```python
def viral_optimizer(content, target_audience):
    """
    Optimize content for viral potential
    """
    return {
        "hook_optimization": optimize_hook(content),
        "engagement_triggers": add_engagement_triggers(content),
        "algorithm_optimization": optimize_for_algorithm(content),
        "shareability_factors": enhance_shareability(content),
        "viral_score": calculate_viral_potential(content)
    }
```

## 🎭 Brand Voice Agent

### Role & Responsibilities
**Primary Function**: Brand voice consistency across all content

**Core Responsibilities**:
- Maintain consistent brand voice
- Apply brand guidelines to content
- Ensure tone alignment
- Validate brand compliance
- Adapt voice for different platforms

### Agent Configuration
```python
brand_voice_agent = Agent(
    name="BrandVoiceGuardian",
    role="Brand Voice Consistency Expert",
    goal="Ensure all content maintains consistent brand voice and personality",
    backstory="""You are a brand strategist who understands the nuances of brand 
    voice and personality. You ensure that every piece of content reflects the 
    brand's unique character while adapting appropriately for different platforms.""",
    model="gpt-4o-mini",
    temperature=0.3,
    max_tokens=1000,
    tools=[
        brand_analyzer,
        tone_detector,
        style_enforcer,
        voice_adapter
    ]
)
```

### Voice Analysis & Application
```python
def analyze_and_apply_brand_voice(content, brand_profile):
    """
    Analyze content and apply brand voice guidelines
    """
    return {
        "voice_analysis": {
            "current_tone": detect_current_tone(content),
            "brand_alignment": check_brand_alignment(content, brand_profile),
            "consistency_score": calculate_consistency_score(content, brand_profile)
        },
        "voice_adjustments": {
            "tone_modifications": suggest_tone_modifications(content, brand_profile),
            "vocabulary_adjustments": adjust_vocabulary(content, brand_profile),
            "style_improvements": improve_style_consistency(content, brand_profile)
        },
        "platform_adaptations": {
            "instagram": adapt_for_instagram(content, brand_profile),
            "linkedin": adapt_for_linkedin(content, brand_profile),
            "tiktok": adapt_for_tiktok(content, brand_profile)
        }
    }
```

### Tools & Capabilities

#### 1. Brand Analyzer
```python
def brand_analyzer(brand_profile):
    """
    Analyze brand profile and extract voice characteristics
    """
    return {
        "voice_attributes": extract_voice_attributes(brand_profile),
        "tone_preferences": identify_tone_preferences(brand_profile),
        "personality_traits": extract_personality_traits(brand_profile),
        "communication_style": analyze_communication_style(brand_profile),
        "brand_values": extract_brand_values(brand_profile)
    }
```

#### 2. Voice Adapter
```python
def voice_adapter(content, platform, brand_voice):
    """
    Adapt brand voice for specific platform while maintaining consistency
    """
    return {
        "platform_adaptation": adapt_voice_for_platform(content, platform, brand_voice),
        "tone_adjustment": adjust_tone_for_platform(content, platform),
        "style_modification": modify_style_for_platform(content, platform),
        "consistency_check": verify_voice_consistency(content, brand_voice)
    }
```

## ✅ Quality Assurance Agent

### Role & Responsibilities
**Primary Function**: Content quality validation and optimization

**Core Responsibilities**:
- Review content quality and accuracy
- Check grammar and spelling
- Validate platform compliance
- Optimize for engagement
- Ensure brand consistency

### Agent Configuration
```python
qa_agent = Agent(
    name="QualityAssurance",
    role="Content Quality Expert",
    goal="Ensure all content meets high quality standards and platform requirements",
    backstory="""You are a meticulous content editor with expertise in digital 
    marketing, grammar, and platform best practices. You have a keen eye for 
    detail and understand what makes content engaging and effective.""",
    model="gpt-4o",
    temperature=0.2,
    max_tokens=1500,
    tools=[
        grammar_checker,
        engagement_optimizer,
        compliance_validator,
        quality_scorer
    ]
)
```

### Quality Assessment Framework
```python
def assess_content_quality(content, platform, brand_profile):
    """
    Comprehensive quality assessment of generated content
    """
    return {
        "quality_scores": {
            "overall_score": calculate_overall_score(content),
            "grammar_score": check_grammar_quality(content),
            "engagement_score": predict_engagement_potential(content),
            "brand_consistency_score": check_brand_consistency(content, brand_profile),
            "platform_optimization_score": check_platform_optimization(content, platform)
        },
        "quality_issues": {
            "grammar_errors": identify_grammar_errors(content),
            "style_inconsistencies": find_style_inconsistencies(content),
            "engagement_weaknesses": identify_engagement_weaknesses(content),
            "platform_violations": check_platform_violations(content, platform)
        },
        "improvement_suggestions": {
            "grammar_fixes": suggest_grammar_fixes(content),
            "engagement_improvements": suggest_engagement_improvements(content),
            "style_adjustments": suggest_style_adjustments(content),
            "platform_optimizations": suggest_platform_optimizations(content, platform)
        },
        "approval_status": determine_approval_status(content)
    }
```

### Tools & Capabilities

#### 1. Grammar Checker
```python
def grammar_checker(content):
    """
    Check grammar, spelling, and language quality
    """
    return {
        "grammar_errors": identify_grammar_errors(content),
        "spelling_errors": identify_spelling_errors(content),
        "punctuation_issues": check_punctuation(content),
        "readability_score": calculate_readability_score(content),
        "language_quality": assess_language_quality(content)
    }
```

#### 2. Engagement Optimizer
```python
def engagement_optimizer(content, platform):
    """
    Optimize content for maximum engagement
    """
    return {
        "engagement_predictions": predict_engagement_metrics(content, platform),
        "optimization_suggestions": suggest_engagement_optimizations(content, platform),
        "hook_improvements": improve_content_hooks(content),
        "cta_optimization": optimize_call_to_actions(content),
        "timing_recommendations": suggest_optimal_posting_times(content, platform)
    }
```

## 🔄 Agent Interaction Patterns

### Sequential Processing
```python
async def sequential_content_generation(request):
    """
    Sequential agent processing for content generation
    """
    # Step 1: Strategy Development
    strategy = await content_strategist.process(request)
    
    # Step 2: Platform-Specific Generation
    platform_content = {}
    for platform in request.platforms:
        specialist = get_platform_specialist(platform)
        platform_content[platform] = await specialist.generate(strategy, request.brand_profile)
    
    # Step 3: Brand Voice Application
    voice_adjusted_content = await brand_voice_agent.apply_voice(platform_content, request.brand_profile)
    
    # Step 4: Quality Assurance
    final_content = await qa_agent.review_and_optimize(voice_adjusted_content)
    
    return final_content
```

### Parallel Processing
```python
async def parallel_content_generation(request):
    """
    Parallel agent processing for faster generation
    """
    # Step 1: Strategy Development
    strategy = await content_strategist.process(request)
    
    # Step 2: Parallel Platform Generation
    platform_tasks = []
    for platform in request.platforms:
        specialist = get_platform_specialist(platform)
        task = specialist.generate(strategy, request.brand_profile)
        platform_tasks.append(task)
    
    platform_results = await asyncio.gather(*platform_tasks)
    
    # Step 3: Brand Voice and QA in parallel
    voice_task = brand_voice_agent.apply_voice(platform_results, request.brand_profile)
    qa_task = qa_agent.review_and_optimize(platform_results)
    
    voice_result, qa_result = await asyncio.gather(voice_task, qa_task)
    
    # Step 4: Merge results
    final_content = merge_agent_results(voice_result, qa_result)
    
    return final_content
```

### Error Handling & Fallbacks
```python
async def robust_content_generation(request):
    """
    Content generation with error handling and fallbacks
    """
    try:
        return await sequential_content_generation(request)
    except AgentTimeoutError:
        # Fallback to simpler generation
        return await fallback_generation(request)
    except AgentQualityError as e:
        # Retry with adjusted parameters
        adjusted_request = adjust_request_parameters(request, e.quality_issues)
        return await sequential_content_generation(adjusted_request)
    except Exception as e:
        # Log error and return basic content
        log_agent_error(e, request)
        return await basic_content_generation(request)
```

## 📊 Performance Monitoring

### Agent Performance Metrics
```python
def monitor_agent_performance():
    """
    Monitor individual agent performance metrics
    """
    return {
        "response_times": {
            "content_strategist": measure_response_time("content_strategist"),
            "instagram_agent": measure_response_time("instagram_agent"),
            "linkedin_agent": measure_response_time("linkedin_agent"),
            "tiktok_agent": measure_response_time("tiktok_agent"),
            "brand_voice_agent": measure_response_time("brand_voice_agent"),
            "qa_agent": measure_response_time("qa_agent")
        },
        "quality_scores": {
            "average_quality": calculate_average_quality_score(),
            "consistency_score": calculate_consistency_score(),
            "user_satisfaction": get_user_satisfaction_score()
        },
        "error_rates": {
            "timeout_errors": count_timeout_errors(),
            "quality_errors": count_quality_errors(),
            "system_errors": count_system_errors()
        }
    }
```

### Continuous Improvement
```python
def continuous_agent_improvement():
    """
    Continuously improve agent performance based on feedback
    """
    feedback_data = collect_user_feedback()
    performance_data = collect_performance_metrics()
    
    improvements = {
        "prompt_optimization": optimize_agent_prompts(feedback_data),
        "model_fine_tuning": fine_tune_models(performance_data),
        "tool_enhancement": enhance_agent_tools(feedback_data),
        "workflow_optimization": optimize_agent_workflows(performance_data)
    }
    
    return apply_improvements(improvements)
```

---

**These agent specifications provide the foundation for building a robust, scalable, and high-quality multi-agent content generation system.**
