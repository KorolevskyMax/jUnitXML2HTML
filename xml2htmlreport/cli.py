# coding=utf-8

import argparse
import sys

from xml2htmlreport.xml2html import copy_static, get_features_and_convert_into_dict, parse_screenshots, \
    get_overall_results, \
    render_templates


parser = argparse.ArgumentParser(
    description="jUnit XML2HTML Report Converter CLI",
)
parser.add_argument(
    "-x", "--xml_folder",
    action="store",
    dest="xml_folder",
    type=str,
    help="a path to a folder with XML report to convert"
)
parser.add_argument(
    "-d", "--html_folder",
    action="store",
    dest="html_folder",
    type=str,
    help="a path to a folder where HTML report will be placed"
)
parser.add_argument(
    "-s", "--screen_shots_folder",
    action="store",
    dest="screen_shots_folder",
    type=str,
    help="a path to a folder with screenshots"
)
parser.add_argument(
    "-t", "--title",
    action="store",
    dest="title",
    type=str,
    help="a unique test report title"
)


def parse_args(args):
    arguments = vars(parser.parse_args(args=args or ["--help"]))
    return arguments


def main(args=sys.argv[1:]):
    sys.exit(run(arguments=parse_args(args=args)))
    # if len(sys.argv) < 6:
    # sys.exit("\nTo run the command\n"
    #              "--xml_folder '/home/user_name/test-results'\n"
    #              "--html_folder '/home/user_name/test-results/html'\n"
    #              "--screen_shots_folder '/home/user_name/test-results/screenshots'\n"
    #              "--title '<Project_Name> Test run #123'\n")


def run(arguments, stdout=sys.stdout, stderr=sys.stderr):
    copy_static(arguments)
    features_results = get_features_and_convert_into_dict(arguments)
    parse_screenshots(arguments, features_results)
    features_results['page'] = dict(title=getattr(arguments, 'title', 'Test Run Report'))
    get_overall_results(features_results)
    render_templates(arguments, features_results)
