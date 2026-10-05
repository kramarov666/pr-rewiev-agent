from pathlib import Path

from openai import OpenAI

client = OpenAI()

#huy
def read_pr_context():
    context = []
    context.append("FILES CHANGED:")
    for file in Path(".").rglob("*"):
        if file.is_file():
            context.append(str(file))
    return "\n".join(context)


def review_pull_request(context):
    prompt = f"""
You are a senior DevOps reviewer.
Review the following pull request changes.
Identify:
- Risks
- Missing tests
- Infrastructure concerns
Respond with:
- Summary
- Risks
- Recommendations
Context:
{context}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a careful DevOps reviewer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content
