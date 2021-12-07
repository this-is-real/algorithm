import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z\d\-_.]+", "", new_id)
    new_id = re.sub(r"[.]{2,}", ".", new_id)
    new_id = re.sub(r"^[.]{1}|[.]{1}$", "", new_id)
    new_id = "a" if new_id == "" else new_id
    new_id = new_id[:15] if len(new_id) >= 16 else new_id
    new_id = re.sub(r"[.]{1}$", "", new_id)
    new_id = new_id + new_id[-1]*(3-len(new_id)) if len(new_id) <= 2 else new_id
    return new_id