from pathlib import Path
import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: create_project.py <project_name> <manifest_id> <manifest_id> ...')
        sys.exit(1)

    content = Path("content")
    project = content / sys.argv[1]
    project.mkdir()

    with (project / "_index.md").open("w") as f:
        f.write("---\n")
        f.write(f"title: {sys.argv[1]}\n")
        f.write("type: project\n")
        f.write("---\n")

    for manifest_id in sys.argv[2:]:
        item = project / f"{manifest_id}.md"
        params = {
            "title": manifest_id,
            "layout": "viewer",
            "manifestId": manifest_id,
            "draft": False
        }
        with item.open("wt") as f:
            f.write("---\n")
            for k, v in params.items():
                f.write(f"{k}: {v}\n")
            f.write("---\n")


if __name__ == '__main__':
    main()