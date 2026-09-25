from app.core.models import DtcRecord, DtcStatus
from app.core.simulator import Simulator
from app.services.filter_service import DtcFilterService
from app.services.report_service import ReportService


def test_filter_service():
    simulator = Simulator()
    result = DtcFilterService.filter_dtcs(simulator.read_dtc_codes(), "p0100")
    assert len(result) == 1


def test_report_service_exports_csv(tmp_path):
    simulator = Simulator()
    path = tmp_path / "report.csv"
    exported = ReportService.export_dtc_report(str(path), simulator.read_dtc_codes())
    assert path.exists()
    assert exported.endswith("report.csv")


def test_session_creation():
    simulator = Simulator()
    session = simulator.create_session("Workshop Test")
    assert session.name == "Workshop Test"
    assert len(simulator.get_sessions()) == 1


def test_alerts_added():
    simulator = Simulator()
    simulator.add_alert("Warning", "Connection issue", "Warning")
    assert len(simulator.get_alerts()) == 1
