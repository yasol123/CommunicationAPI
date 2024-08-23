from flask import Blueprint, jsonify
from services.sfmc_service.create_sfmc_client import create_sfmc_client

sfmc_controller = Blueprint('sfmc_controller', __name__)
sfmc_client = create_sfmc_client()

@sfmc_controller.route('/sfmc-data', methods=['GET'])
def get_sfmc_data():
    response = sfmc_client.make_api_request('some/endpoint', 'GET')
    return jsonify(response), 200
