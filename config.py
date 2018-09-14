# Configuration 
#   for mybibtex, import.py, ...

from string import Template

# List of all conferences, journals, eprint, ...

confs = {}


def add_conf(
        key,
        full_name="",
        name=None,
        url="http://dblp.uni-trier.de/db/conf/${namelower}/${namelower}${url_year}${dis}.html",
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
        url="http://www.informatik.uni-trier.de/~ley/db/journals/${name}/${name}${volume}.html",
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
                "journal": journalkey,
                "month": "%months"  # months is used here
            }
    }


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
add_conf("CCS", "ACM Conference on Computer and Communications Security",
         name="ACM CCS", crossref="ccs",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/ccs/ccs${url_year}.html")
add_conf("ACNS", "International Conference on Applied Cryptography and Network Security")
add_conf("AFRICACRYPT", "International Conference on Cryptology in Africa")
add_conf("ASIACCS", "ACM Symposium on Information, Computer and Communications Security",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/ccs/asiaccs${url_year}.html")
add_conf("AC", "International Conference on the Theory and Application of Cryptology and Information Security",
         name="ASIACRYPT")
add_conf("CANS", "International Conference on Cryptology and Network Security")
add_conf("CHES", "Workshop on Cryptographic Hardware and Embedded Systems")
add_conf("CQRE", "International Exhibition and Congress on Network Security", name="CQRE")
add_conf("C", "International Cryptology Conference", name="CRYPTO")
add_conf("RSA", "RSA Conference, Cryptographers' Track", name="CT-RSA",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/ctrsa/ctrsa${url_year}.html")
add_conf("ESORICS", "European Symposium on Research in Computer Security")
add_conf("EC", "International Conference on the Theory and Applications of Cryptographic Techniques",
         name="EUROCRYPT")
add_conf("FC", "Financial Cryptography and Data Security")
add_conf("FCW", "Financial Cryptography and Data Security Workshops",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/fc/fc${url_year}w.html")
add_conf("FOCS", "Symposium on Foundations of Computer Science")
add_conf("FSE", "International Workshop on Fast Software Encryption")
add_conf("ICALP", "International Colloquium on Automata, Languages and Programming")
add_conf("ICICS", "International Conference on Information and Communications Security")
add_conf("ICISC", "International Conference on Information Security and Cryptology")
add_conf("IMA", "IMA Conference on Cryptography and Coding")
add_conf("ICITS", "International Conference on Information Theoretic Security")
add_conf("SP", "IEEE Symposium on Security and Privacy", name="IEEE SP",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/sp/sp${url_year}.html", crossref="ieeesp")
add_conf("INDOCRYPT", "International Conference on Cryptology in India")
add_conf("ISC", "Information Security Conference",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/isw/isc${url_year}.html")
add_conf("ITCS", "Innovations in Theoretical Computer Science",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/innovations/innovations${url_year}.html")
add_conf("IWSEC", "International Workshop on Security")
add_conf("LATIN", "Latin American Theoretical Informatics Symposium")
add_conf("LC", "International Conference on Cryptology and Information Security in Latin America",
         name="LATINCRYPT")
add_conf("NDSS", "Network and Distributed System Security Symposium")
add_conf("PAIRING", "International Conference on Pairing-based Cryptography", )
add_conf("PKC", "International Conference on Practice and Theory in Public Key Cryptography")
add_conf("PODC", "ACM SIGACT-SIGOPS Symposium on Principles of Distributed Computing")
add_conf("PROVSEC", "International Conference on Provable Security")
add_conf("SAC", "Workshop on Selected Areas in Cryptography",
         url="http://www.informatik.uni-trier.de/~ley/db/conf/sacrypt/sacrypt${url_year}.html")
add_conf("SCN", "Conference on Security and Cryptography for Networks")
add_conf("SODA", "ACM-SIAM Symposium on Discrete Algorithms")
add_conf("STOC", "ACM Symposium on Theory of Computing")
add_conf("TCC", "Theory of Cryptography Conference")
add_conf("TRUSTBUS", "International Conference on Trust, Privacy &amp; Security in Digital Business")
add_conf("VIETCRYPT", "International Conference on Cryptology in Vietnam")
add_conf("WISA", "International Workshop on Information Security Applications")

add_journal("JC", 1988, "jcrypto", "Journal of Cryptology",
            months=["jan", "apr", "jul", "oct"],
            url="http://www.informatik.uni-trier.de/~ley/db/journals/joc/joc${volume}.html")

# Warning: we are not using the import.py script for ToSC
#          therefore, some of the fields here are not used
add_journal("ToSC", 2016, "tosc", "Transactions on Symmetric Cryptology",
            months=[],
            url="http://dblp2.uni-trier.de/db/journals/tosc/tosc${year}.html")

add_journal("TCHES", 2018, "tches", "Transactions on Cryptographic Hardware and Embedded Systems",
            months=[],
            url="https://dblp.uni-trier.de/db/journals/tches/tches${year}.html")

add_misc("EPRINT", "Cryptology ePrint Archive", url="http://eprint.iacr.org/${year}")


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
    "IMA": {1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018},
    "ISC": {1998},
    "LATIN": {1993, 1994, 1996, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017},
    "LC": {2011, 2013},
    "PAIRING": {2011},
    "SCN": {2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017},
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
