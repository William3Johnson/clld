
def test_expand_prefix():
    from clld.lib.rdf import expand_prefix

    assert str(expand_prefix('dcterms:title')) == 'http://purl.org/dc/terms/title'
    assert expand_prefix('noprefix:lname') == 'noprefix:lname'
    assert expand_prefix('rdf:nolname') == 'rdf:nolname'
    assert expand_prefix('nocolon') == 'nocolon'


def test_url_for_qname():
    from clld.lib.rdf import url_for_qname

    assert url_for_qname('dcterms:title') == 'http://purl.org/dc/terms/title'


def test_properties_as_xml_snippet():
    from clld.lib.rdf import properties_as_xml_snippet

    properties_as_xml_snippet(
        'subject', [('foaf:name', 'a name'), ('foaf:homepage', 'http://example.org')])
    properties_as_xml_snippet(
        'subject', [('rdf:about', 'x'), ('foaf:homepage', 'http://example.org')])
    properties_as_xml_snippet(
        'subject', [('about', 'x'), ('foaf:homepage', 'http://example.org')])

    p = properties_as_xml_snippet(
        'http://example.org', [('dcterms:title', 'ttt')])
    assert 'ttt' in p


def test_convert():
    from clld.lib.rdf import ClldGraph, convert, FORMATS

    g = ClldGraph()
    for from_ in FORMATS:
        if from_ != 'nt':
            for to_ in list(FORMATS.keys()) + [None]:
                if to_ != 'nt':
                    convert(g.serialize(format=from_), from_, to_)
