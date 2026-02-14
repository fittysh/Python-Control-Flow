import random


def get_magic_ball_answer(random_number: int) -> str:
    """Return a Magic 8-Ball answer based on a random number."""
    if random_number == 1:
        return "Yes - definitely."
    elif random_number == 2:
        return "It is decidedly so."
    elif random_number == 3:
        return "Without a doubt."
    elif random_number == 4:
        return "Reply hazy, try again."
    elif random_number == 5:
        return "Ask again later."
    elif random_number == 6:
        return "Better not tell you now."
    elif random_number == 7:
        return "My sources say no."
    elif random_number == 8:
        return "Outlook not so good."
    elif random_number == 9:
        return "Very doubtful."
    elif random_number == 10:
        return "I'm happy looking at you."
    elif random_number == 11:
        return "Do your best!"
    else:
        return "Error"


def main() -> None:
    name = "Joe"
    question = "Will I love you?".strip()

    if question == "":
        print("Please write the question before pressing Enter.")
        return

    random_number = random.randint(1, 11)
    answer = get_magic_ball_answer(random_number)

    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}")


if __name__ == "__main__":
    main()
