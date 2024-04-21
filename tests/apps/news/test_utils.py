import os
import tempfile
import unittest

from python_veneto_web.apps.news.utils import (
    clean_html,
    get_data_from_markdown,
)


class TestAppsNewsUtils(unittest.TestCase):
    def setUp(self):
        data_sample = """
Title sample

Author sample

01/01/2024

Donec lobortis odio ante, non euismod metus accumsan quis. Donec nulla lacus, volutpat non lacus eget, molestie
condimentum elit. Ut non erat ac metus condimentum ornare.
        """
        fd, self.path = tempfile.mkstemp()
        with os.fdopen(fd, "w") as tmp:
            tmp.write(data_sample)

    def test_clean_html_should_correctly_clean_html(self):
        value = "<p>Lorem ipsum dolor sit amet</p>"
        expected_value = "Lorem ipsum dolor sit amet"
        clean_value = clean_html(value)
        assert clean_value == expected_value

    def test_get_data_from_markdown_should_return_none_if_path_not_exists(
        self,
    ):
        wrong_path = "/path/to/markdown.md"
        data = get_data_from_markdown(wrong_path)
        assert data is None

    def test_get_data_from_markdown_should_return_correctly_data_with_article(
        self,
    ):
        data = get_data_from_markdown(self.path)
        assert data["title"] == "Title sample"
        assert data["author"] == "Author sample"
        assert data["date"] == "01/01/2024"
        assert data["file_path"] == self.path.split("/")[-1]
        assert data["article"] == (
            "<p>Donec lobortis odio ante, non euismod metus accumsan quis. Donec nulla lacus, "
            "volutpat non lacus eget, molestiecondimentum elit. Ut non erat ac metus condimentum ornare.</p>"
        )

    def test_get_data_from_markdown_should_return_correctly_data_without_article(
        self,
    ):
        data = get_data_from_markdown(self.path, with_article=False)
        assert data["title"] == "Title sample"
        assert data["author"] == "Author sample"
        assert data["date"] == "01/01/2024"
        assert data["file_path"] == self.path.split("/")[-1]
        assert "article" not in data

    def tearDown(self):
        os.remove(self.path)


if __name__ == "__main__":
    unittest.main()
