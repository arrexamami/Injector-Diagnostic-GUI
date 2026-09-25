from app.core.models import InjectorTestType
from app.core.simulator import Simulator


def test_live_data_has_expected_points():
    simulator = Simulator()
    data = simulator.get_live_data()
    assert len(data) == 7
    assert data[0].name == "RPM"
    assert data[0].simulated is True


def test_injector_test_simulation():
    simulator = Simulator()
    result = simulator.run_injector_test(InjectorTestType.RESISTANCE)
    assert result.simulated is True
    assert result.passed is True


def test_dtc_records_exist():
    simulator = Simulator()
    dtcs = simulator.read_dtc_codes()
    assert len(dtcs) >= 1
    assert dtcs[0].code == "P0100"


def test_clear_dtc():
    simulator = Simulator()
    initial_count = len(simulator.read_dtc_codes())
    simulator.clear_dtc_codes()
    assert len(simulator.read_dtc_codes()) == 0
