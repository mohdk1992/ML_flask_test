from typing import Optional, Dict, List
from flask import Flask, Request, Response, render_template

import sys
sys.path.append("services")

from services.error_service import get_request_errors
from services.prediction_service import get_prediction

app = Flask(__name__)


@app.route("/")
def render_home_page():
    return render_template("home.html")


@app.route("/predict/", methods=["GET","POST"])
def predict(request: Request):
    
    request_error: Optional[str] = get_request_errors(request)
    
    if not request_error:
        petal_measures: Dict[str, float] = request.get("form")
        prediction: str = get_prediction(petal_measures)
        return render_template("predict.html", prediction = prediction)

    return request_error


if __name__ == "__main__":
    app.run(debug=True)