# jUnitXML2HTML
Tool, that converts jUnit XML reports into HTML reports.

## Usage
in Python:
    from xml2htmlreport import cli
    cli.run(arguments={
        'xml_folder': 'path/to/xml_folder', # where your's xml report is placed
        'html_folder': 'path/to/html_folder', # where you want to place html report
        'screen_shots_folder': 'path/to/screen_shots_folder', # where your's screenshots is placed
        'title': 'Test Run Report'
        })

from console:
    xml2htmlreport
    usage: xml2htmlreport-script.py [-h] [-x XML_FOLDER] [-d HTML_FOLDER]
                                    [-s SCREEN_SHOTS_FOLDER] [-t TITLE]
    
    jUnit XML2HTML Report Converter CLI
    
    optional arguments:
      -h, --help            show this help message and exit
      -x XML_FOLDER, --xml_folder XML_FOLDER
                            a path to a folder with XML report to convert
      -d HTML_FOLDER, --html_folder HTML_FOLDER
                            a path to a folder where HTML report will be placed
      -s SCREEN_SHOTS_FOLDER, --screen_shots_folder SCREEN_SHOTS_FOLDER
                            a path to a folder with screenshots
      -t TITLE, --title TITLE
                            a unique test report title