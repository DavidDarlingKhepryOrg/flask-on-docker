import json

from typing import Any, Dict, Tuple

from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for, Request, Response


api = Blueprint(name='api',
                import_name=__name__,
                url_prefix='/api')


@api.route('/users', methods=['GET'])
def get_users() -> Tuple[Response, int]:
    response_object = {'status': 'success'}
    return jsonify(response_object), 200

