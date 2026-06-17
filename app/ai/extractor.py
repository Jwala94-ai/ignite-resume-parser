import re


class AIExtractor:

    def extract(self, text, sections):

        email = None
        phone = None
        linkedin = None
        github = None
        full_name = None

        # Email
        email_match = re.search(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            text
        )

        if email_match:
            email = email_match.group(0)

        # Phone
        phone_match = re.search(
            r'(\+?\d[\d\-\s]{8,15})',
            text
        )

        if phone_match:
            phone = phone_match.group(0).strip()

        # LinkedIn
        linkedin_match = re.search(
            r'linkedin\.com/in/[^\s]+',
            text,
            re.IGNORECASE
        )

        if linkedin_match:
            linkedin = linkedin_match.group(0)

        # GitHub
        github_match = re.search(
            r'github\.com/[^\s]+',
            text,
            re.IGNORECASE
        )

        if github_match:
            github = github_match.group(0)

        # Full Name (first non-empty line)
        lines = [
            line.strip()
            for line in text.split("\n")
            if line.strip()
        ]

        if lines:
            full_name = lines[0]

        # Skills
        skills = []

        if "skills" in sections:

            skill_text = "\n".join(
                sections["skills"]
            )

            skills = [
                item.strip()
                for item in re.split(
                    r'[,•\n]',
                    skill_text
                )
                if item.strip()
            ]

            cleaned = []

            for skill in skills:

                skill = (
                    skill.replace(
                        "Programming Languages:",
                        ""
                    )
                    .replace(
                        "Web Technologies:",
                        ""
                    )
                    .replace(
                        "Tools & Platforms:",
                        ""
                    )
                    .replace(
                        "Data & Analytics:",
                        ""
                    )
                    .strip()
                )

                if skill:
                    cleaned.append(skill)

            skills = cleaned

        # Education
        education = []

        if "education" in sections:
            education = sections["education"]

        # Projects
        projects = []

        if "projects" in sections:
            projects = sections["projects"]

        # Certifications
        certifications = []

        if "certifications" in sections:
            certifications = sections["certifications"]

        # Summary
        summary = None

        if "summary" in sections:
            summary = "\n".join(
                sections["summary"]
            )

        return {
            "personal_info": {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "linkedin": linkedin,
                "github": github,
                "portfolio": None,
                "location": None
            },
            "summary": summary,
            "experience": sections.get(
                "experience",
                []
            ),
            "education": education,
            "skills": {
                "technical": skills,
                "soft": [],
                "tools": [],
                "languages": []
            },
            "certifications": certifications,
            "projects": projects,
            "insights": {
                "total_experience_years": None,
                "career_level": "Student",
                "top_skills": skills[:10],
                "domain": "Computer Science"
            },
            "flags": []
        }