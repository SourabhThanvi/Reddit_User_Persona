class PostPrompt:
    
    def get_prompt(self, posts_dict_llm):
        return f"""
Analyze these Reddit posts to understand the user's interests, personality, and content creation style.

## WHAT TO LOOK FOR:

### 1. MAIN INTERESTS
- What topics do they post about most?
- Are they passionate about specific subjects?
- Do they show expertise in certain areas?

### 2. CONTENT STYLE
- Do they create original content or share others' content?
- Are their posts informative, entertaining, or asking questions?
- Do they write detailed posts or prefer short ones?

### 3. PERSONALITY INDICATORS
- Are they confident in sharing their opinions?
- Do they seek validation or just share information?
- Are they creative, analytical, or practical?

### 4. POSTING BEHAVIOR
- Do they post in multiple communities about the same topic?
- Do they engage with comments on their posts?
- What kind of reaction do they seem to want?

## OUTPUT FORMAT:
For each observation, provide:
- **Trait**: What you noticed
- **Evidence**: Post title or content snippet
- **Confidence**: How sure you are (1-10)

## EXAMPLE OUTPUT:
**Trait**: Passionate about History
**Evidence**: Post title: "Amazing 4000-year-old artifact found in ancient city"
**Confidence**: 9/10

**Trait**: Shares Educational Content
**Evidence**: Post content: "Here's a detailed explanation of how this works..."
**Confidence**: 8/10

**Trait**: Active in Multiple Communities
**Evidence**: Same post shared in r/history, r/archaeology, r/ancientcivilizations
**Confidence**: 10/10

## ANALYZE THESE POSTS:
{posts_dict_llm}
"""