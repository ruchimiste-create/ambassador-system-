# Smart Ambassador

def safe_int_input(prompt, default=0):
    value = input(prompt)
    if value.strip() == "":
        return default
    try:
        return int(value)
    except:
        print("Invalid input! Using default value:", default)
        return default


def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["tired", "frustrated", "demotivated"]):
        return "Demotivated"
    elif any(word in text for word in ["happy", "excited", "good"]):
        return "Motivated"
    else:
        return "Neutral"


def calculate_score(tasks, consistency, repos):
    raw = (tasks * 5) + (consistency * 3) + (repos * 2)
    return min(raw, 100)  # keep max 100


def appreciation(score):
    if score >= 80:
        return " Excellent work! You're a top performer!"
    elif score >= 50:
        return " Good job! Keep improving!"
    else:
        return " Don't worry, stay consistent and grow!"


def classify_personality(tasks, consistency):
    if tasks > 8 and consistency > 7:
        return "Hustler"
    elif tasks <= 5 and consistency > 7:
        return "Strategist"
    elif consistency < 4:
        return "Inactive"
    else:
        return "Balanced"


def github_feedback(repos):
    if repos >= 8:
        return "Strong GitHub profile "
    elif repos >= 4:
        return "Decent GitHub profile"
    else:
        return "Weak GitHub profile - build more projects"


def recommend_tasks(personality, mood):
    if mood == "Demotivated":
        return ["Take a short break", "Do 1 easy task", "Build momentum"]

    if personality == "Hustler":
        return ["Lead campaigns", "Handle referrals"]
    elif personality == "Strategist":
        return ["Create content", "Plan campaigns"]
    elif personality == "Inactive":
        return ["Start with 1 simple task", "Join team activity"]
    else:
        return ["Try mixed tasks (referral and content)"]


def future_prediction(consistency):
    if consistency > 7:
        return "High growth expected "
    elif consistency < 4:
        return "Risk of drop "
    else:
        return "Stable performance"


def main():
    print("\n     Smart Ambassador \n")

    name = input("Enter your name: ") or "User"

    tasks = safe_int_input("Tasks completed this week: ", 0)
    consistency = safe_int_input("Consistency score (1-10): ", 5)
    repos = safe_int_input("Number of GitHub repositories: ", 1)

    mood_input = input("How are you feeling today? ") or "normal"

    mood = detect_mood(mood_input)
    personality = classify_personality(tasks, consistency)
    score = calculate_score(tasks, consistency, repos)
    praise = appreciation(score)
    github = github_feedback(repos)
    recommendations = recommend_tasks(personality, mood)
    future = future_prediction(consistency)


    print("       ANALYSED REPORT")
    print("                                 ")
    print(f"Name: {name}")
    print(f"Score: {score}/100")
    print(f"Personality: {personality}")
    print(f"Mood: {mood}")
    print(f"GitHub: {github}")
    print(f"Future: {future}")

    print("\n Appreciation:")
    print(praise)

    print("\n Recommendations:")
    for r in recommendations:
        print(f"- {r}")

    print("\n Keep growing!\n")


if __name__ == "__main__":
    main()
