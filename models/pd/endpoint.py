from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel, constr, validator


class EndpointPD(BaseModel):
    project_id: Optional[int]
    mode: Optional[str]
    user: str
    display_name: Optional[str]
    endpoint: str
    method: constr(to_upper=True)
    date: datetime
    view_args: Optional[dict]
    query_params: Optional[dict]
    json_: Optional[dict]
    files: Optional[dict]
    run_time: float
    status_code: int
    query_params: Optional[dict]
    extra_data: Optional[dict]

    class Config:
        orm_mode = True
        fields = {
            'json_': 'json',
        }

    @validator('display_name', always=True)
    def set_display_name(cls, value: Optional[str], values: dict):
        if not value:
            return values['user']
        return value
