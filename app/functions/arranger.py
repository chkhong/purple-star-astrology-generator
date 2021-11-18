from loguru import logger
import traceback
from .calendar_converter import CalendarConverter
from .place import PlaceMapper

class Arranger:
  def __init__(self):
    self.cc = CalendarConverter()
    self.pm = PlaceMapper()

  def __del__(self):
    pass

  def arrange(self, year:int, month:int, day:int, hour:int=0, minute:int=0):
    ''' Function description
  
      Args:
        
      Returns:
        
    '''
    r = {
      "身宫": "", "五行局": "",
      1:{},
      2:{},
      3:{},
      4:{},
      5:{},
      6:{},
      7:{},
      8:{},
      9:{},
      10:{},
      11:{},
      12:{},
    }
    logger.info('='*100)
    logger.info('arrange() running...')

    try:
      # 换算出生日期时间
      birth_details = self.cc.western_to_chinese(year, month, day, hour, minute)
      logger.debug(birth_details)

      # 安命宫
      r = self.pm.setAllPlace(r, birth_details['month'], birth_details['dz'])

      logger.debug(r)
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return "ok"

if __name__ == '__main__':
  a = Arranger()
  a.arrange(2000, 1, 1, 19, 37)