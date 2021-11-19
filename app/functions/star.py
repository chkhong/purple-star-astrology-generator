from loguru import logger
from map import code_star_map, star_intensity_map, year_effect_map, five_elements_dz_map, five_elements_map, five_elements_map_inv, ziwei_tianfu_map, ziwei_star_group_map, tianfu_star_group_map, lucun_tg_map, kuiyue_tg_map, huoxing_nz_map, lingxing_nz_map, tianma_nz_map
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
      if temp == 9:
        return intensity
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

  def setStarsWithMonth(self, payload:dict, month:int, tg:str) -> dict:
    ''' set stars that are determined by month
  
      Args:
        month: birth month
        tg: tian gan of birth year
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setStarsWithMonth() running...')

    # 安左辅
    star_code = 'g2'
    star = code_star_map[star_code]
    payload[(3+month)%12]['吉星'] += [star, self.intensity_of(star_code, 'dz'+str((3+month)%12)), self.effect_of(star_code,tg)]
    # 安右弼
    star_code = 'g3'
    star = code_star_map[star_code]
    payload[(11-month)%12]['吉星'] += [star, self.intensity_of(star_code, 'dz'+str((11-month)%12)), self.effect_of(star_code,tg)]

    return payload

  def setStarsWithHour(self, payload:dict, tg:str, dz:str, nz:str) -> dict:
    ''' set stars that are determined by hour
  
      Args:
        tg: tian gan of birth year
        dz: di zhi of birth hour
        nz: nian zhi of birth year
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setStarsWithHour() running...')

    dz_int = int(dz[2:])
    nz_int = int(nz[2:])

    # 安文昌
    star_code = 'g0'
    star = code_star_map[star_code]
    payload[(10-dz_int)%12]['吉星'] += [star, self.intensity_of(star_code, 'dz'+str((10-dz_int)%12)), self.effect_of(star_code,tg)]
    # 安文曲
    star_code = 'g1'
    star = code_star_map[star_code]
    payload[(4+dz_int)%12]['吉星'] += [star, self.intensity_of(star_code, 'dz'+str((4+dz_int)%12)), self.effect_of(star_code,tg)]
    # 安地空
    star_code = 'b4'
    star = code_star_map[star_code]
    payload[(11-dz_int)%12]['煞星'] += [star, self.intensity_of(star_code, 'dz'+str((11-dz_int)%12)), '']
    # 安地劫
    star_code = 'b5'
    star = code_star_map[star_code]
    payload[(11+dz_int)%12]['煞星'] += [star, self.intensity_of(star_code, 'dz'+str((11+dz_int)%12)), '']
    # 安火星
    star_code = 'b2'
    star = code_star_map[star_code]
    loc = huoxing_nz_map[nz_int]
    payload[(loc+dz_int)%12]['煞星'] += [star, self.intensity_of(star_code,'dz'+str((loc+dz_int)%12)), '']
    # 安铃星
    star_code = 'b3'
    star = code_star_map[star_code]
    loc = lingxing_nz_map[nz_int]
    payload[(loc+dz_int)%12]['煞星'] += [star, self.intensity_of(star_code,'dz'+str((loc+dz_int)%12)), '']

    logger.debug(payload)
    return payload

  def setStarsWithYear(self, payload:dict, tg:str) -> dict:
    ''' set stars that are determined by year
  
      Args:
        tg: tian gan of birth year
      Returns:
        payload: dict
        
    '''
    logger.info('='*100)
    logger.info('setStarsWithYear() running...')

    tg_int = int(tg[2:]) + 1

    # 安禄存擎羊陀螺
    lucun_star_code = 'g6'
    qingyang_star_code = 'b0'
    tuoluo_star_code = 'b1'
    lucun_loc = lucun_tg_map[tg_int]
    payload[lucun_loc]['吉星'] += [code_star_map[lucun_star_code], self.intensity_of(lucun_star_code,'dz'+str(lucun_loc)), '']
    payload[(lucun_loc+1)%12]['煞星'] += [code_star_map[qingyang_star_code], self.intensity_of(qingyang_star_code,'dz'+str((lucun_loc+1)%12)), '']
    payload[(lucun_loc-1)%12]['煞星'] += [code_star_map[tuoluo_star_code], self.intensity_of(tuoluo_star_code,'dz'+str((lucun_loc-1)%12)), '']

    # 安天魁天钺
    tiankui_star_code = 'g4'
    tianyue_star_code = 'g5'
    tiankui_star_loc, tianyue_star_loc = kuiyue_tg_map[tg_int]
    payload[tiankui_star_loc]['吉星'] += [code_star_map[tiankui_star_code], self.intensity_of(tiankui_star_code,'dz'+str(tiankui_star_loc)), '']
    payload[tianyue_star_loc]['吉星'] += [code_star_map[tianyue_star_code], self.intensity_of(tianyue_star_code,'dz'+str(tianyue_star_loc)), '']

    return payload
  
  def setStarsWithNZ(self, payload:dict, nz:str) -> dict:
    ''' set stars that are determined by nian zhi
  
      Args:
        nz: nian zhi of birth year
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setStarsWithNZ() running...')

    nz_int = int(nz[2:])

    # 安天马
    star_code = 'g7'
    star = code_star_map[star_code]
    loc = tianma_nz_map[nz_int]
    payload[loc]['吉星'] += [star, '', '']

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
  for i in range(0,12):
    r[i]['地支'] = code_star_map['dz'+str(i)]
    r[i]['主星'] = []
    r[i]['吉星'] = []
    r[i]['煞星'] = []
    r[i]['杂曜'] = []
  # sm.intensity_of('m8', 'dz3')
  # sm.effect_of('m3', 'tg5')
  # sm.setFiveElements({},'tg2','dz2')
  # sm.setMainStars(r,'tg5',25,'火六局')
  # sm.setMainStars({},25,'木三局')
  # sm.setMainStars({},28,'水二局')
  # sm.setStarsWithMonth(r, 11,'tg5')
  # sm.setStarsWithHour(r,'tg5', 'dz10', 'dz3')
  sm.setStarsWithNZ(r,'dz3')
  # sm.setStarsWithYear(r,'tg5')