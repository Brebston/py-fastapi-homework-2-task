import datetime

from fastapi import HTTPException


def validate_movie_business_rules(data: dict, movie=None):
    if not data:
        raise HTTPException(status_code=400, detail="Invalid input data.")

    if "score" in data:
        value = data["score"]
        if value < 0 or value > 100:
            raise HTTPException(status_code=400, detail="Invalid input data.")

    if "budget" in data and "revenue" in data:
        budget, revenue = data["budget"], data["revenue"]
        if budget < 0 or revenue < 0:
            raise HTTPException(status_code=400, detail="Invalid input data.")

    if "name" in data:
        value = data["name"]
        value = value.strip()
        if not value or len(value) > 255:
            raise HTTPException(status_code=400, detail="Invalid input data.")

    if "date" in data:
        value = data["date"]
        max_date = datetime.date.today() + datetime.timedelta(days=365)
        if value > max_date:
            raise HTTPException(status_code=400, detail="Invalid input data.")

    if "country" in data:
        value = data["country"]
        value = value.strip().upper()
        if len(value) != 3:
            raise HTTPException(status_code=400, detail="Invalid input data.")
