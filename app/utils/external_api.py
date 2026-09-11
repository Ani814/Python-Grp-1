"""
External API integration.

Uses the free, keyless Frankfurter currency API (https://www.frankfurter.app)
to convert a job's listed salary (assumed GEL) into USD and EUR, so the
job detail page can show live, dynamically-fetched figures.
"""
import requests
from app.utils.logger import job_logger

FRANKFURTER_URL = "https://api.frankfurter.app/latest"


def convert_salary(amount, base_currency="GEL", targets=("USD", "EUR")):
    """
    Returns a dict like {"USD": 370.5, "EUR": 340.2} or None on failure.
    Any failure (network, bad response, timeout) is logged as an
    'API request error', per the assignment's logging requirement.
    """
    if amount is None:
        return None

    try:
        response = requests.get(
            FRANKFURTER_URL,
            params={"amount": amount, "from": base_currency, "to": ",".join(targets)},
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("rates")
    except requests.RequestException as exc:
        job_logger.error(f"API request error (currency conversion): {exc}")
        return None
    except (ValueError, KeyError) as exc:
        job_logger.error(f"API request error (bad response parsing): {exc}")
        return None
