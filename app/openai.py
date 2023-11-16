import json
import openai

from flask import (Blueprint, request, jsonify)
from app.openai_client import create_chat_completions, log_chat_completions

bp = Blueprint('openai', __name__, url_prefix='/')


@bp.route('/openai-completion', methods=['POST'])
def register():
    prompt = request.get_json(silent=True).get('prompt')
    if not prompt:
        return jsonify({"error": {'message': 'prompt is required.'}}), 400

    try:
        chat_response = create_chat_completions(prompt)
        log_chat_completions(prompt, chat_response.json(), True)
        return chat_response.dict(), 200
    except openai.APIStatusError as e:
        log_chat_completions(prompt, e.message, False)
        return jsonify(e.response.json()), e.status_code
    except openai.OpenAIError:
        return jsonify({"error": {'message': 'error on create openai client.'}}), 500
