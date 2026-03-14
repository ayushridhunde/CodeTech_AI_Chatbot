import random

def get_response(user_message):
    # Convert message to lowercase for better matching
    msg = user_message.lower()

    # Context 1: Blockchain & Carbon Credits
    if any(word in msg for word in ["blockchain", "carbon", "solidity"]):
        responses = [
            "Blockchain provides a transparent ledger for tracking carbon credits effectively.",
            "Using Solidity for smart contracts is a key component of your sustainability project.",
            "Your project on blockchain-based carbon tracking is highly relevant for environmental tech."
        ]
        return random.choice(responses)

    # Context 2: AI & ECG Signal Projects
    elif any(word in msg for word in ["ecg", "cnn", "vgg16", "signal"]):
        responses = [
            "CNN architectures like VGG16 are excellent for classifying ECG signals accurately.",
            "Make sure to preprocess the ECG signals before feeding them into your neural network.",
            "Are you focusing on real-time classification for your ECG project?"
        ]
        return random.choice(responses)

    # Context 3: Internships & Professional Experience
    elif any(word in msg for word in ["internship", "codsoft", "machine learning"]):
        return "Your Machine Learning internship at CodSoft is a great way to build your technical portfolio."

    # Context 4: Greetings
    elif any(word in msg for word in ["hi", "hello", "hey"]):
        return "Hello! I am your AI Assistant. Which project should we discuss today?"

    # Context 5: Default Response
    else:
        return "That sounds interesting! Could you tell me more, or would you like to discuss your B.Tech projects?"