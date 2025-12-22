from safety import violates_policy
from evaluator import evaluate_interaction


SYSTEM_DISCLAIMER = (
    "⚠️ Educational use only. This system provides general health information "
    "and cannot diagnose, treat, or give medical advice."
)

def generate_response(user_input: str) -> str:
    """
    Generates a safe, policy-aligned response for patient education.
    """
    if violates_policy(user_input):
        return (
            "I can share general health education, but I can’t help with "
            "diagnosis, treatment, medication, or emergency situations.\n\n"
            "Please consult a licensed healthcare professional."
        )

    return (
        f"Here is general educational information related to your question:\n"
        f"- Topic: {user_input}\n\n"
        "For medical decisions, always consult a qualified clinician."
    )

    if __name__ == "__main__":
    print("Patient Education Assistant")
    print(SYSTEM_DISCLAIMER)
    print("\nType 'exit' to quit.\n")

   while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    demographic = input(
        "Optional context (e.g., age group: <18, 18-35, 36-50, 51+ or press Enter): "
    ).strip() or "unknown"

    blocked = violates_policy(user_input)
    response = generate_response(user_input)

    evaluate_interaction(
        user_input=user_input,
        blocked=blocked,
        demographic=demographic
    )

    print("\nAI:", response, "\n")
