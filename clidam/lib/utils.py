def truncate(s, amount) -> str:
    if len(s) > amount:
        return s[:amount - 3] + "..."
    return s
