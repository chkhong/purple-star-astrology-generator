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
      
      # 地支
      if hour >= 23 or hour < 1:
        r['dz'] = 'dz0'
      elif hour >= 1 and hour < 3:
        r['dz'] = 'dz1'
      elif hour >= 3 and hour < 5:
        r['dz'] = 'dz2'
      elif hour >= 5 and hour < 7:
        r['dz'] = 'dz3'
      elif hour >= 7 and hour < 9:
        r['dz'] = 'dz4'
      elif hour >= 9 and hour < 11:
        r['dz'] = 'dz5'
      elif hour >= 11 and hour < 13:
        r['dz'] = 'dz6'
      elif hour >= 13 and hour < 15:
        r['dz'] = 'dz7'
      elif hour >= 15 and hour < 17:
        r['dz'] = 'dz8'
      elif hour >= 17 and hour < 19:
        r['dz'] = 'dz9'
      elif hour >= 19 and hour < 21:
        r['dz'] = 'dz10'
      elif hour >= 21 and hour < 23:
        r['dz'] = 'dz11'

      # 年支
      r['nz'] = 'dz' + str((r['year']-4) % 12)

      # 天干
      temp = (r['year'] - 4) % 10
      r['tg'] = 'tg' + str(temp)

      r['minute'] = minute
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return r

if __name__ == '__main__':
  cc = CalendarConverter()
  test = cc.western_to_chinese(2000, 1, 1, 19, 33)
  logger.debug(test)