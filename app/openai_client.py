import os

from flask import g
from openai import OpenAI

from app.db import get_db


def get_openai_client():
    if 'openai_client' not in g:
        g.openai_client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
    return g.openai_client


def create_chat_completions(message):
    openai_client = get_openai_client()
    return openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )


def log_chat_completions(prompt, chat_response, is_success):
    db = get_db()
    db.execute(
        "INSERT INTO chat_completions (prompt, response, is_success) VALUES (?, ?, ?)",
        (prompt, chat_response, is_success),
    )
    db.commit()
