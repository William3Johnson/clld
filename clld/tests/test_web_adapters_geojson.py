from mock import Mock

from clld.db.models.common import Parameter, Language
from clld.tests.util import TestWithEnv
from clld.web.adapters import geojson

geojson.pacific_centered()


class Tests(TestWithEnv):
    def test_GeoJsonParameter(self):
        adapter = geojson.GeoJsonParameter(None)
        self.assertTrue(
            '{' in adapter.render(Parameter.get('no-domain'), self.env['request']))

        self.set_request_properties(params=dict(domainelement='de'))
        self.assertTrue(
            '{' in adapter.render(Parameter.get('parameter'), self.env['request']))

    def test_GeoJsonParameterMultipleValueSets(self):
        adapter = geojson.GeoJsonParameterMultipleValueSets(None)
        self.assertTrue(
            '{' in adapter.render(Parameter.get('no-domain'), self.env['request']))

    def test_GeoJsonParameterFlatProperties(self):
        adapter = geojson.GeoJsonParameterFlatProperties(None)
        self.assertTrue(
            '{' in adapter.render(Parameter.get('no-domain'), self.env['request']))

    def test_GeoJsonLanguages(self):
        class MockLanguages(Mock):
            def get_query(self, *args, **kw):
                return [Language.first()]

        adapter = geojson.GeoJsonLanguages(None)
        self.assertTrue(
            '{' in adapter.render(MockLanguages(), self.env['request']))

    def test_get_lonlat(self):
        self.assertIsNone(geojson.get_lonlat(None))
        self.assertIsNone(geojson.get_lonlat((None, 5)))
        self.assertGreater(geojson.get_lonlat((-50, 1))[0], 0)
        self.assertAlmostEquals(geojson.get_lonlat(Mock(latitude=1, longitude=1)), (1, 1))

    def test_get_feature(self):
        l = Language.first()
        self.assertEquals(geojson.get_feature(l)['id'], l.id)
        self.assertEquals(geojson.get_feature(l)['properties']['name'], l.name)
        self.assertEquals(geojson.get_feature(l, name='geo')['properties']['name'], 'geo')