import sys

INDEX_FILE = "/mnt/d/Devops/Project/DockerVolume/nginx/index.html"

def update_index(new_title):
    with open(INDEX_FILE, "r") as file:
        content = file.read()

    updated_content = content.replace(
        '<h1 class="title">', f'<h1 class="title">{new_title}</h1>'
    )

    with open(INDEX_FILE, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_index.py <NEW_TITLE>")
        sys.exit(1)
    
    new_title = sys.argv[1]
    update_index(new_title)
    print(f"Updated index.html with title: {new_title}")
