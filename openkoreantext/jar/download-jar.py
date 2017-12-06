import re
import argparse

from urllib.request import urlopen
from xml.etree import ElementTree

metadata_url = 'http://central.maven.org/maven2/{group_identifier_as_path}/{artifact_identifier}/maven-metadata.xml'
jar_url = 'http://central.maven.org/maven2/{group_identifier_as_path}/{artifact_identifier}/{version}/{artifact_identifier}-{version}.jar'

def build_url(url, **kwargs):
    if 'group_identifier' in kwargs:
        kwargs['group_identifier_as_path'] = kwargs['group_identifier'].replace('.', '/')

    return url.format(**kwargs)

def retrieve_versions(group_identifier, artifact_identifier):
    url = build_url(
        metadata_url,
        group_identifier=group_identifier,
        artifact_identifier=artifact_identifier
    )
    with urlopen(url) as response:
        content = response.read()

    root = ElementTree.fromstring(content)

    versions = []
    for version_element in root.findall('versioning/versions/version'):
        match = re.search(r'^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$', version_element.text.strip())
        if match:
            versions.append((
                int(match.group('major')),
                int(match.group('minor')),
                int(match.group('patch'))
            ))

    return [
        '.'.join(map(str, version))
        for version in sorted(versions)
    ]

def download_jar(group_identifier, artifact_identifier, version, filename=None):
    url = build_url(
        jar_url,
        group_identifier=group_identifier,
        artifact_identifier=artifact_identifier,
        version=version
    )
    with urlopen(url) as response:
        if not filename:
            filename = '{artifact_identifier}-{version}.jar'.format(
                artifact_identifier=artifact_identifier,
                version=version
            )
        with open(filename, 'wb') as output_file:
            output_file.write(response.read())

parser = argparse.ArgumentParser(
    description='Download jar file from the maven repository',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('group_identifier', metavar='group-identifier', help='Group identifier (e.g., org.scala-lang)')
parser.add_argument('artifact_identifier', metavar='artifact-identifier', help='Artifact identifier (e.g., scala-library)')
parser.add_argument('version', nargs='?', default='latest', help='Version (e.g., 2.12.4)')
parser.add_argument('--filename', help='Filename to save')

arguments = parser.parse_args()

group_identifier = arguments.group_identifier
artifact_identifier = arguments.artifact_identifier
version = arguments.version
if version == 'latest':
    versions = retrieve_versions(group_identifier, artifact_identifier)
    version = versions[-1]
filename = arguments.filename

download_jar(group_identifier, artifact_identifier, version, filename)
