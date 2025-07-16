
class PersonaPrompt:
    
    def get_prompt(self, post_analysis_results, comment_analysis_results):
        return f"""
Create a comprehensive user persona by combining the analysis from their Reddit posts and comments.

## INPUT DATA:
### POST ANALYSIS RESULTS:
{post_analysis_results}

### COMMENT ANALYSIS RESULTS:
{comment_analysis_results}

## CREATE A COMPLETE PERSONA INCLUDING:

### 1. PERSONA OVERVIEW
- Give them a descriptive name/title (like "The Curious Tech Enthusiast")
- Write a 2-3 sentence summary of who they are
- What makes them unique on Reddit?

### 2. CORE INTERESTS (Top 5)
- List their main topics of interest
- Rate each interest by how passionate they seem (1-10)
- Show evidence from posts or comments

### 3. PERSONALITY TRAITS
- How do they communicate? (friendly, serious, sarcastic, etc.)
- Are they confident or hesitant?
- Do they prefer helping others or debating?
- How do they handle disagreements?

### 4. COMMUNICATION STYLE
- Do they write long detailed responses or keep it short?
- Are they formal or casual?
- Do they use humor, emojis, or stay serious?
- How do they interact with others?

### 5. BEHAVIOR PATTERNS
- When are they most active? (if detectable)
- How often do they post/comment?
- Do they cross-post in multiple communities?
- Are they more of a creator or commenter?

### 6. EXPERTISE & KNOWLEDGE AREAS
- What topics do they know a lot about?
- Do they share educational content?
- Are they recognized as helpful in certain communities?

### 7. SOCIAL CHARACTERISTICS
- Are they supportive of others?
- Do they build relationships or just drop comments?
- How do they respond to criticism?
- Are they leaders or followers in discussions?

## OUTPUT FORMAT:

### PERSONA: [Give them a catchy name]

**Summary**: [2-3 sentences describing them]

**Core Interests**:
1. [Interest] - Passion Level: X/10
   - Evidence: "[Quote or example]"
2. [Interest] - Passion Level: X/10
   - Evidence: "[Quote or example]"
[Continue for top 5]

**Personality Traits**:
- **[Trait Name]**: [Description]
  - Evidence: "[Quote or example]"
  - Confidence: X/10

**Communication Style**:
- **Writing Style**: [Description with examples]
- **Interaction Pattern**: [How they engage with others]
- **Tone**: [Formal/casual/humorous/serious]

**Behavior Patterns**:
- **Activity Level**: [Consistent/Occasional/Intense]
- **Content Type**: [Creator/Commenter/Sharer]
- **Community Engagement**: [How they participate]

**Expertise Areas**:
- [Area 1]: [Description with evidence]
- [Area 2]: [Description with evidence]

**Social Characteristics**:
- [How they interact socially with evidence]

**Overall Confidence Score**: X/10
(How confident are you in this persona based on available data?)

## EXAMPLE OUTPUT:

### PERSONA: The Passionate History Teacher

**Summary**: A knowledgeable and enthusiastic educator who loves sharing historical facts and archaeological discoveries. They're patient with learners but can be defensive about historical accuracy.

**Core Interests**:
1. Ancient History - Passion Level: 9/10
   - Evidence: "Posted 15 times about archaeological discoveries"
2. Education - Passion Level: 8/10
   - Evidence: "Always provides detailed explanations in comments"

**Personality Traits**:
- **Patient Educator**: Enjoys explaining complex topics simply
  - Evidence: "Let me break this down step by step..."
  - Confidence: 9/10

**Communication Style**:
- **Writing Style**: Detailed, educational, uses examples
- **Interaction Pattern**: Helpful teacher, corrects misinformation
- **Tone**: Professional but approachable

**Behavior Patterns**:
- **Activity Level**: Consistent daily posting
- **Content Type**: Mix of original educational content and curated historical posts
- **Community Engagement**: Active in multiple history-related subreddits

**Expertise Areas**:
- Ancient Civilizations: Deep knowledge with academic sources
- Archaeological Methods: Understands dating techniques and excavation

**Social Characteristics**:
- Supportive of genuine learners but impatient with ignorance
- Builds reputation as reliable information source
- Respectful in debates but firm on facts

**Overall Confidence Score**: 8/10

## NOW CREATE THE PERSONA:
[This is where the AI will generate the actual persona]
"""