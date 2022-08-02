from pytrivia import Category, Diffculty, Type, Trivia

target = ["results"]


def get_me_question():
    trivia_client = Trivia(True)
    question = trivia_client.request(1, Category.General, Diffculty.Easy, Type.True_False)
    for k, v in question.items():
        if k in target:
            results = v[0]
            return results