from voluptuous import Schema, PREVENT_EXTRA, Length, All


def is_email_true(email):
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("Это не email")


user_schema = Schema(
    {
        "id": int,
        "email": All(str, is_email_true),
        "first_name": str,
        "last_name": str,
        "avatar": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([user_schema], Length(min=1)),
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)
