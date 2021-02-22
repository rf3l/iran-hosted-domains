import re


def cleanup(text: str) -> str:
    text = text.lower()

    # Remove http://, https:// and www.
    text = re.sub("(http(s)?://)?(www\\.)?", "", text)

    # Remove everything after /
    text = re.sub("^(.+)/.*$", "\1", text)

    return text


def is_ip(text: str) -> bool:
    return bool(
        re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", text)
    )


def is_ir(text: str) -> bool:
    return bool(re.match(r"^(.+)\.ir$", text))


def is_url(text: str) -> bool:
    return bool(re.match(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", text))
