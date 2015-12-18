# coding=utf-8

from distutils import dir_util, file_util
import os
from collections import OrderedDict

from jinja2 import Environment, PackageLoader
import xmltodict
from xml2htmlreport._filters import *


def get_features_and_convert_into_dict(args):
    all_files = list((f for f in os.listdir(os.path.abspath(args['xml_folder']))
                      if os.path.isfile(os.path.abspath(os.path.join(args['xml_folder'], f)))))
    json_features = OrderedDict({'features': []})
    for f in all_files:
        with open(os.path.join(args['xml_folder'], f)) as feature:
            json_features['features'].append(xmltodict.parse(feature.read()))
    return json_features


def get_overall_results(features_results):
    features_results['overall'] = OrderedDict([('features', ''), ('scenarios', '')])
    features_results['overall']['features'] = OrderedDict([('@errors', '0'),
                                                           ('@failures', '0'),
                                                           ('@skipped', '0'),
                                                           ('@tests', '0'),
                                                           ('@time', '0')])
    features_results['overall']['scenarios'] = OrderedDict([('@errors', '0'),
                                                            ('@failures', '0'),
                                                            ('@skipped', '0'),
                                                            ('@tests', '0'),
                                                            ('@time', '0')])
    for feature in features_results['features']:
        for key in features_results['overall']['scenarios']:
            features_results['overall']['scenarios'][key] = str(
                float(features_results['overall']['scenarios'][key]) + float(feature['testsuite'][key]))
        for key in features_results['overall']['features']:
            if feature['testsuite'][key] != '0' and key != '@time' and key != '@skipped':
                features_results['overall']['features'][key] = str(
                    int(features_results['overall']['features'][key]) + 1)
            elif key == '@skipped' and feature['testsuite'][key] != '0':
                if feature['testsuite']['@errors'] == '0' or feature['testsuite']['@failures'] == '0' or feature['testsuite']['@tests'] == '0':
                     features_results['overall']['features'][key] = str(
                        int(features_results['overall']['features'][key]) + 1)
            elif key == '@time':
                features_results['overall']['features'][key] = str(
                    float(features_results['overall']['features'][key]) + float(feature['testsuite'][key]))


def copy_static(args):
    if '../' in args['html_folder']:
        dir_util.copy_tree(os.path.join(os.path.dirname(__file__), 'static'),
                           os.path.join(os.path.abspath(args['html_folder']), 'static'))
    else:
        dir_util.copy_tree(os.path.join(os.path.dirname(__file__), 'static'),
                           os.path.join(os.path.abspath(args['html_folder']), 'static'))


def render_templates(args, features_results):
    env = Environment(loader=PackageLoader('xml2htmlreport', 'templates'))
    env.filters['nl2br'] = nl2br
    template = env.get_template('base.html')
    feature_template = env.get_template('feature.html')
    template.stream(features_results).dump(os.path.join(args['html_folder'], 'index.html'))
    count = 0
    for i in range(0, len(features_results['features'])):
        features_results['feature_number'] = i
        feature_template.stream(features_results).dump(os.path.join(args['html_folder'], "{}.html".format(
            features_results['features'][i]['testsuite']['@name'].split('.')[0])))


def parse_screenshots(args, features_results):
    try:
        all_screenshots = list((f for f in os.listdir(os.path.abspath(args['screen_shots_folder']))
                                if os.path.isfile(os.path.abspath(os.path.join(args['screen_shots_folder'], f)))))
    except FileNotFoundError:
        return features_results
    if not os.path.exists(os.path.join(args['html_folder'], 'static', 'img', 'screenshots')):
        os.makedirs(os.path.join(args['html_folder'], 'static', 'img', 'screenshots'))
    for feature in features_results['features']:
        if feature['testsuite']['@tests'] > '1':
            for testcase in feature['testsuite']['testcase']:
                testcase['images'] = []
                for screenshot in all_screenshots:
                    if "{}__{}".format(testcase['@classname'].split('.')[0], testcase['@name']) in screenshot:
                        testcase['images'].append(screenshot)
                        file_util.copy_file(os.path.join(args['screen_shots_folder'], screenshot),
                                            os.path.join(args['html_folder'], 'static', 'img', 'screenshots'))


