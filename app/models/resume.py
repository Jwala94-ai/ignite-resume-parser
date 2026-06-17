"""Resume data model"""
from pydantic import BaseModel
from typing import List, Optional

class PersonalInfo(BaseModel):
    full_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    portfolio: Optional[str]
    location: Optional[str]

class Experience(BaseModel):
    title: Optional[str]
    company: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    duration: Optional[str]
    location: Optional[str]
    responsibilities: List[str]
    skills: List[str]

class Education(BaseModel):
    degree: Optional[str]
    field_of_study: Optional[str]
    institution: Optional[str]
    graduation_year: Optional[str]
    gpa: Optional[str]

class Resume(BaseModel):
    personal_info: PersonalInfo
    summary: Optional[str]
    experience: List[Experience]
    education: List[Education]
    skills: dict
    certifications: list
    projects: list
    insights: dict
    flags: List[str]