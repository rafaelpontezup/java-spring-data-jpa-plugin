import xml.etree.ElementTree as ET
from templateframework.metadata import Metadata
from templateframework.render.default_filters import DefaultFilters

def run(metadata: Metadata = None):
    tree = ET.parse('pom.xml')
    root = tree.getroot()
    for xml in root:
        if "groupId" in xml.tag:
            group = xml.tag
        if "artifactId" in xml.tag:
            artifact = xml.tag

    group_id = root.find(group)

    artifact_id = root.find(artifact)
    artifact_id_text = artifact_id.text.replace("-", "")

    package=f"{group_id.text}.{artifact_id_text}"
    path_main_code_directory= f"src.main.java.{package}"
    path_test_code_directory= f"src.test.java.{package}"

    filters = DefaultFilters().create()
    
    metadata.computed_inputs['package']=package
    metadata.computed_inputs['path_main_code_directory']=filters["group_id_folder"](path_main_code_directory)
    metadata.computed_inputs['path_test_code_directory']=filters["group_id_folder"](path_test_code_directory)

    return metadata