from loguru import logger
import traceback
from lunardate import LunarDate as ld

class CalendarConverter:
  def __init__(self):
    pass

  def __del__(self):
    pass

  def western_to_chinese(self, year:int, month:int, day:int, hour:int=0) -> dict:
    r = {}
    try:
      # get year, month, day
      temp = ld.fromSolarDate(year, month, day)
      r['year'] = temp.year
      r['month'] = temp.month
      r['day'] = temp.day
      
      r['hour'] = hour
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return r

if __name__ == '__main__':
  cc = CalendarConverter()
  test = cc.western_to_chinese(1999,9,27)
  logger.debug(test)