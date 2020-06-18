from carte.models import Direction, EtatSite
from datetime import datetime
from django.utils.safestring import mark_safe

def get_paragraph() -> str:
    etats_site = EtatSite.objects.all()
    production = get_production_dict(etats_site)
    paragraph_args = get_paragraph_args(etats_site, production)
    paragraph = """\
        Au {date}, nous avons {nombre_dev} sites DDSP en {dev}, {nombre_preco} sites en {preco}.<br>\
        {production}<br>\
        {production_disa}<br>\
        Suite a l'accord avec la DCPAF, les sites de la DZPAF 33, 35, 78 et DDPAF 78 sont dorénavent suivis par nos\
        services pour leur futur site intranet.\
    """.format(**paragraph_args)
    paragraph = mark_safe(paragraph)
    return paragraph


def get_production_dict(etats_site: list,) -> dict:
    production = Direction.objects.filter(etat_site=etats_site[3])
    en_prod = []
    en_prod_disa = []
    for site in production:
        if site.name != site.map_code:
            en_prod.append(site.name)
        else:
            en_prod_disa.append(site.name)
    en_prod = ", ".join(en_prod)
    en_prod = rreplace(en_prod, ", ", " et ", 1)
    en_prod_disa = ", ".join(en_prod_disa)
    en_prod_disa = rreplace(en_prod_disa, ", ", " et ", 1)
    if en_prod:
        en_prod = "Les sites des DDSP {} sont en production.".format(en_prod)
    else:
        en_prod = "Aucun site de DDSP n'est en production."
    if en_prod_disa:
        en_prod_disa = "Au niveau des DISA, les sites {} sont en production.".format(en_prod_disa)
    else:
        en_prod_disa = "Au niveau des DISA, aucun site n'est en production."
    return {"ddsp": en_prod, "disa": en_prod_disa}


def get_paragraph_args(etats_site: list, production: dict) -> dict:
    paragraph_args = {
        "date": datetime.strftime(datetime.now(), "%d/%m/%Y"),
        "nombre_dev": len(Direction.objects.filter(etat_site=etats_site[2])),
        "dev": etats_site[2].name,
        "nombre_preco": len(Direction.objects.filter(etat_site=etats_site[1])),
        "preco": etats_site[1].name,
        "production": production["ddsp"],
        "production_disa": production["disa"]
    }
    return paragraph_args

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)