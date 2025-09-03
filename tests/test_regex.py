import re
from typing import List, Tuple, Dict


class RegexTester:
    def __init__(self):
        self.test_text = """Jooble — is a Ukrainian IT company that operates in 71 countries. The company's product is a job search website with more than 90M monthly users.
According to SimilarWeb, Jooble is the second most visited employment website in the world, and it is among 500 top visited websites globally. Jooble is a remote-first company. We believe that talented people can create cool projects no matter where they are. The company's headquarters are located in Kyiv. Offices in Kyiv, Uzhgorod and Lutsk are available for employees to visit at any time they want. Currently, 590 professionals in our team communicate in 25 different languages.
Here are some exciting resources where you can find out more about our company:
1.	Jooble's history https://ain.ua/ — https://ain.ua/2019/03/25/fotoreportazh-jooble/
2.	Our workspace — an episode of "DOU-revisor" (inspector) about the Jooble office in Kyiv — https://dou.ua/lenta/articles/dou-revisor-jooble-2/. About career path possibilities in our company https://hiring.jooble.org/
In case you have additional questions — there is a chatbot on this website https://hiring.jooble.org/. We also have a Telegram bot for those who prefer to use their phones — @jooblecandidate_bot. And also a bot for Viber — @jooblecandidate_bot. Corporate email of our Talent manager — yulyia.lysnianskaia@jooble.com."""
        
        self.patterns = {
            'url': r'https?://[^\s<>"{}|\\^`\[\]]+',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'bot': r'@[A-Za-z0-9_]+',
            'parentheses': r'\([^)]+\)'
        }
    
    def test_pattern(self, pattern_name: str) -> List[str]:
        pattern = self.patterns[pattern_name]
        return re.findall(pattern, self.test_text)
    
    def run_all_tests(self) -> Dict[str, List[str]]:
        results = {}
        for pattern_name in self.patterns:
            results[pattern_name] = self.test_pattern(pattern_name)
        return results
    
    def print_results(self):
        print("=== REGEX TESTING RESULTS ===\n")
        
        for pattern_name, matches in self.run_all_tests().items():
            print(f"{pattern_name.upper()}:")
            for i, match in enumerate(matches, 1):
                print(f"  {i}. {match}")
            print(f"Total: {len(matches)}\n")
        
        print("=== PATTERNS ===")
        for pattern_name, pattern in self.patterns.items():
            print(f"{pattern_name}: {pattern}")


def main():
    tester = RegexTester()
    tester.print_results()


if __name__ == "__main__":
    main()

