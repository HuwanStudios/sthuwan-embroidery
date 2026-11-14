from dataclasses import dataclass

@dataclass(frozen=True)
class MachineProfile:
    name: str
    max_width_mm: float
    max_height_mm: float
    preferred_format: str

BROTHER_SE600 = MachineProfile(
    name="Brother SE600",
    max_width_mm=100.0,
    max_height_mm=100.0,
    preferred_format="pes",
)

def validate_bounds(width_mm: float, height_mm: float, machine=BROTHER_SE600):
    if width_mm <= 0 or height_mm <= 0:
        raise ValueError("Design dimensions must be positive.")
    if width_mm > machine.max_width_mm or height_mm > machine.max_height_mm:
        raise ValueError(
            f"{width_mm:.1f} x {height_mm:.1f} mm exceeds "
            f"{machine.name} {machine.max_width_mm:.0f} x {machine.max_height_mm:.0f} mm field."
        )
    return True
