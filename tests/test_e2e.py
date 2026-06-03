from routing_service.arctic_routing import build_route


def test_full_route_generation_scenario():
    route = build_route("Murmansk", "Dudinka", 3)

    assert route is not None
    assert route["status"] == "created"
    assert route["start"] == "Murmansk"
    assert route["finish"] == "Dudinka"
    assert route["risk"] == 30
