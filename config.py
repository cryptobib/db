# Configuration
#   for mybibtex, import.py, ...

from string import Template

# List of all conferences, journals, eprint, ...

confs = {}


def add_conf(
        key,
        full_name="",
        name=None,
        url="https://dblp.uni-trier.de/db/conf/${namelower}/${namelower}${url_year}${dis}.html",
        crossref=None
):
    if name is None:
        name = key
    if crossref is None:
        crossref = name.lower()

    confs[key] = {
        "type":
            "conf",
        "url":                # list of url(s) to retrieve the conf data (from DBLP)
            [
                Template(url).safe_substitute(namelower=name.lower(), url_year="${year}"),
                Template(url).safe_substitute(namelower=name.lower(), url_year="${short_year}")
            ],
        "entry_type":         # bibtex entry type to be looked for
            "InProceedings",
        "key":                # prefix of the bib key (ACISP, AC, ...) -> upper case
            key,
        "name":               # name of the conference (ACISP, ASIACRYPT, ...) -> upper case
            name,
        "crossref":           # name for crossref
            crossref,
        "full_name":          # full name of the conference
            full_name,
        "fields_dblp":        # fields to extract from DBLP
            {"title", "author", "pages", "doi"},
        "fields_add":
            {
                "crossref": crossref + "${short_year}${dis}"
            }
    }


def add_journal(
        key,
        first_year,
        journalkey,
        full_name="",
        months=None,
        name=None,
        url="https://dblp.uni-trier.de/db/journals/${name}/${name}${volume}.html",
        publisher="springer",
):
    if name is None:
        name = key
    if months is None:
        months = []

    confs[key] = {
        "type":
            "journal",
        "url":                # list of url(s) to retrieve the conf data (from DBLP)
            [url],
        "entry_type":         # bibtex entry type to be looked for
            "Article",
        "key":                # prefix of the bib key (ACISP, AC, ...) -> upper case
            key,
        "name":               # name of the conference (ACISP, ASIACRYPT, ...) -> upper case
            name,
        "full_name":          # full name of the conference
            full_name,
        "first_year":         # first year of the journal (used to convert years into volume numbers in import.py)
            first_year,
        "months":             # month from number
            months,
        "fields_dblp":        # fields to extract from DBLP
            {"title", "author", "pages", "volume", "year", "number", "doi"},
        "fields_add":
            {
                "publisher": publisher,
                "journal": journalkey
            }
    }
    if months:
        # if months is a non-empty array
        # then the import script will use months[number-1] as month for the publication
        confs[key]["fields_add"]["month"] = "%months" # months is used here automatically


def add_misc(
        key,
        full_name,
        url,
        name=None,
        crossref=None
):
    if name is None:
        name = key
    if crossref is None:
        crossref = name.lower()

    confs[key] = {
        "type":
            "misc",
        "url":                # list of url(s) to retrieve the misc data (currently only EPRINT is supported)
            [url],
        "entry_type":         # bibtex entry type to be looked for
            "Misc",
        "key":                # prefix of the bib key (ACISP, AC, ...) -> upper case
            key,
        "name":               # name of the conference (ACISP, ASIACRYPT, ...) -> upper case
            name,
        "crossref":           # name for crossref (not used yet)
            crossref,
        "full_name":          # full name of the conference (not used yet)
            full_name,
        "fields_dblp":        # not used
            set(),
        "fields_add":         # not used
            dict([])
    }


add_conf("ACISP", "Australasian Conference on Information Security and Privacy")
# WARNING:
# the URL for ACM CCS 2006 is https://dblp.org/db/conf/ccs/ccs2006usa.html (without the suffix "usa", it is AsiaCCS)
# the URL for ACM CCS 2004 is https://dblp.uni-trier.de/db/conf/ccs/ccs2004p.html (wihtout the suffix "p", it is FMSE)
# These are the only exceptions
# If you want to re-import these conferences, the simplest (dirty) way is to hardcode the URL below
add_conf("CCS", "ACM Conference on Computer and Communications Security",
         name="ACM CCS", crossref="ccs",
         url="https://dblp.uni-trier.de/db/conf/ccs/ccs${url_year}.html")
add_conf("ACNS", "International Conference on Applied Cryptography and Network Security")
add_conf("AFRICACRYPT", "International Conference on Cryptology in Africa")
add_conf("ASIACCS", "ACM Symposium on Information, Computer and Communications Security",
         url="https://dblp.uni-trier.de/db/conf/asiaccs/asiaccs${url_year}.html")
add_conf("AC", "International Conference on the Theory and Application of Cryptology and Information Security",
         name="ASIACRYPT")
add_conf("CANS", "International Conference on Cryptology and Network Security")
add_conf("CHES", "Workshop on Cryptographic Hardware and Embedded Systems")
add_conf("COSADE", "International Workshop on Constructive Side-Channel Analysis and Secure Design")
add_conf("CQRE", "International Exhibition and Congress on Network Security", name="CQRE")
# Some CSF ('07-'16) are labeled csfw/csf, remaining csfw/csfw
# 
add_conf("CSF", "IEEE Computer Security Foundations Symposium", name="CSF", url="https://dblp.uni-trier.de/db/conf/csfw/csfw${url_year}.html")
add_conf("C", "International Cryptology Conference", name="CRYPTO")
add_conf("RSA", "RSA Conference, Cryptographers' Track", name="CT-RSA", crossref="rsa",
         url="https://dblp.uni-trier.de/db/conf/ctrsa/ctrsa${url_year}.html")
add_conf("ESORICS", "European Symposium on Research in Computer Security")
add_conf("EC", "International Conference on the Theory and Applications of Cryptographic Techniques",
         name="EUROCRYPT")
add_conf("FC", "Financial Cryptography and Data Security")
add_conf("FCW", "Financial Cryptography and Data Security Workshops",
         url="https://dblp.uni-trier.de/db/conf/fc/fc${url_year}w.html")
add_conf("FOCS", "Symposium on Foundations of Computer Science")
add_conf("FSE", "International Workshop on Fast Software Encryption")
add_conf("ICALP", "International Colloquium on Automata, Languages and Programming")
add_conf("ICICS", "International Conference on Information and Communications Security")
add_conf("ICISC", "International Conference on Information Security and Cryptology")
add_conf("IMA", "IMA Conference on Cryptography and Coding",url="https://dblp.uni-trier.de/db/conf/ima/imacc${url_year}.html")
add_conf("ICITS", "International Conference on Information Theoretic Security")
add_conf("SP", "IEEE Symposium on Security and Privacy", name="IEEE SP",
         url="https://dblp.uni-trier.de/db/conf/sp/sp${url_year}.html", crossref="ieeesp")
add_conf("INDOCRYPT", "International Conference on Cryptology in India")
add_conf("ISC", "Information Security Conference",
         url="https://dblp.uni-trier.de/db/conf/isw/isc${url_year}.html")
add_conf("ITC", "Information-Theoretic Cryptography",
         url="https://dblp.uni-trier.de/db/conf/icits/itc${url_year}.html")
add_conf("ITCS", "Innovations in Theoretical Computer Science",
         url="https://dblp.uni-trier.de/db/conf/innovations/innovations${url_year}.html")
add_conf("IWSEC", "International Workshop on Security")
add_conf("LATIN", "Latin American Theoretical Informatics Symposium")
add_conf("LC", "International Conference on Cryptology and Information Security in Latin America",
         name="LATINCRYPT")
add_conf("NDSS", "Network and Distributed System Security Symposium")
add_conf("PAIRING", "International Conference on Pairing-based Cryptography", )
add_conf("PETS", "International Symposium on Privacy Enhancing Technologies", url="https://dblp.uni-trier.de/db/conf/pet/pets${url_year}.html")
add_conf("PKC", "International Conference on Practice and Theory in Public Key Cryptography")
add_conf("PODC", "ACM SIGACT-SIGOPS Symposium on Principles of Distributed Computing")
add_conf("PQCRYPTO", "International Conference on Post-Quantum Cryptography")
add_conf("PROVSEC", "International Conference on Provable Security")
add_conf("SAC", "Workshop on Selected Areas in Cryptography",
         url="https://dblp.uni-trier.de/db/conf/sacrypt/sacrypt${url_year}.html")
add_conf("SCN", "Conference on Security and Cryptography for Networks")
add_conf("SODA", "ACM-SIAM Symposium on Discrete Algorithms")
add_conf("STOC", "ACM Symposium on Theory of Computing")
add_conf("TCC", "Theory of Cryptography Conference")
add_conf("TRUSTBUS", "International Conference on Trust, Privacy &amp; Security in Digital Business")
add_conf("USENIX", "USENIX Security Symposium",
         url="https://dblp.uni-trier.de/db/conf/uss/uss${url_year}.html")
add_conf("VIETCRYPT", "International Conference on Cryptology in Vietnam")
add_conf("WISA", "International Workshop on Information Security Applications")

add_journal("JC", 1988, "jcrypto", "Journal of Cryptology",
            months=["jan", "apr", "jul", "oct"],
            url="https://dblp.uni-trier.de/db/journals/joc/joc${volume}.html")

add_journal("JCEng", 2011, "jcryptoeng", "Journal of Cryptographic Engineering",
            months=["apr", "jun", "sep", "nov"],
            url="https://dblp.uni-trier.de/db/journals/jce/jce${volume}.html")

add_journal("PoPETS", 2022, "popets", "Proceedings on Privacy Enhancing Technologies",
            months=["jan", "apr", "jul", "oct"],
            url="https://dblp.uni-trier.de/db/journals/popets/popets${year}.html")

# Note: PoPETS is now self-publishing!
# add_journal("PoPETS", 2015, "popets", "Proceedings on Privacy Enhancing Technologies",
#             months=["jan", "apr", "jul", "oct"],
#             url="https://dblp.uni-trier.de/db/journals/popets/popets${year}.html",
#             publisher="degruyter")

# Warning: we are not using the import.py script for ToSC
#          therefore, some of the fields here are not used
add_journal("ToSC", 2016, "tosc", "Transactions on Symmetric Cryptology",
            months=[],
            url="https://dblp.uni-trier.de/db/journals/tosc/tosc${year}.html")

add_journal("TCHES", 2018, "tches", "Transactions on Cryptographic Hardware and Embedded Systems",
            months=[],
            url="https://dblp.uni-trier.de/db/journals/tches/tches${year}.html",
            publisher="tchespub")

add_misc("EPRINT", "Cryptology ePrint Archive", url="https://eprint.iacr.org/complete/compact")


def get_conf_name(confkey):
    if confkey in confs:
        return confs[confkey]["name"]
    else:
        return confkey.upper()


# Missing years for conferences (used by lib.confs_years

confs_missing_years = {
    "AC": {1993, 1995, 1997},
    "AFRICACRYPT": {2015},
    "CCS": {1995},
    "EC": {1983},
    "ESORICS": {1991, 1993, 1995, 1997, 1999, 2001},
    "FSE": {1995},
    "ICICS": {1998, 2000},
    "ICITS": {2010, 2014},
    "IMA": {1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020},
    "ISC": {1998},
    "LATIN": {1993, 1994, 1996, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019},
    "LC": {2011, 2013, 2016, 2018, 2020},
    "PAIRING": {2011},
    "PQCRYPTO": {2009, 2012, 2015},
    "SCN": {2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019},
    "USENIX": {1994, 1997},
}

# Bibtex output

# keys of entries are sorted in this order: first_keys then alphabetical order
first_keys = ["author", "title", "pages", "editor", "booktitle", "volume", "address", "month", "publisher", "series",
              "year", "journal", "number", "doi"]

types = {
    "inproceedings": "InProceedings",
    "article": "Article",
    "proceedings": "Proceedings",
    "misc": "Misc"
}
