from loguru import logger
import traceback
from lunardate import LunarDate as ld

class CalendarConverter:

  def western_to_chinese(self, year:int, month:int, day:int, hour:int=0, minute:int=0) -> dict:
    r = {}
    try:
      # get year, month, day
      temp = ld.fromSolarDate(year, month, day)
      r['year'] = temp.year
      r['month'] = temp.month
      r['day'] = temp.day
      
      if hour >= 23 or hour < 1:
        r['hour'] = 'dz1'
      elif hour >= 1 and hour < 3:
        r['hour'] = 'dz2'
      elif hour >= 3 and hour < 5:
        r['hour'] = 'dz3'
      elif hour >= 5 and hour < 7:
        r['hour'] = 'dz4'
      elif hour >= 7 and hour < 9:
        r['hour'] = 'dz5'
      elif hour >= 9 and hour < 11:
        r['hour'] = 'dz6'
      elif hour >= 11 and hour < 13:
        r['hour'] = 'dz7'
      elif hour >= 13 and hour < 15:
        r['hour'] = 'dz8'
      elif hour >= 15 and hour < 17:
        r['hour'] = 'dz9'
      elif hour >= 17 and hour < 19:
        r['hour'] = 'dz10'
      elif hour >= 19 and hour < 21:
        r['hour'] = 'dz11'
      elif hour >= 21 and hour < 23:
        r['hour'] = 'dz12'

      r['minute'] = minute
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return r

if __name__ == '__main__':
  cc = CalendarConverter()
  test = cc.western_to_chinese(2021, 12, 1, 17)
  logger.debug(test)