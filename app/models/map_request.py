from pydantic import BaseModel, Field

class MapRequest(BaseModel):
    width:  int = Field(..., gt=0, strict=True)
    height: int = Field(..., gt=0, strict=True)
    biome:  str
