from pydantic import BaseModel, Field

class Request(BaseModel):
  year: int = Field(..., title='Birth year')
  month: int = Field(..., title='Birth month')
  day: int = Field(..., title='Birth day')
  hour: int = Field(..., title='Birth hour')
  minute: int = Field(..., title='Birth minute')

  class Example:
    examples = {
      'example1': {
        'summary': 'example 1',
        'value': {
          "year": 2000,
          "month": 1,
          "day": 1,
          "hour": 19,
          "minute": 37
        }
      }
    }