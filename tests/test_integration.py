from routing_service.arctic_routing import build_route


def test_build_route_uses_ice_classification_and_risk_calculation():
    route = build_route("Murmansk", "Dudinka", 4)

    assert route["start"] == "Murmansk"
    assert route["finish"] == "Dudinka"
    assert route["ice_class"] == "medium"
    assert route["risk"] == 40
