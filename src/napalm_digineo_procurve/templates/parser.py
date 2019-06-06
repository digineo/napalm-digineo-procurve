import napalm_digineo_procurve.templates.reader


def parse(raw_data: str, template_name: str):
    t = napalm_digineo_procurve.templates.reader.read_template(template_name)
    return t.ParseText(raw_data)
