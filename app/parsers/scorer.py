"""Scoring and ranking for resume matches"""
class ResumeScorer:
    
    def generate(self, data):

        years = 0

        for exp in data["experience"]:
            years += exp.get("years",0)

        return {
            "total_experience_years": years,
            "career_level": self.level(years),
            "top_skills": [],
            "domain": None
        }

    def level(self, years):

        if years < 1:
            return "Fresher"

        if years < 3:
            return "Junior"

        if years < 7:
            return "Mid-Level"

        if years < 12:
            return "Senior"

        return "Lead"