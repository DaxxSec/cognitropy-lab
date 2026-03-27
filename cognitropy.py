#!/usr/bin/env python3
"""
Cognitropy Engine — Entropy injection for creative workspace generation.

Uses the current date as a seed to deterministically select from a large pool
of domains, techniques, and concept crossovers. Each day produces a unique,
unpredictable combination that forces creative workspace design.

Usage:
    python3 cognitropy.py           # Today's assignment
    python3 cognitropy.py 2026-04-15  # Specific date
"""

import hashlib
import datetime
import sys
import json

# === DOMAIN POOL (200+ unique domains across wildly different fields) ===

DOMAINS = [
    # Sciences
    "marine biology", "volcanology", "mycology", "paleontology", "astrobiology",
    "epidemiology", "quantum physics", "glaciology", "entomology", "seismology",
    "dendrochronology", "limnology", "ethology", "crystallography", "parasitology",
    "arachnology", "speleology", "pedology", "phenology", "virology",

    # Engineering & Technical
    "naval architecture", "acoustic engineering", "hydraulic engineering",
    "biomechanical engineering", "geotechnical engineering", "nuclear reactor ops",
    "wind turbine maintenance", "satellite communications", "fiber optic installation",
    "desalination plant ops", "dam safety inspection", "bridge stress analysis",
    "wastewater treatment", "HVAC system design", "elevator maintenance",
    "power grid management", "railway signaling", "tunnel boring operations",

    # Trades & Crafts
    "watchmaking", "blacksmithing", "glassblowing", "bookbinding", "taxidermy",
    "locksmithing", "gem cutting", "coopering", "thatching", "masonry restoration",
    "letterpress printing", "leatherworking", "pottery", "woodturning",
    "instrument building", "sailmaking", "upholstery", "engraving",
    "stained glass restoration", "clockwork repair",

    # Outdoor & Adventure
    "cave diving", "mountaineering", "falconry", "bushcraft", "ice climbing",
    "paragliding", "deep sea fishing", "orienteering", "storm chasing",
    "wildlife tracking", "mushroom foraging", "beekeeping", "trail building",
    "avalanche forecasting", "wildfire management", "search and rescue",
    "underwater archaeology", "coral reef restoration", "whale watching ops",

    # Food & Agriculture
    "viticulture", "cheesemaking", "sourdough baking", "aquaponics",
    "coffee roasting", "chocolate tempering", "fermentation science",
    "olive oil production", "truffle hunting", "sake brewing",
    "permaculture design", "seed banking", "vertical farming",
    "livestock genetics", "soil microbiome management", "apiary management",
    "hydroponic systems", "heritage grain cultivation",

    # Arts & Creative
    "jazz composition", "stop motion animation", "calligraphy",
    "sound design", "theatrical lighting", "puppetry", "mosaic art",
    "film restoration", "voice acting", "choreography",
    "street photography", "documentary filmmaking", "comic book inking",
    "perfumery", "typography design", "architectural model building",
    "foley artistry", "tattoo design", "neon sign crafting",

    # History & Culture
    "archaeological excavation", "medieval manuscript analysis",
    "nautical history", "industrial archaeology", "numismatics",
    "heraldry", "genealogy research", "oral history collection",
    "museum curation", "artifact conservation", "epigraphy",
    "ancient metallurgy analysis", "battlefield archaeology",
    "historical costume reconstruction", "archival preservation",

    # Medical & Health
    "emergency triage", "prosthetics fitting", "sleep medicine",
    "sports medicine rehab", "toxicology screening", "surgical planning",
    "radiology interpretation", "veterinary dentistry", "epidemiological modeling",
    "physical therapy programming", "herbal pharmacology", "audiometry",
    "optometry practice", "occupational therapy", "trauma surgery planning",

    # Transportation & Logistics
    "air traffic control", "cargo ship loading", "railway dispatching",
    "drone delivery logistics", "port operations", "fleet maintenance scheduling",
    "cold chain logistics", "hazmat transportation", "airport ground ops",
    "canal lock operations", "helicopter emergency services", "space mission planning",
    "submarine navigation", "yacht racing tactics", "convoy planning",

    # Environmental & Earth
    "wetland restoration", "air quality monitoring", "carbon credit verification",
    "ocean current mapping", "soil erosion prevention", "invasive species management",
    "light pollution measurement", "noise pollution mapping", "glacier monitoring",
    "urban heat island analysis", "microplastics sampling", "river rewilding",
    "abandoned mine remediation", "landfill gas management",

    # Security & Intelligence (non-cyber)
    "physical penetration testing", "executive protection", "crisis negotiation",
    "espionage tradecraft", "counterintelligence analysis", "bomb disposal",
    "hostage rescue planning", "surveillance detection", "border security ops",
    "diplomatic security", "witness protection logistics", "prison security audit",
    "maritime piracy prevention", "VIP motorcade planning",

    # Space & Aviation
    "telescope mirror grinding", "asteroid mining planning", "satellite deorbiting",
    "rocket engine testing", "space habitat design", "EVA procedure planning",
    "radio telescope operations", "launch pad refurbishment", "space debris tracking",
    "Mars terrain analysis", "comet composition analysis",

    # Unusual & Niche
    "competitive barbecue judging", "escape room design", "haunted house engineering",
    "roller coaster design", "theme park queue optimization", "zookeeping",
    "circus rigging", "pyrotechnics choreography", "ice rink maintenance",
    "bowling alley mechanics", "pinball machine restoration", "jukebox repair",
    "vintage synthesizer calibration", "pipe organ maintenance",
    "lighthouse keeping", "gondola piloting", "hot air balloon operations",
    "trebuchet engineering", "sundial construction", "weather balloon launches",
]

# === TECHNIQUE/APPROACH MODIFIERS ===
# These force a methodological angle on the domain

TECHNIQUES = [
    "with real-time monitoring dashboards",
    "using evidence chain-of-custody tracking",
    "with decision tree triage workflows",
    "using structured hypothesis testing",
    "with automated anomaly detection",
    "using standardized inspection checklists",
    "with predictive maintenance scheduling",
    "using time-series trend analysis",
    "with multi-source intelligence fusion",
    "using risk scoring matrices",
    "with incident response runbooks",
    "using resource optimization algorithms",
    "with environmental impact assessment",
    "using peer review workflows",
    "with compliance audit trails",
    "using stakeholder communication templates",
    "with failure mode analysis (FMEA)",
    "using root cause analysis frameworks",
    "with capacity planning models",
    "using simulation and scenario testing",
    "with knowledge base and FAQ generation",
    "using apprenticeship progression tracking",
    "with safety protocol enforcement",
    "using cost-benefit analysis frameworks",
    "with geographic/spatial analysis",
    "using Bayesian probability assessment",
    "with timeline reconstruction",
    "using taxonomy and classification systems",
    "with inventory and supply chain tracking",
    "using quality control statistical methods",
]

# === CROSSOVER SPARKS ===
# Forces unexpected domain combinations

SPARKS = [
    "What if {domain1} practitioners used techniques from {domain2}?",
    "Build a workspace that applies {domain2} methodology to {domain1} problems.",
    "A {domain1} expert needs {domain2}-style documentation and tracking.",
    "Create a {domain1} workspace with the rigor and process of {domain2}.",
    "Someone working in {domain1} wants to borrow the analytical framework of {domain2}.",
]


def get_daily_assignment(date_str=None):
    """Generate today's workspace assignment using date-seeded entropy."""
    if date_str:
        today = datetime.date.fromisoformat(date_str)
    else:
        today = datetime.date.today()

    # Create deterministic but unpredictable seed from date
    seed = int(hashlib.sha256(today.isoformat().encode()).hexdigest(), 16)

    # Pick primary domain
    primary_idx = seed % len(DOMAINS)
    primary_domain = DOMAINS[primary_idx]

    # Pick secondary domain (for crossover spark) — ensure it's different
    secondary_seed = int(hashlib.sha256((today.isoformat() + "secondary").encode()).hexdigest(), 16)
    secondary_idx = secondary_seed % len(DOMAINS)
    if secondary_idx == primary_idx:
        secondary_idx = (secondary_idx + 1) % len(DOMAINS)
    secondary_domain = DOMAINS[secondary_idx]

    # Pick technique modifier
    technique_idx = int(hashlib.sha256((today.isoformat() + "technique").encode()).hexdigest(), 16) % len(TECHNIQUES)
    technique = TECHNIQUES[technique_idx]

    # Pick crossover spark
    spark_idx = int(hashlib.sha256((today.isoformat() + "spark").encode()).hexdigest(), 16) % len(SPARKS)
    spark = SPARKS[spark_idx].format(domain1=primary_domain, domain2=secondary_domain)

    # Determine if today is a crossover day (roughly 30% of days)
    crossover_flag = int(hashlib.sha256((today.isoformat() + "crossover").encode()).hexdigest(), 16) % 10
    is_crossover = crossover_flag < 3

    result = {
        "date": today.isoformat(),
        "primary_domain": primary_domain,
        "technique": technique,
        "is_crossover": is_crossover,
        "secondary_domain": secondary_domain if is_crossover else None,
        "spark": spark if is_crossover else None,
        "day_number": (today - datetime.date(2026, 3, 26)).days + 1,
    }

    return result


def format_assignment(assignment):
    """Pretty-print the daily assignment."""
    lines = []
    lines.append(f"{'='*60}")
    lines.append(f" COGNITROPY — Day {assignment['day_number']} Assignment")
    lines.append(f" Date: {assignment['date']}")
    lines.append(f"{'='*60}")
    lines.append(f"")
    lines.append(f" Primary Domain: {assignment['primary_domain'].upper()}")
    lines.append(f" Technique:      {assignment['technique']}")
    lines.append(f"")

    if assignment['is_crossover']:
        lines.append(f" ** CROSSOVER DAY **")
        lines.append(f" Secondary Domain: {assignment['secondary_domain']}")
        lines.append(f" Spark: {assignment['spark']}")
        lines.append(f"")
        lines.append(f" Your mission: Build an agent workspace that fuses these")
        lines.append(f" two domains in a way that's genuinely useful.")
    else:
        lines.append(f" Your mission: Build an agent workspace for")
        lines.append(f" {assignment['primary_domain']} {assignment['technique']}.")

    lines.append(f"")
    lines.append(f"{'='*60}")

    return "\n".join(lines)


if __name__ == "__main__":
    date_arg = sys.argv[1] if len(sys.argv) > 1 else None
    assignment = get_daily_assignment(date_arg)

    # Print human-readable
    print(format_assignment(assignment))

    # Also output JSON for programmatic use
    print("\n--- JSON ---")
    print(json.dumps(assignment, indent=2))
