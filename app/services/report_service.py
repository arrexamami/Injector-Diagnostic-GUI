from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import List

from app.core.models import DtcRecord


class ReportService:
    @staticmethod
    def export_dtc_report(path: str, dtcs: List[DtcRecord]) -> str:
        file_path = Path(path)
        with file_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(["code", "system", "description", "status"])
            for dtc in dtcs:
                writer.writerow([dtc.code, dtc.system, dtc.description, dtc.status.value])
        return str(file_path)

    @staticmethod
    def export_session_summary(path: str, session_name: str, vehicle: str) -> str:
        file_path = Path(path)
        with file_path.open("w", encoding="utf-8") as handle:
            handle.write(f"Session Name: {session_name}\n")
            handle.write(f"Vehicle: {vehicle}\n")
            handle.write(f"Generated At: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            handle.write("Status: Simulation mode\n")
        return str(file_path)
