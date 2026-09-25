from __future__ import annotations

from typing import List

from app.core.models import DtcRecord, DiagnosisStep


class DiagnosisEngine:
    @staticmethod
    def create_workflow(dtc: DtcRecord) -> List[DiagnosisStep]:
        return [
            DiagnosisStep(
                stage="Fault Code",
                result=f"{dtc.code} - {dtc.description}",
                next_action="Review possible causes",
                status="Passed",
            ),
            DiagnosisStep(
                stage="Possible Causes",
                result=dtc.possible_causes[0] if dtc.possible_causes else "No causes available.",
                next_action="Perform sensor check",
                status="Pending",
            ),
            DiagnosisStep(
                stage="Sensor Check",
                result="Simulation workflow: sensor inspection required.",
                next_action="Perform wiring check",
                status="Pending",
            ),
            DiagnosisStep(
                stage="Wiring Check",
                result="Simulation workflow: wiring/connector inspection required.",
                next_action="Review test result",
                status="Pending",
            ),
            DiagnosisStep(
                stage="Test Result",
                result="No physical test performed in Simulation Mode.",
                next_action="Perform next recommended check on real vehicle",
                status="Needs Inspection",
            ),
        ]
