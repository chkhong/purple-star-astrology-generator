from loguru import logger
from map import code_star_map, star_intensity_map, year_effect_map
import traceback

class Star:
  def __init__(self, code:str, intensity:int=0, effect:int=0):
    self.code = code
    self.intensity = intensity
    self.effect = effect

class StarMapper:
  def __init__(self):
    # 代码与星星
    self.code_star_map = code_star_map
    # 星曜亮度
    self.star_intensity_map = star_intensity_map
    # 生年四化
    self.year_effect_map = year_effect_map

  # 星曜亮度
  def intensity_of(self, code:str, dz:str) -> str:
    ''' Returns intensity of the star in specific location
  
      Args:
        code: the code of star
        dz: dizhi of the location
      Returns:
        intensity: str
    '''
    logger.info('-'*100)
    logger.info('intensity_of() running...')
    intensity = ''
    try:
      i = int(dz[2:])
      temp = self.star_intensity_map[code][i]
      intensity = 'i' + str(temp)
      logger.debug(f"{self.code_star_map[code]}'s intensity at {self.code_star_map[dz]}: {self.code_star_map[intensity]}")
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return intensity
  
  # 星曜四化 
  def effect_of(self, code:str, year:int) -> str:
    ''' Return the star effect 
  
      Args:
        code: the code of star
        year: birth year
      Returns:
        effect: str
    '''
    logger.info('-'*100)
    logger.info('effect_of() running...')
    effect = ''
    try:
      remain = (year - 3) % 10
      if code in self.year_effect_map[remain]:
        effect = 'e' + str(self.year_effect_map[remain].index(code))
        logger.debug(f"{self.code_star_map[code]}'s effect in {year} is {self.code_star_map[effect]}")
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return effect


if __name__ == '__main__':
  sm = StarMapper()
  sm.intensity_of('m8', 'dz3')
  sm.effect_of('m3', 1999)