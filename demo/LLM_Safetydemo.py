import os

def safety_guardrails(message):
    """Basic safety filter for dangerous instructions."""
    unsafe_phrases = ["diagnose me", "prescribe", "doses", "drug amount"]
    for phrase in unsafe_phrases:
        if phrase in message.lower():
            return True
    return False


def generate_safe_response(user_input):
    """Simulated safe response (placeholder for real LLM)."""

    if safety_guardrails(user_input):
        return (
            "⚠️ I can provide general health information, "
            "but I cannot diagnose, prescribe, or give medical instructions.\n"
            "Please consult a licensed clinician."
        )

    return (
        f"Here is general educational information related to your question:\n"
        f"- Prompt received: {user_input}\n"
        f"- Always consult a clinician for diagnosis or treatment."
    )


if __name__ == "__main__":
    print("Healthcare LLM Safety Demo\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = generate_safe_response(user_input)
        print("\nAI:", response, "\n")
