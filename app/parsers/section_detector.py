"""Section detection in resumes"""

class SectionDetector:

    HEADERS = {
        "experience": [
            "experience",
            "experience & simulations",
            "employment",
            "work history",
            "professional experience"
        ],

        "education": [
            "education",
            "academics"
        ],

        "skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "projects": [
            "projects"
        ],

        "certifications": [
            "certifications",
            "licenses"
        ],

        "summary": [
            "professional summary",
            "summary",
            "profile"
        ],

        "achievements": [
            "achievements",
            "achievements & activities"
        ],

        "interests": [
            "interests"
        ]
    }

    def detect(self, text):

        sections = {}

        lines = text.split("\n")

        current = "unknown"

        for line in lines:

            normalized = (
                line.lower()
                .strip()
                .replace(":", "")
            )

            found_header = False

            for key, values in self.HEADERS.items():

                if normalized in values:

                    current = key

                    sections[current] = []

                    found_header = True

                    break

            if found_header:
                continue

            sections.setdefault(
                current,
                []
            ).append(line)

        return sections