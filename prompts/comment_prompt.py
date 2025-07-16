class CommentPrompt:
    
    def get_prompt(self, comments_dict_llm):
        return f"""
Analyze these Reddit comments to understand the user's personality and behavior patterns.

## WHAT TO LOOK FOR:

### 1. INTERESTS & TOPICS
- What subjects do they comment about most?
- What topics make them most engaged?

### 2. COMMUNICATION STYLE
- Are they helpful, argumentative, or neutral?
- Do they write long detailed responses or short ones?
- Are they formal or casual in their language?
- Do they use humor, sarcasm, or stay serious?

### 3. PERSONALITY TRAITS
- Are they confident or hesitant in their opinions?
- Do they seem knowledgeable or ask questions?
- Are they supportive or critical of others?
- How do they handle disagreements?

### 4. BEHAVIOR PATTERNS
- Do they provide sources or evidence?
- Do they ask follow-up questions?
- Do they correct others or share personal experiences?
- Are they active in discussions or just drop quick comments?

## OUTPUT FORMAT:
For each trait you identify, provide:
- **Trait**: What you observed
- **Evidence**: Direct quote from their comment
- **Confidence**: How sure you are (1-10)

## EXAMPLE OUTPUT:
**Trait**: Helpful and Educational
**Evidence**: "I can explain this better - here's a step-by-step guide..."

**Trait**: Uses Humor
**Evidence**: "Well, that escalated quickly"

## ANALYZE THESE COMMENTS:
{comments_dict_llm}
"""