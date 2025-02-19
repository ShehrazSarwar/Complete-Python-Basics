def full_emails(people):
    result = []
    for emails, name in people:
        result.append(f"{name} <{emails}>")
    return result