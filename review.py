import ollama 

def review_code(code: str, language: str) -> str:
    prompt = f"""You are a senior software engineer doing a thorough code review.

Language: {language}

Code:
{code}

Review the code and structure your response under these exact headings:

BUGS
List any actual bugs, logic errors, or broken functionality. If none, write "None found."

WARNINGS
List potential issues, edge cases, or risky patterns that may cause problems.

IMPROVEMENTS
Suggest concrete refactors, optimizations, or better approaches.

BEST PRACTICES
Point out violations of language conventions, naming, structure, or code style.

TIME COMPLEXITY
Analyze and provide the time complexity of the code. Mention worst-case complexity (Big-O) and give a short explanation.

SPACE COMPLEXITY
Analyze and provide the space complexity of the code. Mention auxiliary space used and give a short explanation.

SUMMARY
A 2-3 sentence overall assessment of the code quality.

Be specific, direct, and reference actual line content where possible."""

    response = ollama.chat(
        model="codellama:latest",   
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]