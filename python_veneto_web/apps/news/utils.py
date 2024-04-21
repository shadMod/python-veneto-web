import os.path

import markdown


def clean_html(value: str, tag_html: str = "p") -> str:
    """Cleans up the value with selected html tags.

    Parameters
    ----------
    value : str
        The value to clean.
    tag_html : str
        The html tag to clean.

    Returns
    -------
    str
        Return cleaned value.
    """
    value = value.replace(f"<{tag_html}>", "").replace(f"</{tag_html}>", "")
    return value


def get_data_from_markdown(
    markdown_path: str, with_article: bool = True
) -> dict | None:
    """Get data from markdown.

    Parameters
    ----------
    markdown_path : str
        The markdown file path.
    with_article : bool
        True if you want it to return the whole article, False otherwise.

    Returns
    -------
    dict | None
        The data file path.
    """
    if not os.path.exists(markdown_path):
        return None

    with open(markdown_path, "r") as fn:
        render_html = markdown.markdown(fn.read())
        row_list = render_html.split("\n")
        header = [row for row in row_list[:3]]
        data = {
            "title": clean_html(header[0]),
            "author": clean_html(header[1]),
            "date": clean_html(header[2]),
            "file_path": os.path.basename(markdown_path).replace(".md", ""),
        }
        if with_article:
            body = [row for row in row_list[3:]]
            data["article"] = "".join(body)
    return data
