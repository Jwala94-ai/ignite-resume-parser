import re


class JDMatcher:

    def match(self, resume_data, job_description):

        resume_skills = set(
            skill.lower().strip()
            for skill in resume_data["skills"]["technical"]
        )

        jd_words = set(
            re.findall(
                r'\b[a-zA-Z]+\b',
                job_description.lower()
            )
        )

        matched = list(
            resume_skills.intersection(
                jd_words
            )
        )

        missing = list(
            jd_words.difference(
                resume_skills
            )
        )

        if len(jd_words) == 0:
            percentage = 0

        else:
            percentage = round(
                (
                    len(matched)
                    /
                    len(jd_words)
                ) * 100,
                2
            )

        recommendations = []

        for skill in missing[:5]:

            recommendations.append(
                f"Consider adding experience with {skill}"
            )

        if percentage < 40:

            recommendations.append(
                "Resume has low keyword alignment with the job description"
            )

        elif percentage < 70:

            recommendations.append(
                "Resume has moderate alignment; consider adding more relevant keywords"
            )

        else:

            recommendations.append(
                "Resume is well aligned with the job description"
            )

        return {
            "match_percentage": percentage,
            "matched_keywords": matched,
            "missing_keywords": missing[:20],
            "recommendations": recommendations
        }