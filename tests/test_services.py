from app.core.models import InjectorTestType, ConnectionMode
from app.core.simulator import Simulator
from app.services.ecu_service import EcuService
from app.services.injector_service import InjectorService


def test_ecu_service_reads_dtcs():
    simulator = Simulator()
    service = EcuService(simulator)
    dtcs = service.read_dtc_codes()
    assert len(dtcs) >= 1
    assert dtcs[0].code == "P0100"


def test_ecu_service_status_simulation():
    simulator = Simulator()
    service = EcuService(simulator)
    status = service.get_status_text(simulator.communication)
    assert status == "SIMULATION MODE"


def test_injector_service_runs_test():
    simulator = Simulator()
    service = InjectorService(simulator)
    result = service.run_test(InjectorTestType.RESISTANCE)
    assert result.passed is True
    assert result.simulated is True
    assert result.measured_value == 12.4


def test_all_injector_tests():
    simulator = Simulator()
    service = InjectorService(simulator)
    for test_type in InjectorTestType:
        result = service.run_test(test_type)
        assert result.simulated is True
        assert result.passed is True
