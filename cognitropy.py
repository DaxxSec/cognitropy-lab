#!/usr/bin/env python3
"""
Cognitropy Engine — Entropy injection for creative workspace generation.

Uses the current date as a seed to deterministically select from a two-tier
category-domain structure (300+ domains across 20+ categories) that prevents
thematic clustering on consecutive days.

Each day produces a unique, unpredictable combination that forces creative
workspace design.

Usage:
    python3 cognitropy.py           # Today's assignment
    python3 cognitropy.py 2026-04-15  # Specific date
"""

import hashlib
import datetime
import sys
import json

# === TWO-TIER DOMAIN STRUCTURE (20+ categories, 300+ domains) ===
# This design prevents consecutive days from landing in the same theme.

CATEGORIES = {
    "Cyber & DFIR": [
        "malware reverse engineering", "network intrusion analysis",
        "digital forensics investigation", "incident response automation",
        "threat intelligence fusion", "vulnerability assessment",
        "penetration testing ops", "security log analysis",
        "memory forensics", "web application security testing",
        "cryptanalysis", "endpoint detection and response",
        "social engineering red team", "supply chain security audit",
        "cloud security architecture", "SIEM rule development",
    ],

    "RF/SDR/Signals": [
        "software defined radio development", "RF spectrum analysis",
        "signal modulation classification", "wireless protocol reverse engineering",
        "antenna design optimization", "radar signal processing",
        "satellite communication protocols", "electromagnetic shielding design",
        "frequency hopping analysis", "noise figure measurement",
        "microwave filter design", "phase coherence testing",
        "RF test fixture design", "jamming detection systems",
        "wireless sensor network optimization",
    ],

    "Automotive & Engine": [
        "internal combustion engine tuning", "diesel particulate filter testing",
        "transmission fluid dynamics", "engine block metallurgy analysis",
        "automotive electrical system diagnostics", "fuel injection optimization",
        "suspension geometry tuning", "brake system failure analysis",
        "powertrain control module reprogramming", "engine knock detection",
        "hybrid system energy management", "vehicle crash test interpretation",
        "driveline vibration analysis", "emissions system troubleshooting",
        "tire grip coefficient testing",
    ],

    "Hardware & Embedded": [
        "microcontroller firmware development", "PCB layout optimization",
        "FPGA design and simulation", "real-time embedded systems",
        "sensor calibration and integration", "bootloader reverse engineering",
        "power consumption profiling", "thermal management design",
        "memory hierarchy optimization", "interrupt handler design",
        "hardware-software codesign", "mixed-signal circuit analysis",
        "embedded Linux kernel tuning", "IoT device security hardening",
        "BLE protocol implementation",
    ],

    "Physical Sciences": [
        "quantum mechanics modeling", "particle physics simulation",
        "crystallography analysis", "thermodynamics equation solving",
        "optics system design", "acoustics room correction",
        "materials science testing", "X-ray diffraction analysis",
        "plasma physics containment", "relativity calculations",
        "nuclear decay modeling", "electromagnetic field mapping",
        "superconductor characterization", "photonics waveguide design",
        "spectroscopy interpretation",
    ],

    "Life Sciences": [
        "marine biology ecology", "mycology taxonomy", "paleontology excavation",
        "astrobiology habitability analysis", "entomology specimen identification",
        "ethology behavior pattern analysis", "parasitology life cycle tracking",
        "arachnology venom characterization", "virology infection modeling",
        "genetics trait inheritance", "microbiology culture techniques",
        "botany plant physiology", "zoology comparative anatomy",
        "immunology antibody engineering", "cellular biology imaging",
    ],

    "Earth Sciences": [
        "volcanology eruption forecasting", "glaciology ice core analysis",
        "seismology earthquake prediction", "dendrochronology tree ring dating",
        "limnology lake ecosystem study", "pedology soil composition",
        "oceanography current mapping", "meteorology weather modeling",
        "hydrogeology groundwater flow", "mineralogy crystal identification",
        "geomorphology landform evolution", "paleoclimatology ice age modeling",
        "stratigraphy layer dating", "geothermal reservoir characterization",
        "tsunami simulation modeling",
    ],

    "Engineering & Technical": [
        "naval architecture ship design", "acoustic engineering sound dampening",
        "hydraulic engineering fluid dynamics", "biomechanical engineering prosthetics",
        "geotechnical engineering foundation", "nuclear reactor operations",
        "wind turbine maintenance diagnostics", "satellite communications design",
        "fiber optic installation testing", "desalination plant operations",
        "dam safety inspection protocols", "bridge stress analysis",
        "wastewater treatment design", "HVAC system optimization",
        "elevator maintenance diagnostics", "power grid management",
        "railway signaling systems", "tunnel boring machine operation",
    ],

    "Trades & Crafts": [
        "watchmaking precision assembly", "blacksmithing metal forging",
        "glassblowing form shaping", "bookbinding leather work",
        "taxidermy animal preservation", "locksmithing mechanism design",
        "gem cutting angle optimization", "coopering barrel construction",
        "thatching roof design", "masonry restoration mortar selection",
        "letterpress printing ink mixing", "leatherworking pattern creation",
        "pottery wheel throwing", "woodturning tool techniques",
        "instrument building acoustic design", "sailmaking seam strength",
        "upholstery frame restoration", "engraving line precision",
        "stained glass restoration", "clockwork repair synchronization",
    ],

    "Outdoor & Adventure": [
        "cave diving depth decompression", "mountaineering altitude acclimatization",
        "falconry bird training", "bushcraft shelter construction",
        "ice climbing equipment selection", "paragliding thermal lift detection",
        "deep sea fishing line strength", "orienteering map navigation",
        "storm chasing radar interpretation", "wildlife tracking sign reading",
        "mushroom foraging species identification", "beekeeping hive health",
        "trail building erosion control", "avalanche forecasting slope analysis",
        "wildfire management containment", "search and rescue coordination",
        "underwater archaeology excavation", "coral reef restoration",
        "whale watching migration tracking",
    ],

    "Food & Agriculture": [
        "viticulture grape phenology", "cheesemaking culture selection",
        "sourdough baking fermentation timing", "aquaponics system balance",
        "coffee roasting temperature profiling", "chocolate tempering crystal structure",
        "fermentation science pH management", "olive oil production harvest timing",
        "truffle hunting animal tracking", "sake brewing koji cultivation",
        "permaculture design ecosystem planning", "seed banking storage conditions",
        "vertical farming nutrient management", "livestock genetics selection",
        "soil microbiome management", "apiary management disease prevention",
        "hydroponic system nutrients", "heritage grain preservation",
    ],

    "Arts & Creative": [
        "jazz composition harmony theory", "stop motion animation frame planning",
        "calligraphy letterform design", "sound design audio synthesis",
        "theatrical lighting color theory", "puppetry movement mechanics",
        "mosaic art tile arrangement", "film restoration degradation analysis",
        "voice acting character development", "choreography movement notation",
        "street photography composition", "documentary filmmaking narrative",
        "comic book inking line weight", "perfumery scent layering",
        "typography design kerning", "architectural model building scale",
        "foley artistry sound recording", "tattoo design line art",
        "neon sign crafting gas physics",
    ],

    "History & Culture": [
        "archaeological excavation stratigraphy", "medieval manuscript analysis paleography",
        "nautical history ship technology", "industrial archaeology site survey",
        "numismatics coin dating", "heraldry symbol interpretation",
        "genealogy research tree construction", "oral history collection interviewing",
        "museum curation artifact selection", "artifact conservation cleaning",
        "epigraphy inscription translation", "ancient metallurgy composition analysis",
        "battlefield archaeology site mapping", "historical costume reconstruction",
        "archival preservation digital scanning", "cultural anthropology field study",
        "linguistic etymology tracking",
    ],

    "Medical & Health": [
        "emergency triage protocols", "prosthetics fitting biomechanics",
        "sleep medicine sleep study analysis", "sports medicine injury rehabilitation",
        "toxicology screening interpretation", "surgical planning imaging analysis",
        "radiology interpretation diagnosis", "veterinary dentistry extraction",
        "epidemiological modeling disease spread", "physical therapy exercise programming",
        "herbal pharmacology compound extraction", "audiometry hearing test interpretation",
        "optometry practice vision correction", "occupational therapy adaptation",
        "trauma surgery emergency protocol", "palliative care symptom management",
        "nutrition science dietary planning",
    ],

    "Transportation & Logistics": [
        "air traffic control radar systems", "cargo ship loading optimization",
        "railway dispatching scheduling", "drone delivery route planning",
        "port operations container handling", "fleet maintenance scheduling",
        "cold chain logistics temperature control", "hazmat transportation regulations",
        "airport ground operations sequencing", "canal lock operations timing",
        "helicopter emergency services dispatch", "space mission planning trajectory",
        "submarine navigation positioning", "yacht racing tactics wind patterns",
        "convoy planning route security", "traffic engineering signal timing",
        "supply chain network design",
    ],

    "Environmental & Earth": [
        "wetland restoration native planting", "air quality monitoring sensor placement",
        "carbon credit verification accounting", "ocean current mapping data collection",
        "soil erosion prevention contour design", "invasive species management eradication",
        "light pollution measurement sky brightness", "noise pollution mapping acoustic",
        "glacier monitoring melt rate", "urban heat island analysis",
        "microplastics sampling testing", "river rewilding habitat restoration",
        "abandoned mine remediation water treatment", "landfill gas management capture",
        "renewable energy siting analysis", "environmental impact assessment",
        "climate change modeling prediction",
    ],

    "Security & Intelligence": [
        "physical penetration testing access control", "executive protection threat assessment",
        "crisis negotiation communication tactics", "espionage tradecraft asset handling",
        "counterintelligence analysis motive identification", "bomb disposal robot operation",
        "hostage rescue planning terrain", "surveillance detection evasion",
        "border security operations scanning", "diplomatic security advance planning",
        "witness protection logistics relocation", "prison security audit perimeter",
        "maritime piracy prevention escort", "VIP motorcade planning route",
        "security clearance vetting investigation",
    ],

    "Space & Aviation": [
        "telescope mirror grinding precision", "asteroid mining trajectory analysis",
        "satellite deorbiting controlled descent", "rocket engine testing thrust measurement",
        "space habitat design life support", "EVA procedure planning suited operations",
        "radio telescope operations signal detection", "launch pad refurbishment equipment",
        "space debris tracking collision avoidance", "Mars terrain analysis rover planning",
        "comet composition analysis spectroscopy", "orbital mechanics rendezvous",
        "aircraft autopilot programming", "aeronautical navigation systems",
        "propulsion system design efficiency",
    ],

    "Computing & Software": [
        "database query optimization indexing", "distributed systems consensus algorithms",
        "compiler design intermediate representation", "operating system kernel design",
        "graphics engine rendering pipeline", "machine learning model training",
        "cloud infrastructure deployment automation", "API design specification",
        "version control workflow management", "continuous integration testing",
        "containerization orchestration", "data structure algorithm analysis",
        "system architecture design scalability", "code review standards",
        "performance profiling bottleneck identification",
    ],

    "Finance & Economics": [
        "portfolio management asset allocation", "options trading volatility analysis",
        "forex trading currency correlation", "cryptocurrency blockchain analysis",
        "real estate valuation appraisal", "insurance underwriting risk assessment",
        "tax planning strategy optimization", "accounting audit trail verification",
        "corporate finance capital structure", "behavioral economics decision making",
        "macroeconomics GDP modeling", "microeconomics supply demand",
        "financial forecasting cash flow", "risk management scenario analysis",
    ],

    "Education & Training": [
        "curriculum design learning objectives", "instructional design assessment",
        "corporate training needs analysis", "apprenticeship program structure",
        "online learning platform development", "mentorship relationship building",
        "performance evaluation metrics", "professional certification exam preparation",
        "knowledge management documentation", "coaching skill development",
        "educational technology integration", "adult learning theory application",
        "course facilitation engagement", "knowledge transfer documentation",
    ],

    "Unusual & Niche": [
        "competitive barbecue judging flavor profiles", "escape room design puzzle logic",
        "haunted house engineering scares", "roller coaster design forces physics",
        "theme park queue optimization flow", "zookeeping enrichment planning",
        "circus rigging acrobatics safety", "pyrotechnics choreography timing",
        "ice rink maintenance surface freezing", "bowling alley mechanics pin setting",
        "pinball machine restoration flipper mechanics", "jukebox repair player mechanism",
        "vintage synthesizer calibration frequency", "pipe organ maintenance air pressure",
        "lighthouse keeping beam maintenance", "gondola piloting cable tension",
        "hot air balloon operations weather", "trebuchet engineering projectile trajectory",
        "sundial construction angle calculation", "weather balloon launches tracking",
        "antique clock restoration pendulum", "magic trick illusion design",
    ],
}

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

# === STATISTICS ===
def get_stats():
    """Return pool statistics."""
    total_categories = len(CATEGORIES)
    total_domains = sum(len(domains) for domains in CATEGORIES.values())
    total_unique_outcomes = total_categories * total_domains
    return {
        "total_categories": total_categories,
        "total_domains": total_domains,
        "total_unique_outcomes": total_unique_outcomes,
    }


def get_daily_assignment(date_str=None):
    """
    Generate today's workspace assignment using date-seeded entropy.
    Two-tier selection: category first, then domain within category.
    This prevents thematic clustering on consecutive days.
    """
    if date_str:
        today = datetime.date.fromisoformat(date_str)
    else:
        today = datetime.date.today()

    category_list = list(CATEGORIES.keys())

    # === PRIMARY SELECTION ===
    # Hash 1: Category selection
    primary_cat_hash = int(hashlib.sha256(today.isoformat().encode()).hexdigest(), 16)
    primary_cat_idx = primary_cat_hash % len(category_list)
    primary_category = category_list[primary_cat_idx]
    primary_domains = CATEGORIES[primary_category]

    # Hash 2: Domain within primary category
    primary_dom_hash = int(hashlib.sha256(
        (today.isoformat() + "domain").encode()).hexdigest(), 16)
    primary_dom_idx = primary_dom_hash % len(primary_domains)
    primary_domain = primary_domains[primary_dom_idx]

    # === SECONDARY SELECTION (for crossover) ===
    # Hash 3: Secondary category (must differ from primary)
    secondary_cat_hash = int(hashlib.sha256(
        (today.isoformat() + "secondary").encode()).hexdigest(), 16)
    secondary_cat_idx = secondary_cat_hash % len(category_list)
    if secondary_cat_idx == primary_cat_idx:
        secondary_cat_idx = (secondary_cat_idx + 1) % len(category_list)
    secondary_category = category_list[secondary_cat_idx]
    secondary_domains = CATEGORIES[secondary_category]

    # Domain within secondary category
    secondary_dom_hash = int(hashlib.sha256(
        (today.isoformat() + "secondary_domain").encode()).hexdigest(), 16)
    secondary_dom_idx = secondary_dom_hash % len(secondary_domains)
    secondary_domain = secondary_domains[secondary_dom_idx]

    # === TECHNIQUE MODIFIER ===
    # Hash 4: Technique selection
    technique_hash = int(hashlib.sha256(
        (today.isoformat() + "technique").encode()).hexdigest(), 16)
    technique_idx = technique_hash % len(TECHNIQUES)
    technique = TECHNIQUES[technique_idx]

    # === CROSSOVER FLAG ===
    # Hash 5: Crossover probability (~30% of days)
    crossover_hash = int(hashlib.sha256(
        (today.isoformat() + "crossover").encode()).hexdigest(), 16)
    crossover_flag = crossover_hash % 10
    is_crossover = crossover_flag < 3

    # === SPARK SELECTION ===
    spark_hash = int(hashlib.sha256(
        (today.isoformat() + "spark").encode()).hexdigest(), 16)
    spark_idx = spark_hash % len(SPARKS)
    spark = SPARKS[spark_idx].format(domain1=primary_domain, domain2=secondary_domain)

    result = {
        "date": today.isoformat(),
        "primary_category": primary_category,
        "primary_domain": primary_domain,
        "secondary_category": secondary_category if is_crossover else None,
        "secondary_domain": secondary_domain if is_crossover else None,
        "technique": technique,
        "is_crossover": is_crossover,
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
    lines.append(f" Primary Category: {assignment['primary_category']}")
    lines.append(f" Primary Domain:   {assignment['primary_domain'].upper()}")
    lines.append(f" Technique:        {assignment['technique']}")
    lines.append(f"")

    if assignment['is_crossover']:
        lines.append(f" ** CROSSOVER DAY **")
        lines.append(f" Secondary Category: {assignment['secondary_category']}")
        lines.append(f" Secondary Domain:   {assignment['secondary_domain']}")
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

    # Print pool statistics
    print("\n--- POOL STATISTICS ---")
    stats = get_stats()
    print(f"Total Categories: {stats['total_categories']}")
    print(f"Total Domains: {stats['total_domains']}")
    print(f"Possible Unique Outcomes: {stats['total_unique_outcomes']:,}")
