import os
import xml.etree.ElementTree as ET
import json

source_folder = "/home/.../decomiled_apks"
output_path = "/home/../manifest_output/"


def parse_android_manifest(manifest_path):
    # Parse the XML file
    tree = ET.parse(manifest_path)
    root = tree.getroot()

    components = {}

    # Find all activity elements
    activity_elements = root.findall(".//activity")
    service_elements = root.findall(".//service")
    package_name = root.attrib.get('package')

    services = []
    activities = []

    for service_element in service_elements:
        service = {"name": service_element.get("{http://schemas.android.com/apk/res/android}name")}
        services.append(service)

    components['services'] = services

    # Iterate over each activity element
    for activity_element in activity_elements:
        activity = {}

        # Get the activity attributes
        activity["name"] = activity_element.get("{http://schemas.android.com/apk/res/android}name")
        activity["launchMode"] = activity_element.get("{http://schemas.android.com/apk/res/android}launchMode")
        activity["taskAffinity"] = activity_element.get("{http://schemas.android.com/apk/res/android}taskAffinity")
        activity["finishOnTaskLaunch"] = activity_element.get(
            "{http://schemas.android.com/apk/res/android}finishOnTaskLaunch")
        activity["noHistory"] = activity_element.get("{http://schemas.android.com/apk/res/android}noHistory")
        activity["allowTaskReparenting"] = activity_element.get(
            "{http://schemas.android.com/apk/res/android}allowTaskReparenting")
        activity["documentLaunchMode"] = activity_element.get(
            "{http://schemas.android.com/apk/res/android}documentLaunchMode")
        activity["excludeFromRecents"] = activity_element.get(
            "{http://schemas.android.com/apk/res/android}excludeFromRecents")

        # Find intent filter elements
        intent_filter_elements = activity_element.findall("intent-filter")

        # Iterate over each intent filter element
        intent_filters = []
        for intent_filter_element in intent_filter_elements:
            intent_filter = {"actions": [action.get("{http://schemas.android.com/apk/res/android}name") for action in
                                         intent_filter_element.findall("action")],
                             "categories": [category.get("{http://schemas.android.com/apk/res/android}name") for
                                            category
                                            in intent_filter_element.findall("category")],
                             "data": [data.get("{http://schemas.android.com/apk/res/android}scheme") for data in
                                      intent_filter_element.findall("data")]}

            # Get the intent filter attributes

            intent_filters.append(intent_filter)

        activity["intentFilters"] = intent_filters

        activities.append(activity)

    components['activities'] = activities
    components['packageName'] = package_name

    return components


def search_android_manifest(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if "AndroidManifest.xml" in files:
            manifest_path = os.path.join(root, "AndroidManifest.xml")
            return manifest_path

    return None


subfolders = [subfolder for subfolder in os.listdir(source_folder) if
              os.path.isdir(os.path.join(source_folder, subfolder))]

print(subfolders)


def save_file(apk_name, parsed_activities, output_path):
    apk_details = {"apkName": apk_name, "activityDetails": parsed_activities}
    with open(output_path + apk_name + ".json", "w") as activity_json:
        json.dump(apk_details, activity_json, indent=4, sort_keys=True)

    pass


for sf in subfolders:
    manifest_path = search_android_manifest(source_folder + "/" + sf)
    if manifest_path:
        print("AndroidManifest.xml found at:", manifest_path)
        parsed_activities = parse_android_manifest(manifest_path)
        save_file(sf, parsed_activities, output_path)
    else:
        print("AndroidManifest.xml not found in the folder.")

# Example usage
