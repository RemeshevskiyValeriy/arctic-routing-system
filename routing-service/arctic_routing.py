def calculate_risk(ice_level: int) -> int:
    return ice_level * 10


def classify_ice(ice_level: int) -> str:
    if ice_level <= 2:
        return "low"
    if ice_level <= 5:
        return "medium"
    return "high"


def build_route(start: str, finish: str, ice_level: int) -> dict:
    risk = calculate_risk(ice_level)
    ice_class = classify_ice(ice_level)

    return {
        "start": start,
        "finish": finish,
        "ice_level": ice_level,
        "ice_class": ice_class,
        "risk": risk,
        "status": "created",
    }