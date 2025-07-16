class SystemPrompt:
    
    def get_prompt(self):
        return """

## PRIMARY ATTRIBUTES (Required):

### 1. CONTENT ANALYSIS
- **Primary Topics** (Top 5): Extract main interest areas with relevance scores (1-10)
- **Content Quality**: Original vs. reposts, depth of knowledge
- **Expertise Areas**: Topics where user demonstrates deep knowledge

### 2. COMMUNICATION STYLE
- **Tone Dimensions** (1-10 scale):
  - Assertiveness: Passive(1) → Aggressive(10)
  - Formality: Casual(1) → Professional(10)
  - Emotionality: Neutral(1) → Highly Emotional(10)
- **Response Patterns**: Length, detail level, use of sources/links

### 3. BEHAVIORAL PATTERNS
- **Engagement Style**: Commenter/Creator/Cross-poster
- **Interaction Type**: Helpful/Argumentative/Informative/Social
- **Community Participation**: Follows rules, engages with discussions

### 4. TEMPORAL PATTERNS
- **Posting Schedule**: Most active hours (with timezone if detectable)
- **Activity Consistency**: Regular/Occasional/Intense
- **Response Speed**: Fast responder vs. thoughtful delayed responses

### 5. SOCIAL INDICATORS
- **Demographics** (inferred only if clearly evident):
  - Approximate age range
  - Geographic location (if mentioned)
  - Professional/educational background
- **Life Stage Indicators**: Student/Professional/Retired/Parent

## SCORING METHODOLOGY:
- Each attribute gets a confidence score (1-10)
- Provide evidence citations for scores above 7
- Include uncertainty indicators for ambiguous traits

## OUTPUT FORMAT:
Structured persona with confidence levels and evidence citations.
"""
