class ATSScorer:
    
    def score(self, result):

        score = 0

        strengths = []
        weaknesses = []

        personal = result["personal_info"]

        # Contact Information (15)
        if personal["email"]:
            score += 5
        else:
            weaknesses.append("Missing email")

        if personal["phone"]:
            score += 5
        else:
            weaknesses.append("Missing phone")

        if personal["linkedin"]:
            score += 3
        else:
            weaknesses.append("Missing LinkedIn profile")

        if personal["github"]:
            score += 2

        # Summary (10)
        if result["summary"]:
            score += 10
            strengths.append("Professional summary present")
        else:
            weaknesses.append("Missing summary")

        # Education (10)
        if result["education"]:
            score += 10
        else:
            weaknesses.append("Education section missing")

        # Experience (20)
        experience_count = len(result["experience"])

        if experience_count >= 10:
            score += 20

        elif experience_count >= 5:
            score += 15

        elif experience_count > 0:
            score += 10

        else:
            weaknesses.append("No experience found")

        # Projects (20)
        project_count = len(result["projects"])

        if project_count >= 10:
            score += 20

        elif project_count >= 5:
            score += 15

        elif project_count > 0:
            score += 10

        else:
            weaknesses.append("No projects found")

        # Skills (20)
        skill_count = len(
            result["skills"]["technical"]
        )

        if skill_count >= 15:
            score += 20

        elif skill_count >= 10:
            score += 15

        elif skill_count >= 5:
            score += 10

        else:
            weaknesses.append(
                "Few technical skills listed"
            )

        # Certifications (5)
        cert_count = len(
            result["certifications"]
        )

        if cert_count >= 5:
            score += 5

        elif cert_count > 0:
            score += 3

        # Bonus (optional)
        if personal["linkedin"] and personal["github"]:
            score += 5

        score = min(score, 100)

        if score >= 90:
            strengths.append(
                "Excellent ATS readiness"
            )

        elif score >= 75:
            strengths.append(
                "Strong ATS profile"
            )

        elif score >= 60:
            strengths.append(
                "Average ATS profile"
            )

        else:
            weaknesses.append(
                "Resume needs significant improvement"
            )

        return {
            "ats_score": score,
            "strengths": strengths,
            "weaknesses": weaknesses
        }