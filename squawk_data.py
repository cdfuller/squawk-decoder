"""Squawk data and lookup utilities derived from FAA Order JO 7110.66G (NBCAP)
and ARTCC_Location_Identifiers.csv.

All relevant squawk allocation information is embedded so the source PDF/CSV
are not required at runtime.
"""

# Table A-1 allocations from JO 7110.66G.
SPECIAL_ALLOCATIONS = [
    {
        "codes": [(0, 0)],
        "allocation": (
            "Used by certain UAT ADS-B units upon power-up until the aircraft enters "
            "beacon interrogation surveillance coverage."
        ),
    },
    {
        "codes": [(100, 100), (200, 200), (300, 300), (400, 400)],
        "allocation": (
            "Code blocks allocated to Service Area Operations for use by Terminal/CERAP, "
            "NAS Stakeholder, Unique Purpose, and Experimental activities."
        ),
        "block": True,
    },
    {
        "codes": [(1000, 1000)],
        "allocation": "Used exclusively by ADS-B aircraft to inhibit Mode 3A transmit.",
    },
    {
        "codes": [(1200, 1200)],
        "allocation": "Visual Flight Rules (VFR) aircraft that may or may not be in contact with ATC.",
    },
    {
        "codes": [(2000, 2000)],
        "allocation": "Used in oceanic airspace unless another code is assigned by ATC.",
    },
    {
        "codes": [(1201, 1201)],
        "allocation": (
            "VFR aircraft operating in the Los Angeles Special Flight Rules Area "
            "(SFRA) in accordance with 14 CFR sections 93.93 and 93.95."
        ),
    },
    {
        "codes": [(1202, 1202)],
        "allocation": "VFR gliders that may or may not be in contact with ATC.",
    },
    {
        "codes": [(1205, 1205)],
        "allocation": (
            "VFR Helicopters within the Los Angeles region that may or may not be in contact with ATC, "
            "or VFR aircraft departing the DC SFRA fringe airports in accordance with 14 CFR section 93.345."
        ),
    },
    {
        "codes": [(1206, 1206)],
        "allocation": (
            "Reserved for use by VFR Public Service helicopters within the Los Angeles region that may "
            "or may not be in contact with ATC."
        ),
    },
    {
        "codes": [(1207, 1233), (1235, 1254), (1256, 1272)],
        "allocation": (
            "Discrete 1200 series code subsets allocated to Service Area Operations for assignment to air "
            "traffic facilities as needed for Unique Purpose VFR Programs (e.g., DVFR, tour operators)."
        ),
    },
    {
        "codes": [(1234, 1234)],
        "allocation": (
            "VFR aircraft conducting pattern work at airports in the DC SFRA, in accordance with "
            "14 CFR section 93.339."
        ),
    },
    {
        "codes": [(1255, 1255)],
        "allocation": "Firefighting aircraft.",
    },
    {
        "codes": [(1273, 1275)],
        "allocation": "Calibration Performance Monitoring Equipment (CPME), MRSM, and PARROT transponders.",
    },
    {
        "codes": [(1276, 1276)],
        "allocation": (
            "Air Defense Identification Zone (ADIZ) penetration when unable to establish communication "
            "with ATC or an aeronautical facility."
        ),
    },
    {
        "codes": [(1277, 1277)],
        "allocation": "Designated Search and Rescue (SAR) aircraft.",
    },
    {
        "codes": [(4400, 4433)],
        "allocation": (
            "Reserved/allocated. For information on the use of this code subset, contact 9-ATOR-HQ-SBC@faa.gov."
        ),
    },
    {
        "codes": [(4434, 4437)],
        "allocation": "Weather reconnaissance, as appropriate.",
    },
    {
        "codes": [(4440, 4452)],
        "allocation": (
            "Reserved/allocated. For information on the use of this code subset, contact 9-ATOR-HQ-SBC@faa.gov."
        ),
    },
    {
        "codes": [(4453, 4453)],
        "allocation": (
            "High balloon operations - National Scientific Balloon Facility, Palestine, TX; and other providers, "
            "some in international operations."
        ),
    },
    {
        "codes": [(4454, 4477)],
        "allocation": (
            "Reserved/allocated. For information on the use of this code subset, contact 9-ATOR-HQ-SBC@faa.gov."
        ),
    },
    {
        "codes": [(5100, 5100), (5200, 5200)],
        "allocation": "Code blocks allocated to Potomac TRACON (PCT) for use in the D.C. SFRA and FRZ.",
        "block": True,
    },
    {
        "codes": [(5000, 5000), (5400, 5400), (6100, 6100), (6400, 6400)],
        "allocation": (
            "Reserved/allocated. For information on the use of these code blocks, contact 9-ATOR-HQ-SBC@faa.gov."
        ),
        "block": True,
    },
    {
        "codes": [(7400, 7400)],
        "allocation": "Reserved for an unmanned aircraft experiencing a lost link situation.",
    },
    {
        "codes": [(7500, 7500)],
        "allocation": "Hijack/Unlawful Interference - reserved internationally.",
    },
    {
        "codes": [(7600, 7600)],
        "allocation": "Communication Failure - reserved internationally.",
    },
    {
        "codes": [(7700, 7700)],
        "allocation": "Emergency - reserved internationally.",
    },
    {
        "codes": [(7501, 7577), (7601, 7607), (7701, 7707), (7777, 7777)],
        "allocation": (
            "Reserved/allocated. For information on the use of these code subsets, contact 9-ATOR-HQ-SBC@faa.gov."
        ),
    },
    {
        "codes": [
            (500, 500),
            (600, 600),
            (700, 700),
            (1000, 1000),
            (1100, 1100),
            (1300, 1300),
            (1400, 1400),
            (1500, 1500),
            (1600, 1600),
            (1700, 1700),
            (2100, 2100),
            (2200, 2200),
            (2300, 2300),
            (2400, 2400),
            (2500, 2500),
            (2600, 2600),
            (2700, 2700),
            (3000, 3000),
            (3100, 3100),
            (3200, 3200),
            (3300, 3300),
            (3400, 3400),
            (3500, 3500),
            (3600, 3600),
            (3700, 3700),
            (4000, 4000),
            (4100, 4100),
            (5600, 5600),
            (5700, 5700),
            (6000, 6000),
            (6200, 6200),
            (6300, 6300),
            (6500, 6500),
            (6600, 6600),
            (6700, 6700),
            (7000, 7000),
            (7100, 7100),
            (7200, 7200),
            (7300, 7300),
            (7401, 7477),
            (7610, 7676),
            (7710, 7776),
        ],
        "allocation": (
            "External ARTCC code blocks and code subsets, consisting of the discrete codes of the blocks except for "
            "the nondiscrete code of the first primary block, which is used as the ARTCC nondiscrete external code "
            "if all discrete external codes are assigned."
        ),
        "block": True,
    },
    {
        "codes": [(0, 0), (4200, 4200), (4300, 4300), (4500, 4500), (4600, 4600), (4700, 4700), (5100, 5100), (5200, 5200), (5300, 5300), (5500, 5500)],
        "allocation": (
            "Internal ARTCC code blocks, consisting of the discrete codes of the blocks except for the nondiscrete code "
            "of the first primary block, which is used as the ARTCC nondiscrete internal code if all discrete internal "
            "codes are assigned. Internal ARTCC code blocks are assigned by the Policy Directorate, Standards & Procedures "
            "Group, ATC Procedures (En Route) Team."
        ),
        "block": True,
    },
]

# Table B-3 assignments from JO 7110.66G.
ARTCC_ASSIGNMENTS = {
    'KZAK': [(1100, 1100, 'ATOP')],
    'KZWY': [(1001, 1077, 'ATOP')],
    'ZAB': [(700, 700, 'EP-1'), (1500, 1500, 'ES-1'), (1600, 1600, 'ES-2'), (2600, 2600, 'EP-2'), (3001, 3020, 'ET-1'), (3101, 3134, 'ET-2'), (3501, 3515, 'ET-3'), (4100, 4100, 'ES-3'), (4200, 4200, 'IP-1'), (4300, 4300, 'IP-2'), (5500, 5500, 'IS-1'), (5601, 5621, 'ET-4'), (6024, 6047, 'ET-5')],
    'ZAN': [(2200, 2200, 'I'), (2300, 2300, 'I'), (3100, 3100, 'IS'), (3400, 3400, 'E'), (3500, 3500, 'IS'), (4000, 4000, 'ES'), (4100, 4100, 'E'), (4200, 4200, 'I'), (4500, 4500, 'I'), (4600, 4600, 'I'), (4700, 4700, 'I'), (5100, 5100, 'I'), (5200, 5200, 'I'), (5300, 5300, 'M'), (5500, 5500, 'M'), (5600, 5600, 'ES'), (5700, 5700, 'E'), (7200, 7200, 'E')],
    'ZAU': [(1, 7, 'IS-1'), (11, 17, 'IS-2'), (21, 27, 'IS-3'), (31, 37, 'IS-4'), (41, 47, 'IS-5'), (51, 57, 'IS-6'), (61, 67, 'IS-7'), (71, 77, 'IS-8'), (500, 500, 'ET-1'), (1300, 1300, 'EP-1'), (2200, 2200, 'ET-2'), (3100, 3100, 'EP-2'), (3200, 3200, 'ES-1'), (3500, 3500, 'ES-2'), (4300, 4300, 'IP-1'), (4700, 4700, 'IS-9'), (5300, 5300, 'IP-2'), (5500, 5500, 'IS-10'), (5600, 5600, 'ES-3'), (6200, 6200, 'EP-3'), (6500, 6500, 'EP-4'), (7200, 7200, 'ES-4')],
    'ZBW': [(1, 77, 'IS-1'), (1300, 1300, 'ES-1'), (1400, 1400, 'ES-2'), (2000, 2007, 'ES-3'), (2400, 2400, 'ET-1'), (3400, 3400, 'EP-1'), (3500, 3500, 'EP-2'), (4600, 4600, 'IS-2'), (4700, 4700, 'IS-3'), (5300, 5300, 'IP-1'), (5500, 5500, 'IS-4'), (7000, 7000, 'ET-2'), (7300, 7300, 'ES-4')],
    'ZDC': [(1, 77, 'IS-1'), (500, 500, 'EP-1'), (1300, 1300, 'ES-1'), (2100, 2100, 'EP-2'), (2400, 2400, 'EP-3'), (3500, 3500, 'ET-1'), (3600, 3600, 'EP-4'), (3700, 3700, 'ET-2'), (4600, 4600, 'IP-1'), (4700, 4700, 'IS-2'), (5300, 5300, 'IP-2'), (5500, 5500, 'IS-3'), (5600, 5600, 'EP-5'), (6200, 6200, 'ES-2'), (6500, 6500, 'ES-3'), (7000, 7000, 'EP-6')],
    'ZDV': [(1, 77, 'IS-1'), (600, 600, 'ES-1'), (1400, 1400, 'EP-1'), (2212, 2235, 'ET-1'), (2700, 2700, 'ES-2'), (3333, 3377, 'ET-2'), (3401, 3427, 'ET-3'), (3700, 3700, 'ES-3'), (4300, 4300, 'IS-2'), (5100, 5100, 'IP-1'), (5500, 5500, 'IS-3'), (5622, 5642, 'ET-4'), (6500, 6500, 'ES-4'), (6644, 6655, 'ET-5'), (7441, 7453, 'ET-6')],
    'ZFW': [(500, 500, 'EP-1'), (613, 677, 'ET-1'), (2200, 2200, 'EP-2'), (2300, 2300, 'EP-3'), (3021, 3077, 'ET-2'), (3241, 3264, 'ET-3'), (3400, 3400, 'ES-1'), (3600, 3600, 'ES-2'), (4500, 4500, 'IS-1'), (5100, 5100, 'IP-1'), (5200, 5200, 'IP-2'), (5300, 5300, 'IS-2'), (6200, 6200, 'ES-3'), (7041, 7077, 'ET-4')],
    'ZHU': [(1, 77, 'IT-1'), (2400, 2400, 'EP-1'), (2500, 2500, 'EP-2'), (2700, 2700, 'ES-1'), (4000, 4000, 'ES-2'), (4200, 4200, 'IS-1'), (4500, 4500, 'IP-1'), (4600, 4600, 'IP-2'), (4700, 4700, 'IS-2'), (5101, 5127, 'IT-2'), (5146, 5177, 'IT-3'), (5200, 5200, 'IS-3'), (6600, 6600, 'ET-1'), (6700, 6700, 'ET-2'), (7200, 7200, 'ES-3'), (7300, 7300, 'ES-4'), (7401, 7477, 'ES-5')],
    'ZID': [(1400, 1400, 'ES-1'), (2601, 2642, 'ET-1'), (2701, 2735, 'ET-2'), (3001, 3042, 'ET-3'), (3400, 3400, 'ES-2'), (3700, 3700, 'ES-3'), (4000, 4000, 'EP-1'), (4200, 4200, 'IP-1'), (4500, 4500, 'IP-2'), (5500, 5500, 'IS-1'), (6600, 6600, 'EP-2'), (6700, 6700, 'EP-3'), (7300, 7300, 'ES-4')],
    'ZJX': [(700, 700, 'EP-1'), (1001, 1077, 'EP-2'), (1500, 1500, 'ES-1'), (1600, 1600, 'ES-2'), (2600, 2600, 'EP-3'), (2700, 2700, 'ET-1'), (3000, 3000, 'ES-3'), (3200, 3200, 'ES-4'), (3400, 3400, 'IP-1'), (4200, 4200, 'IP-2'), (4300, 4300, 'IT-1'), (5500, 5500, 'IP-3'), (6200, 6200, 'ES-5'), (6500, 6500, 'ET-2'), (6700, 6700, 'ET-3'), (7300, 7300, 'ES-6'), (7401, 7477, 'IS-1'), (7610, 7676, 'ET-4'), (7710, 7776, 'ET-5')],
    'ZKC': [(1100, 1100, 'EP-1'), (1700, 1700, 'EP-2'), (2001, 2020, 'ET-1'), (2100, 2100, 'EP-3'), (2500, 2500, 'ES-1'), (3301, 3311, 'ET-2'), (4600, 4600, 'IP-1'), (4700, 4700, 'IP-2'), (5200, 5200, 'IS-1'), (5700, 5700, 'ES-2'), (6001, 6023, 'ET-3'), (7101, 7120, 'ET-4'), (7401, 7440, 'ET-5')],
    'ZLA': [(1000, 1000, 'EP-1'), (1300, 1300, 'ES-1'), (2000, 2000, 'ES-2'), (2401, 2477, 'ET-1'), (4600, 4600, 'IP-1'), (4700, 4700, 'IP-2'), (5100, 5100, 'IS-1'), (5300, 5300, 'IS-2'), (6700, 6700, 'ES-3'), (7200, 7200, 'EP-2'), (7300, 7300, 'EP-3'), (7610, 7675, 'ET-2'), (7710, 7776, 'ET-3')],
    'ZLC': [(500, 500, 'ES-1'), (701, 710, 'ET-1'), (716, 720, 'ET-2'), (726, 730, 'ET-3'), (2201, 2211, 'ET-4'), (2301, 2332, 'ET-5'), (2501, 2512, 'ET-6'), (3100, 3100, 'ES-2'), (4000, 4000, 'ES-3'), (4100, 4100, 'ET-7'), (4200, 4200, 'IS-1'), (4300, 4300, 'IP-1'), (5200, 5200, 'IS-2'), (5300, 5300, 'IS-3'), (5601, 5611, 'ET-8'), (6000, 6000, 'EP-1'), (6201, 6211, 'ET-9'), (7401, 7411, 'ET-10'), (7610, 7676, 'ET-11'), (7710, 7776, 'ET-12')],
    'ZMA': [(0, 0, 'IP-1'), (500, 500, 'ET-1'), (1100, 1100, 'ES-1'), (1300, 1300, 'ES-2'), (1400, 1400, 'EP-1'), (2100, 2100, 'ES-3'), (2200, 2200, 'ET-2'), (2300, 2300, 'ES-4'), (3300, 3300, 'ES-5'), (3500, 3500, 'ES-6'), (3600, 3600, 'EP-2'), (3700, 3700, 'EP-3'), (4200, 4200, 'IS-1'), (4500, 4500, 'IP-2'), (4600, 4600, 'IP-3'), (4700, 4700, 'IP-4'), (5100, 5100, 'IS-2'), (5300, 5300, 'IS-3'), (5600, 5600, 'ET-3'), (5700, 5700, 'ES-7'), (6000, 6000, 'ES-8'), (6600, 6600, 'ES-9'), (7000, 7000, 'ET-4'), (7100, 7100, 'ET-5'), (7401, 7477, 'EP-4'), (7610, 7676, 'ET-6'), (7710, 7776, 'ET-7')],
    'ZME': [(700, 700, 'ES-1'), (1001, 1077, 'ES-2'), (1300, 1300, 'ES-3'), (1500, 1500, 'EP-1'), (1600, 1600, 'EP-2'), (4300, 4300, 'IP-1'), (4500, 4500, 'IS-1'), (5300, 5300, 'IS-2'), (5500, 5500, 'IP-2'), (5600, 5600, 'EP-3'), (7610, 7676, 'ET-1'), (7710, 7776, 'ET-2')],
    'ZMP': [(1501, 1532, 'ET-1'), (1600, 1600, 'ES-1'), (2400, 2400, 'EP-1'), (2600, 2600, 'EP-2'), (3000, 3000, 'ES-2'), (3312, 3332, 'ET-2'), (3600, 3600, 'EP-3'), (4200, 4200, 'IP-1'), (4500, 4500, 'IP-2'), (4600, 4600, 'IS-1'), (5200, 5200, 'IS-2'), (6700, 6700, 'ET-3'), (7000, 7000, 'ES-3')],
    'ZNY': [(1001, 1077, 'ES-1'), (1100, 1100, 'EP-1'), (1500, 1500, 'EP-2'), (1600, 1600, 'EP-3'), (1700, 1700, 'EP-4'), (2200, 2200, 'ES-2'), (2300, 2300, 'ES-3'), (2600, 2600, 'EP-5'), (2700, 2700, 'EP-6'), (3000, 3000, 'EP-7'), (3300, 3300, 'EP-8'), (4000, 4000, 'ES-4'), (4200, 4200, 'IP-1'), (4500, 4500, 'IS-1'), (4600, 4600, 'IS-2'), (6601, 6666, 'ES-5'), (6725, 6777, 'ET-1'), (7100, 7100, 'EP-9'), (7610, 7676, 'ET-2'), (7710, 7776, 'ET-3')],
    'ZOA': [(601, 647, 'ET-1'), (1700, 1700, 'ES-1'), (2212, 2235, 'ET-2'), (3001, 3020, 'ET-3'), (3200, 3200, 'EP-1'), (3300, 3300, 'EP-2'), (3600, 3600, 'ES-2'), (3700, 3700, 'ES-3'), (4200, 4200, 'IP-1'), (4300, 4300, 'IS-1'), (4500, 4500, 'IP-2'), (5500, 5500, 'IS-2'), (6300, 6300, 'ES-4'), (7000, 7000, 'IS-3'), (7441, 7464, 'ET-4')],
    'ZOB': [(500, 500, 'ET-1'), (600, 600, 'ET-2'), (700, 700, 'ET-3'), (1001, 1077, 'ES-1'), (2100, 2100, 'ES-2'), (2300, 2300, 'ES-3'), (2500, 2500, 'ES-4'), (4100, 4100, 'EP-1'), (4500, 4500, 'IS-1'), (5100, 5100, 'IP-1'), (5200, 5200, 'IP-2'), (5700, 5700, 'EP-2'), (6000, 6000, 'ES-5'), (6300, 6300, 'ET-4'), (7200, 7200, 'ES-6'), (7401, 7477, 'EP-3')],
    'ZSE': [(650, 677, 'ET-1'), (1500, 1500, 'ES-1'), (1600, 1600, 'ES-2'), (2236, 2277, 'ET-2'), (3430, 3477, 'ET-3'), (3500, 3500, 'EP-1'), (4600, 4600, 'IP-1'), (4700, 4700, 'IP-2'), (5100, 5100, 'IS-1'), (5200, 5200, 'IS-2'), (6600, 6600, 'EP-2'), (7412, 7477, 'ET-4')],
    'ZTL': [(1100, 1100, 'ES-1'), (1700, 1700, 'ES-2'), (2000, 2000, 'EP-1'), (2200, 2200, 'ES-3'), (2500, 2500, 'EP-2'), (2600, 2600, 'IS-1'), (3100, 3100, 'EP-3'), (3300, 3300, 'ES-4'), (3500, 3500, 'ES-5'), (4134, 4177, 'ES-6'), (4700, 4700, 'IS-2'), (5100, 5100, 'IP-1'), (5200, 5200, 'IP-2'), (5300, 5300, 'IS-3'), (5700, 5700, 'ES-7'), (6000, 6000, 'ES-8'), (7100, 7100, 'EP-4'), (7200, 7200, 'ES-9')],
}

# ARTCC metadata from ARTCC_Location_Identifiers.csv.
ARTCC_METADATA = {
    'ZAB': {'icao': 'KZAB', 'name': 'Albuquerque'},
    'ZAN': {'icao': 'PAZA', 'name': 'Anchorage'},
    'ZAU': {'icao': 'KZAU', 'name': 'Chicago'},
    'ZBW': {'icao': 'KZBW', 'name': 'Boston'},
    'ZDC': {'icao': 'KZDC', 'name': 'Washington'},
    'ZDV': {'icao': 'KZDV', 'name': 'Denver'},
    'ZFW': {'icao': 'KZFW', 'name': 'Fort Worth'},
    'ZHN': {'icao': 'PHZH', 'name': 'Honolulu'},
    'ZHU': {'icao': 'KZHU', 'name': 'Houston'},
    'ZID': {'icao': 'KZID', 'name': 'Indianapolis'},
    'ZJX': {'icao': 'KZJX', 'name': 'Jacksonville'},
    'ZKC': {'icao': 'KZKC', 'name': 'Kansas City'},
    'ZLA': {'icao': 'KZLA', 'name': 'Los Angeles'},
    'ZLC': {'icao': 'KZLC', 'name': 'Salt Lake City'},
    'ZMA': {'icao': 'KZMA', 'name': 'Miami'},
    'ZME': {'icao': 'KZME', 'name': 'Memphis'},
    'ZMP': {'icao': 'KZMP', 'name': 'Minneapolis'},
    'ZNY': {'icao': 'KZNY', 'name': 'New York'},
    'ZOA': {'icao': 'KZOA', 'name': 'Oakland'},
    'ZOB': {'icao': 'KZOB', 'name': 'Cleveland'},
    'ZSE': {'icao': 'KZSE', 'name': 'Seattle'},
    'ZSU': {'icao': 'TJZS', 'name': 'San Juan'},
    'ZTL': {'icao': 'KZTL', 'name': 'Atlanta'},
    'ZUA': {'icao': 'PGZU', 'name': 'Guam'},
}

CATEGORY_NAMES = {
    "I": "Internal Departures",
    "E": "External Departures",
    "M": "Military",
    "S": "Special Use",
}

SEQUENCE_NAMES = {
    "P": "Primary code block or subset",
    "S": "Secondary code block or subset",
    "T": "Tertiary code block or subset",
}

ATOP_EXPLANATION = "Automated oceanic assignment via Advanced Technologies and Oceanic Procedures (ATOP)."


class SquawkDatabase:
    """In-memory squawk information lookup built from JO 7110.66G and ARTCC data."""

    def __init__(self):
        self.special_allocations = SPECIAL_ALLOCATIONS
        self.artcc_assignments = ARTCC_ASSIGNMENTS
        self.artcc_metadata = ARTCC_METADATA

    def normalize_code(self, code):
        """Normalize a Mode 3/A code and validate its shape.

        Args:
            code: User-supplied squawk (string or number).

        Returns:
            Dict with normalized code string, validity flag, and error text if invalid.
        """
        raw = str(code).strip()
        if not raw:
            return {"code": None, "valid": False, "error": "No code provided."}
        if not raw.isdigit():
            return {"code": raw, "valid": False, "error": "Mode 3/A codes must be numeric."}
        digits = raw.zfill(4)
        if len(digits) != 4:
            return {
                "code": digits,
                "valid": False,
                "error": "Mode 3/A codes use exactly four octal digits (0000-7777).",
            }
        if any(ch not in "01234567" for ch in digits):
            return {
                "code": digits,
                "valid": False,
                "error": "Mode 3/A codes are octal; use digits 0-7 only.",
            }
        return {"code": digits, "valid": True, "error": None}

    def lookup(self, code):
        """Look up squawk details.

        Args:
            code: Mode 3/A squawk to evaluate.

        Returns:
            Dict containing validation, allocation hits, ARTCC hits, and closest hint.
        """
        normalized = self.normalize_code(code)
        result = {
            "input": str(code),
            "code": normalized.get("code"),
            "valid": normalized["valid"],
            "error": normalized.get("error"),
            "table_a": [],
            "artcc": [],
            "closest": None,
        }
        if not normalized["valid"]:
            numeric_guess = self._numeric_value(normalized.get("code"))
            if numeric_guess is not None:
                result["closest"] = self._closest_hint(numeric_guess, exclude_exact=False)
            return result

        code_value = int(normalized["code"])
        result["table_a"] = self._match_table_a(code_value)
        result["artcc"] = self._match_artcc(code_value)

        if not result["table_a"] and not result["artcc"]:
            result["closest"] = self._closest_hint(code_value, exclude_exact=True)
        return result

    def format_summary(self, lookup_result, verbose=False):
        """Convert a lookup result to readable text.

        Args:
            lookup_result: Dict from lookup().
            verbose: Whether to append the priority legend.

        Returns:
            String ready for CLI display.
        """
        code = lookup_result.get("code") or lookup_result.get("input")
        lines = []
        if not lookup_result["valid"]:
            lines.append(f"Squawk {code}: invalid Mode 3/A ({lookup_result['error']})")
        else:
            known = bool(lookup_result["table_a"] or lookup_result["artcc"])
            lines.append(f"Squawk {code}")
            lines.append(f"Status: {'allocation found' if known else 'no allocation found'}")

            lines.append("Allocations:")
            if lookup_result["table_a"]:
                for entry in lookup_result["table_a"]:
                    lines.append(f"  - {entry['range']}: {entry['allocation']}")
            else:
                lines.append("  - none")

            lines.append("ARTCC assignments:")
            if lookup_result["artcc"]:
                for hit in lookup_result["artcc"]:
                    meta_bits = []
                    if hit["name"]:
                        meta_bits.append(hit["name"])
                    if hit["icao"]:
                        meta_bits.append(hit["icao"])
                    label = f"{hit['artcc']}" + (f" ({', '.join(meta_bits)})" if meta_bits else "")
                    detail_bits = []
                    if hit["category"]:
                        detail_bits.append(hit["category"])
                    if hit["sequence"]:
                        detail_bits.append(hit["sequence"])
                    if hit["order"] is not None:
                        detail_bits.append(f"order {hit['order']}")
                    detail_text = "; ".join(detail_bits) if detail_bits else None
                    summary = f"{label} | {hit['range']} | {hit['priority']}"
                    if detail_text:
                        summary += f" | {detail_text}"
                    lines.append(f"  - {summary}")
            else:
                lines.append("  - none")

        if lookup_result.get("closest"):
            hint = lookup_result["closest"]
            extra = []
            if hint.get("artcc"):
                artcc_label = hint["artcc"]
                if hint.get("name"):
                    artcc_label += f" ({hint['name']})"
                extra.append(artcc_label)
            if hint.get("priority"):
                extra.append(f"priority {hint['priority']}")
            extras = f" [{' | '.join(extra)}]" if extra else ""
            lines.append(
                f"  Closest known range: {hint['range']} in {hint['source']}{extras} "
                f"(distance {hint['distance']})."
            )

        if verbose:
            lines.append("  Priority key: categories (E External, I Internal, M Military, S Special Use); "
                         "sequence (P Primary, S Secondary, T Tertiary).")
        return "\n".join(lines)

    def _match_table_a(self, code_value):
        """Find Table A allocations that cover the given code."""
        matches = []
        for entry in self.special_allocations:
            for start, end in entry["codes"]:
                eff_start, eff_end, include_nondiscrete = self._effective_range(
                    start, end, entry.get("block", False)
                )
                in_range = eff_start <= code_value <= eff_end
                if in_range or (include_nondiscrete and code_value == start):
                    matches.append(
                        {
                            "range": self._format_range(eff_start, eff_end),
                            "allocation": entry["allocation"],
                        }
                    )
                    break
        return matches

    def _match_artcc(self, code_value):
        """Find ARTCC assignments that cover the given code."""
        matches = []
        for artcc, ranges in self.artcc_assignments.items():
            meta = self.artcc_metadata.get(artcc, {})
            for start, end, priority in ranges:
                eff_start, eff_end, include_nondiscrete = self._effective_range(start, end, treat_block=True)
                in_range = eff_start <= code_value <= eff_end
                if in_range or (include_nondiscrete and code_value == start):
                    decoded = self._decode_priority(priority)
                    matches.append(
                        {
                            "artcc": artcc,
                            "name": meta.get("name"),
                            "icao": meta.get("icao"),
                            "range": self._format_range(eff_start, eff_end),
                            "priority": priority,
                            "category": decoded.get("category"),
                            "sequence": decoded.get("sequence"),
                            "order": decoded.get("order"),
                            "explanation": decoded.get("explanation"),
                        }
                    )
        matches.sort(key=lambda item: (item["artcc"], item["range"]))
        return matches

    def _decode_priority(self, priority):
        """Decode EP/ES/ET/IP/IS/IT/ATOP codes into human text."""
        if priority == "ATOP":
            return {
                "category": None,
                "sequence": None,
                "order": None,
                "explanation": ATOP_EXPLANATION,
            }
        prefix, order = priority, None
        if "-" in priority:
            prefix, order_part = priority.split("-", 1)
            if order_part.isdigit():
                order = int(order_part)
        category = CATEGORY_NAMES.get(prefix[0]) if prefix else None
        sequence = SEQUENCE_NAMES.get(prefix[1:]) if len(prefix) > 1 else None
        explanation_bits = []
        if category:
            explanation_bits.append(category)
        if sequence:
            explanation_bits.append(sequence)
        if order is not None:
            explanation_bits.append(f"adaptation order {order}")
        return {
            "category": category,
            "sequence": sequence,
            "order": order,
            "explanation": ", ".join(explanation_bits) if explanation_bits else None,
        }

    def _closest_hint(self, code_value, exclude_exact):
        """Return the nearest known range when there is no direct hit."""
        best = None

        def consider(source, start, end, payload):
            in_range = start <= code_value <= end
            if exclude_exact and in_range:
                return
            distance = 0 if in_range else min(abs(code_value - start), abs(code_value - end))
            nonlocal best
            if best is None or distance < best["distance"]:
                best = {
                    "source": source,
                    "range": self._format_range(start, end),
                    "distance": distance,
                }
                best.update(payload)

        for entry in self.special_allocations:
            for start, end in entry["codes"]:
                eff_start, eff_end, _ = self._effective_range(start, end, entry.get("block", False))
                consider("allocations", eff_start, eff_end, {"priority": None, "artcc": None, "name": None})

        for artcc, ranges in self.artcc_assignments.items():
            meta = self.artcc_metadata.get(artcc, {})
            for start, end, priority in ranges:
                eff_start, eff_end, _ = self._effective_range(start, end, treat_block=True)
                consider(
                    "ARTCC assignments",
                    eff_start,
                    eff_end,
                    {"priority": priority, "artcc": artcc, "name": meta.get("name")},
                )

        return best

    def _numeric_value(self, code):
        """Safely parse an integer code value."""
        try:
            return int(code)
        except Exception:
            return None

    def _format_range(self, start, end):
        """Render a start/end pair as a squawk range string."""
        if start == end:
            return f"{start:04d}"
        return f"{start:04d}-{end:04d}"

    def _effective_range(self, start, end, treat_block=False):
        """Expand nondiscrete block references (xx00) to cover the block."""
        if treat_block and start == end and start != 0 and start % 100 == 0:
            # Block code: include nondiscrete xx00 plus xx01-xx77.
            return start, start + 77, True
        return start, end, True
