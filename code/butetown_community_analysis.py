"""
Butetown Community Impact — Data Analysis
===========================================
Research synthesis on crime, deprivation (WIMD), and community sport
programmes in Butetown, Cardiff.

Charts: scripts/generate_butetown_charts.py
Police API: scripts/fetch_police_crimes.py → data/police/butetown_crimes.json
Maps: scripts/generate_butetown_police_maps.py → public/.../crime-map.html
Portfolio: content/projects/butetown-community-impact.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# ── Published statistics (research report, 2025–2026) ─────────────────────────

@dataclass(frozen=True)
class ButetownStats:
    crime_rate_per_1000: int = 260
    pct_above_wales: float = 38.0
    pct_above_uk: float = 32.0
    incidents_sep_2025: int = 278
    wimd_rank: int = 87
    wimd_total_areas: int = 1909
    pl_kicks_funding_gbp: int = 474_928


STATS = ButetownStats()


CLUBS = [
    {
        "name": "Tiger Bay Amateur Boxing Club",
        "founded": 2018,
        "weekly_reach": 200,
        "focus": "Mental health, mentorship, knife crime reduction (Youth Endowment Fund)",
    },
    {
        "name": "Tiger Bay FC / Tiger Bay Youth Development",
        "founded": 2009,
        "weekly_reach": 100,
        "focus": "Inclusive youth football, 8–16, parents & schools engagement",
    },
    {
        "name": "AFC Butetown / Cardiff Bay Warriors",
        "founded": 2005,
        "weekly_reach": None,
        "focus": "Leadership pipeline, representing fathers' and grandfathers' areas",
    },
    {
        "name": "Cardiff City FC Foundation — Premier League Kicks",
        "founded": None,
        "weekly_reach": None,
        "focus": "Free football, mentoring, life skills — Butetown site at Cardiff & Vale College",
    },
]


def crime_vs_benchmarks(stats: ButetownStats = STATS) -> dict[str, float]:
    """Derive implied Wales and UK average crime rates from Butetown uplift."""
    wales = stats.crime_rate_per_1000 / (1 + stats.pct_above_wales / 100)
    uk = stats.crime_rate_per_1000 / (1 + stats.pct_above_uk / 100)
    return {"butetown": stats.crime_rate_per_1000, "wales": wales, "uk": uk}


def wimd_percentile(stats: ButetownStats = STATS) -> float:
    """Higher percentile = more deprived (rank 1 is worst)."""
    return 100 * (1 - (stats.wimd_rank - 1) / stats.wimd_total_areas)


def print_report(stats: ButetownStats = STATS) -> None:
    benchmarks = crime_vs_benchmarks(stats)
    print("=" * 60)
    print("BUTETOWN COMMUNITY IMPACT — DATA SUMMARY")
    print("=" * 60)
    print(f"\nCrime rate: {stats.crime_rate_per_1000}/1,000")
    print(f"  vs Wales (+{stats.pct_above_wales}%): ~{benchmarks['wales']:.0f}/1,000")
    print(f"  vs UK (+{stats.pct_above_uk}%):     ~{benchmarks['uk']:.0f}/1,000")
    print(f"  Sep 2025 incidents: {stats.incidents_sep_2025}")
    print(f"\nWIMD rank: {stats.wimd_rank} of {stats.wimd_total_areas}")
    print(f"  Deprivation percentile: top {100 - wimd_percentile(stats):.1f}% most deprived")
    print(f"\nPL Kicks funding: £{stats.pl_kicks_funding_gbp:,}")
    print("\nCommunity clubs:")
    for c in CLUBS:
        reach = f"{c['weekly_reach']}+/week" if c["weekly_reach"] else "programme-wide"
        print(f"  • {c['name']} ({reach}) — {c['focus']}")
    print("=" * 60)


if __name__ == "__main__":
    print_report()
