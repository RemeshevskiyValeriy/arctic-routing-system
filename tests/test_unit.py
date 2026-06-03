from routing_service.arctic_routing import calculate_risk, classify_ice


def test_calculate_risk():
    assert calculate_risk(5) == 50


def test_classify_ice_medium():
    assert classify_ice(4) == "medium"
