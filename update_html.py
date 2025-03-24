import sys
import time

# Get input values from command-line arguments
new_title = sys.argv[1] if len(sys.argv) > 1 else "Welcome to My Site"
build_number = sys.argv[2] if len(sys.argv) > 2 else "N/A"
pipeline_name = sys.argv[3] if len(sys.argv) > 3 else "N/A"
duration = sys.argv[4] if len(sys.argv) > 4 else "N/A"

# File path
html_file = "/mnt/d/Devops/Project/DockerVolume/nginx/index.html"

# Read existing file
with open(html_file, "r") as file:
    content = file.read()

# Replace title tag
new_content = content.replace(
    '<h1 class="title">', f'<h1 class="title">{new_title} - Build {build_number}</h1>\n'
)

# Append build metadata at the end
metadata = f"""
<!-- Updated by Jenkins -->
<!-- Pipeline: {pipeline_name} -->
<!-- Build Number: {build_number} -->
<!-- Duration: {duration} seconds -->
"""

new_content += metadata

# Write back to file
with open(html_file, "w") as file:
    file.write(new_content)

print(f"✅ index.html updated successfully with title: {new_title} (Build {build_number})")
