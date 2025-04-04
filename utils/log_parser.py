def parse_log(path: str):
    try:
        with open(path, "r") as f:
            lines = f.readlines()[-10:]
        return {"last_lines": lines}
    except Exception as e:
        return {"error": str(e)}
