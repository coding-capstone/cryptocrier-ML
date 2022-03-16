import time

from flask import Flask, request, jsonify

from model.get_history import get_history

application = Flask(__name__)


@application.route('/')
def home():
    return """
    <h1> crypto-crier ML API is functional.</h1>
    <h2> Available routes:</h2>
    <ul>
        <li>/history
        <li>/prediction
    </ul>
    """


@application.route('/history', methods=['GET', 'POST'])
def history():
    history_request = request.json
    result = get_history(history_request)
    return jsonify(result)


@application.route('/prediction', methods=['GET', 'POST'])
def prediction():
    t1_start = time.process_time()
    print('remote address: ', str(request.remote_addr))

    prediction_request = request.json
    result = 'You sent the following prediction request: ' + str(prediction_request)

    t1_stop = time.process_time()
    elapsed_time = t1_stop - t1_start
    print("Elapsed time:", elapsed_time)

    return jsonify("{}".format(result))


if __name__ == "__main__":
    application.run(debug=True)
    # application.run(host="0.0.0.0")
