from pathlib import Path
import unittest


FOOTER = Path(__file__).resolve().parents[1] / "wpcode-footer.html"


class WpcodeFooterXssContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = FOOTER.read_text(encoding="utf-8")

    def test_response_markup_is_sanitized_before_live_dom_insertion(self):
        self.assertIn("template.innerHTML = String(unsafeHtml);", self.source)
        self.assertIn("msg.replaceChildren(sanitizeBotHtml(rawText));", self.source)
        self.assertNotIn("msg.innerHTML = rawText", self.source)

    def test_sanitizer_uses_element_and_attribute_allowlists(self):
        self.assertIn("BOT_ALLOWED_HTML_TAGS.has(tagName)", self.source)
        self.assertIn("BOT_DROP_HTML_TAGS.has(tagName)", self.source)
        self.assertIn("'script'", self.source)
        self.assertIn("'iframe'", self.source)
        self.assertIn("'svg'", self.source)
        self.assertIn("name.startsWith('on')", self.source)
        self.assertIn("name === 'srcdoc'", self.source)

    def test_untrusted_navigation_urls_are_protocol_checked(self):
        self.assertIn("url.protocol === 'https:'", self.source)
        self.assertIn("url.protocol === 'http:' && url.origin === window.location.origin", self.source)
        self.assertIn("url.protocol === 'mailto:'", self.source)


if __name__ == "__main__":
    unittest.main()
