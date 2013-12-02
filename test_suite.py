import unittest
from profanity import profanity


class ProfanityTest(unittest.TestCase):
    def test_contains_profanity(self):
        profane = profanity.contains_profanity('dude, SHIT!')
        self.failUnless(profane)

    def test_leaves_paragraphs_untouched(self):
        innocent_text = """If you prick us do we not bleed?
                        If you tickle us do we not laugh?
                        If you poison us do we not die?
                        And if you wrong us shall we not revenge?"""
        censored_text = profanity.censor(innocent_text)
        self.failUnless(innocent_text == censored_text)

    def test_censorship(self):
        bad_text = "Dude, I hate shit. Fuck bullshit."
        censored_text = profanity.censor(bad_text)
        # make sure it finds both instances
        self.failIf("shit" in censored_text)
        # make sure it's case sensitive
        self.failIf("fuck" in censored_text)
        # make sure some of the original text is still there
        self.failUnless("Dude" in censored_text)

    def test_custom_wordlist(self):
        custom_badwords = ['happy', 'jolly', 'merry']
        profanity.load_words(custom_badwords)
        # make sure it doesn't find real profanity anymore
        self.failIf(profanity.contains_profanity("Fuck you!"))
        # make sure it finds profanity in a sentence containing custom_badwords
        self.failUnless(profanity.contains_profanity("Have a merry day! :)"))


if __name__ == "__main__":
    unittest.main()
