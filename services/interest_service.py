from services.api import auth_post


def save_interests(interest_ids):

    response = auth_post(
        "/recommendations/save-interests/",
        data={
            "interest_ids": interest_ids
        }
    )

    return response.json()