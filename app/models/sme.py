from pydantic import BaseModel


class SMERequest(BaseModel):
    company_name: str | None = None
    location: str
    industry: str
    employees: int
    locations: int
    remote_workers: int