from __future__ import annotations

from typing import List

from app.core.diagnostics import DiagnosisEngine
from app.core.models import DtcRecord, DiagnosisStep


class DiagnosisService:
    def __init__(self) -> None:
        self.engine = DiagnosisEngine()

    def create_workflow(self, dtc: DtcRecord) -> List[DiagnosisStep]:
        return self.engine.create_workflow(dtc)
