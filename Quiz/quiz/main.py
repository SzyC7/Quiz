from flask import Blueprint, render_template, redirect, request, session
from flask_login import login_required, current_user
from quiz.client import get_me_question
from quiz import db
from quiz.models import User, Score
from quiz.utilities import check_answers, total_score

base = Blueprint("base", __name__)


@base.route("/")
def index():
    users = User.query.all()

    return render_template("index.html", users=users)


@base.route("/admin/")
@login_required
def admin_index():
    users = User.query.all()

    return render_template("admin_index.html", users=users)


@base.route("/admin/delete/<username>")
@login_required
def terminator(username):

    user = User.query.filter_by(username=username).first()

    db.session.delete(user)
    db.session.commit()

    return redirect("admin_index.html")


@base.route("/profile/", methods=["GET"])
@login_required
def profile():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    scores = Score.query.filter_by(user_id=user.id).all()
    total = total_score(user, scores)

    return render_template("profile.html", username=username, scores=scores, total=total)


@base.route("/trivia/", methods=["GET"])
@login_required
def trivia():
    question = get_me_question()
    session["q"] = question
    return render_template("trivia.html", username=current_user.username, question=question)


@base.route("/trivia/check/", methods=["POST"])
@login_required
def correct():
    username = current_user.username
    user = User.query.filter_by(username=username).first()

    quest = session.get("q", None)

    if request.form["my_answer"] == quest["correct_answer"]:
        answers = request.form["my_answer"]
        check_answers(answers, quest, user)
    else:
        answers = request.form["my_answer"]
        check_answers(answers, quest, user)
    return redirect("/trivia/")