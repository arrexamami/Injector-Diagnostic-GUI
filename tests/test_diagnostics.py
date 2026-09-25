from app.core.models import DtcRecord, DtcStatus
from app.core.diagnostics import DiagnosisEngine


def test_diagnosis_workflow():
    dtc = DtcRecord(
        code="P0100",
        system="Air intake",
        description="Mass Air Flow sensor circuit malfunction",
        status=DtcStatus.STORED,
        possible_causes=["MAF issue"],
        recommended_checks=["Inspect MAF signal"],
    )
    steps = DiagnosisEngine.create_workflow(dtc)
    assert len(steps) == 5
    assert steps[0].stage == "Fault Code"
    assert steps[0].status == "Passed"


def test_diagnosis_workflow_structure():
    dtc = DtcRecord(
        code="P0115",
        system="Engine temperature",
        description="Engine coolant temperature sensor circuit malfunction",
        status=DtcStatus.STORED,
    )
    steps = DiagnosisEngine.create_workflow(dtc)
    stages = [step.stage for step in steps]
    assert "Fault Code" in stages
    assert "Possible Causes" in stages
    assert "Sensor Check" in stages
    assert "Wiring Check" in stages
    assert "Test Result" in stages
