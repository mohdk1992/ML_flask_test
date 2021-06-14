from flask import Request
from typing import Dict, Optional


def is_all_float_type(form_data: Dict[str, float]) -> bool:
    """Check if all petal measure values are of type float"""
    return all([
        isinstance(petal_measure, float)
        for _, petal_measure in form_data.items()
    ])


def get_request_errors(request: Request) -> Optional[str]:
    """"Handle request semantics for prediction request"""
    if not request.get("method") == "POST":
        return "Invalid request method used"
        
    request_form: Optional[Dict] = request.get("form")
    if not request_form:
        return "Please enter values in the form"

    if not is_all_float_type(request_form):
        return "Please enter valid petal measure values"

    return None
