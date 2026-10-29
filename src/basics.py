"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.
    
    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    if a < 0 or c < 0 or g < 0 or t < 0:
        raise ValueError("Base counts cannot be negative.")

    total = a + c + g + t

    if total == 0:
        raise ValueError("Total base count cannot be zero.")

    gc = ((g + c) / total) * 100
    return gc
    

def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    report = f"{sample}: {length} bases, GC {gc:.1f}%"
    return report

def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    parts = text.replace(",", " ").split()

    if len(parts) != 4:
        raise ValueError("Exactly four counts are required")

    counts = []

    for part in parts:
        try:
            number = int(part)
        except ValueError:
            raise ValueError("Counts must be integers")

        if number < 0:
            raise ValueError("Counts cannot be negative")

        counts.append(number)

    return tuple(counts)