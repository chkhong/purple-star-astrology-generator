from loguru import logger
from map import code_star_map, star_intensity_map, year_effect_map, five_elements_dz_map, five_elements_map, five_elements_map_inv, ziwei_tianfu_map, ziwei_star_group_map, tianfu_star_group_map
import traceback
from math import floor

class StarMapper:

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
      temp = star_intensity_map[code][i]
      intensity = code_star_map['i'+str(temp)]
      logger.debug(f"{code_star_map[code]}'s intensity at {code_star_map[dz]}: {intensity}")
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return intensity
  
  # 星曜四化 
  def effect_of(self, code:str, tg:str) -> str:
    ''' Return the star effect 
  
      Args:
        code: the code of star
        tg: tian gan of birth year
      Returns:
        effect: str
    '''
    logger.info('-'*100)
    logger.info('effect_of() running...')
    effect = ''
    try:
      tg_int = int(tg[2:]) + 1
      if code in year_effect_map[tg_int]:
        effect = code_star_map['e'+str(year_effect_map[tg_int].index(code))]
        logger.debug(f"{code_star_map[code]}'s effect in {code_star_map[tg]} is {effect}")
    except Exception as e:
      logger.error(e)
      logger.error(traceback.format_exc())
    finally:
      return effect

  def setFiveElements(self, payload:dict, tg:str, dz:str) -> dict:
    ''' Set 五行局
  
      Args:
        tg: tian gan of birth year
        dz: dizhi of the birth hour
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setFiveElements() running...')
  
    # 命宫天干
    tg_int = int(tg[2:])
    tg_int_temp = floor((tg_int + 2)/2)

    # 命宫地支
    dz_int = int(dz[2:])
    dz_int_temp = five_elements_dz_map[dz_int]

    five_elems_index = (tg_int_temp + dz_int_temp) % 5

    payload['五行局'] = five_elements_map[five_elems_index]

    return payload

  def setMainStars(self, payload:dict, tg:str, day:int, fiveElements:str) -> dict:
    ''' Set 十四主星 by finding 紫微星
  
      Args:
        tg: tian gan of the birth year
        day: day of birth year
        fiveElements:
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setMainStars() running...')

    dividend = day
    divisor = five_elements_map_inv[fiveElements]
    remainder = dividend % divisor
    quotient = (dividend // divisor + 1) % 12
    
    if remainder != 0:
      quotient += 1
      to_add = divisor - remainder

      if to_add % 2 == 0:
        quotient = (quotient + to_add) % 12
      else:
        quotient = (quotient - to_add)

    ziwei_loc = quotient
    tianfu_loc = ziwei_tianfu_map[ziwei_loc]

    logger.debug(f'{code_star_map["m0"]} location: {code_star_map["dz"+str(ziwei_loc)]}')
    logger.debug(f'{code_star_map["m6"]} location: {code_star_map["dz"+str(tianfu_loc)]}')

    for offset in range(0,12):
      # 紫微星群
      star_code = ziwei_star_group_map[offset]
      if star_code != '':
        star = code_star_map[star_code]
        to_add = [star,self.intensity_of(star_code, 'dz'+str((ziwei_loc-offset)%12)),self.effect_of(star_code,tg)]
        payload[(ziwei_loc-offset)%12]['主星'].append(to_add)

      # 天府星群
      star_code = tianfu_star_group_map[offset]
      if star_code != '':
        star = code_star_map[star_code]
        to_add = [star,self.intensity_of(star_code, 'dz'+str((tianfu_loc+offset)%12)),self.effect_of(star_code,tg)]
        payload[(tianfu_loc+offset)%12]['主星'].append(to_add)


    logger.debug(payload)
    return payload


if __name__ == '__main__':
  sm = StarMapper()
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
  # sm.intensity_of('m8', 'dz3')
  # sm.effect_of('m3', 'tg5')
  # sm.setFiveElements({},'tg2','dz2')
  sm.setMainStars(r,'tg5',25,'火六局')
  # sm.setMainStars({},25,'木三局')
  # sm.setMainStars({},28,'水二局')