import os.path

import markdown


def clean_html(value, tag_html: str = "p"):
    value = value.replace(f"<{tag_html}>", "").replace(f"</{tag_html}>", "")
    return value


def get_data_file_path_md(file_path: str, with_article: bool = True) -> dict | None:
    """Add me.

    :param file_path: Add me.
    :param with_article: Add me.
    :return: (str | None) Add me.
    """
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as fn:
        render_html = markdown.markdown(fn.read())
        row_list = render_html.split("\n")
        header = [row for row in row_list[:3]]
        data = {
            "title": clean_html(header[0]),
            "author": clean_html(header[1]),
            "date": clean_html(header[2]),
            "file_path": os.path.basename(file_path).replace(".md", ""),
        }
        if with_article:
            body = [row for row in row_list[3:]]
            data["article"] = "".join(body)
    return data
