from loguru import logger
import traceback
from .map import code_star_map
from .calendar_converter import CalendarConverter
from .place import PlaceMapper
from .star import StarMapper
import json

class Arranger:
  def __init__(self):
    self.cc = CalendarConverter()
    self.pm = PlaceMapper()
    self.st = StarMapper()

  def __del__(self):
    pass

  def _setBoilerplate(self) -> dict:
    r = {
      "身宫": "", "五行局": "",
      0:{},
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
    }
    for i in range(0,12):
      r[i]['地支'] = code_star_map['dz'+str(i)]
      r[i]['主星'] = []
      r[i]['吉星'] = []
      r[i]['煞星'] = []
      r[i]['杂曜'] = []
      
    return r

  def arrange(self, year:int, month:int, day:int, hour:int=0, minute:int=0):
    ''' Function description
  
      Args:
        
      Returns:
        
    '''
    
    logger.info('='*100)
    logger.info('arrange() running...')

    r = self._setBoilerplate()
    try:
      # 换算出生日期时间 bd -> birth_details
      bd = self.cc.western_to_chinese(year, month, day, hour, minute)
      logger.debug(bd)

      # 安命宫
      r = self.pm.setAllPlace(r, bd['month'], bd['dz'])
      # 安十二宫干
      r = self.pm.setPalaceDZ(r, bd['tg'])
      # 安五行局
      r = self.st.setFiveElements(r)
      # 安十四主星
      r = self.st.setMainStars(r, bd['tg'], bd['day'])
      # 安生月系诸星
      r = self.st.setStarsWithMonth(r, bd['month'], bd['tg'])
      # 安时系诸星
      r = self.st.setStarsWithHour(r, bd['tg'], bd['dz'], bd['nz'])
      # 安生年支系诸星
      r = self.st.setStarsWithNZ(r, bd['nz'])
      # 安生年干系诸星
      r = self.st.setStarsWithYear(r,bd['tg'])

      logger.debug(r)


      with open('output.json', 'w') as output:
        json.dump(r,output,indent=2,ensure_ascii=False)

    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return r

if __name__ == '__main__':
  a = Arranger()
  a.arrange(2000, 1, 1, 19, 37)