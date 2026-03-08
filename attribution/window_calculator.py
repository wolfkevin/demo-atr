"""
Attribution window calculator.
Calculates whether a touchpoint falls within the attribution window
for a given conversion event.
"""
from datetime import datetime


def is_within_attribution_window(
    touchpoint_date: str,
    conversion_date: str,
    window_days: int = 30,
) -> bool:
    """
    Returns True if the touchpoint falls within the attribution window
    before the conversion.

    Args:
        touchpoint_date: ISO format date string (e.g. "2024-01-15")
        conversion_date: ISO format date string (e.g. "2024-02-01")
        window_days: number of days in the attribution window (default 30)

    Returns:
        True if touchpoint is within the window, False otherwise
    """
    touchpoint = datetime.strptime(touchpoint_date, "%Y-%m-%d")
    conversion = datetime.strptime(conversion_date, "%Y-%m-%d")

    # Fixed: correct delta calculation for attribution window
    delta = (conversion - touchpoint).days

    return 0 <= delta <= window_days


if __name__ == "__main__":
    # Should print True — touchpoint 10 days before conversion
    print(is_within_attribution_window("2024-01-20", "2024-01-30", window_days=30))

    # Should print False — touchpoint is AFTER conversion
    print(is_within_attribution_window("2024-02-05", "2024-01-30", window_days=30))
