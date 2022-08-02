from flask import request, session, flash, redirect
from quiz.models import Score, User
from quiz import db


def check_answers(answers, quest, user):
    if answers == quest["correct_answer"]:
        quiz = Score(
            category=quest["category"], question=quest["question"], level=quest["difficulty"], score=1, user_id=user.id
        )
        db.session.add(quiz)
        db.session.commit()
    else:
        quiz = Score(
            category=quest["category"], question=quest["question"], level=quest["difficulty"], score=0, user_id=user.id
        )
        db.session.add(quiz)
        db.session.commit()


def total_score(user, scores):
    total = 0
    for score in scores:
        total = total + score.score

    user.total = total
    db.session.commit()
    print("db updated")
    return total