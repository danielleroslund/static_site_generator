import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, text_to_textnodes

def test_split_code():
    node = TextNode("This is `code` text", TextType.TEXT)
    result = split_nodes_delimiter([node], "`", TextType.CODE)

    assert len(result) == 3 
    assert result[0].text == "This is "
    assert result[0].text_type == TextType.TEXT
    assert result[1].text == "code"
    assert result[1].text_type == TextType.CODE
    assert result[2].text == " text"
    assert result[2].text_type == TextType.TEXT

def test_split_bold():
    node = TextNode("This is **bold** text", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)

    assert len(result) == 3
    assert result[0].text == "This is "
    assert result[0].text_type == TextType.TEXT
    assert result[1].text == "bold"
    assert result[1].text_type == TextType.BOLD
    assert result[2].text == " text"
    assert result[2].text_type == TextType.TEXT

def test_invalid_markdown():
    node = TextNode("This is `broken code", TextType.TEXT)
    try:
        split_nodes_delimiter([node], "`", TextType.CODE)
        assert False
    except Exception as e:
        assert str(e) == "Invalid Markdown syntax — unmatched delimiter"

def test_extract_two_images():
    text = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    assert extract_markdown_images(text) == expected

def test_extract_no_images():
    text = "This text has no images, only text."
    expected = []
    assert extract_markdown_images(text) == expected

def test_extract_two_links():
    text = "Check [Boot.dev](https://www.boot.dev) and [YouTube](https://www.youtube.com)"
    expected = [("Boot.dev", "https://www.boot.dev"), ("YouTube", "https://www.youtube.com")]
    assert extract_markdown_links(text) == expected

def test_extract_no_links():
    text = "This text ha no links, only a immage ![image](https://example.com/image.png)"
    expected = []
    assert extract_markdown_links(text) == expected

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_images_no_images(self):
    node = TextNode("This is text without images.", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual([node], new_nodes)

def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://second.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://second.com"),
        ],
        new_nodes,
    )

def test_split_links_no_links(self):
    node = TextNode("Just plain text, no links here.", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    self.assertListEqual([node], new_nodes)

def test_text_to_textnodes(self):
    input_text = "This is **text** with an _italic_ word and `code blodk` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    expected_nodes = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
    ]

    result_nodes = text_to_textnodes(input_text)

    self.assertEqual(len(result_nodes), len(expected_nodes))

    for result, expected in zip(result_nodes, expected_nodes):
        self.assertEqual(result.text, expected.text)
        self.assertEqual(result.text_type, expected.text_type)
        self.assertEqual(result.url, expected.url)

def test_markdown_to_blocks(self):
    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    blocks = markdown_to_blocks(md)
    self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )