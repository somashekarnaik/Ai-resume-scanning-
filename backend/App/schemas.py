from typing import Annotated, Literal

from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):

    name: str

    email: str

    password: str


class LoginRequest(BaseModel):

    email: str

    password: str


class JobMatchRequest(BaseModel):

    skills: str


class SampleResumeRequest(BaseModel):

    role_title: str

    resume_skills: list[str]


class CareerAssistantMessage(BaseModel):

    role: Literal["user", "assistant"]

    content: str = Field(min_length=1, max_length=5000)


class CareerAssistantRequest(BaseModel):

    question: str = Field(min_length=1, max_length=1000)

    resume_skills: list[Annotated[str, Field(min_length=1, max_length=80)]] = Field(
        default_factory=list,
        max_length=40,
    )

    expected_role: str | None = Field(default=None, max_length=100)

    expected_role_score: float | None = Field(default=None, ge=0, le=100)

    recommended_role: str | None = Field(default=None, max_length=100)

    format_issues: list[Annotated[str, Field(min_length=1, max_length=300)]] = Field(
        default_factory=list,
        max_length=20,
    )

    history: list[CareerAssistantMessage] = Field(default_factory=list, max_length=10)