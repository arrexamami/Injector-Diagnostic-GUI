from __future__ import annotations

from datetime import datetime
from typing import List

from app.core.models import DtcRecord


class DtcFilterService:
    @staticmethod
    def filter_dtcs(dtcs: List[DtcRecord], text: str = "") -> List[DtcRecord]:
        if not text:
            return dtcs
        query = text.lower().strip()
        return [
            dtc for dtc in dtcs
            if query in dtc.code.lower()
            or query in dtc.system.lower()
            or query in dtc.description.lower()
        ]

    @staticmethod
    def sort_dtcs_by_time(dtcs: List[DtcRecord]) -> List[DtcRecord]:
        return sorted(dtcs, key=lambda x: x.code)
