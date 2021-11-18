from loguru import logger
from map import code_star_map, tg_palace_dz_map
import traceback
from math import ceil

class PlaceMapper:
  def __init__(self):
    # 代码与星星
    self.code_star_map = code_star_map
    self.tg_palace_dz_map = tg_palace_dz_map

  # 安13宫
  def setAllPlace(self, payload:dict, month:int, dz:str) -> dict:
    ''' Return 13 宫所在位置 
  
      Args:
        month: birth month
        dz: dizhi of the location
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setAllPlace() running...')

    dz_int = int(dz[2:])
    # 命宫位置
    life_location = (1 + month - (dz_int)) % 12

    # 排12宫
    for i in range(0,12):
      # loc: location of palace
      loc = (life_location-i)%12
      payload[loc]['宫位'] = code_star_map['p' + str(i)]
    
    # 找身宫
    if dz_int % 6 == 1:
      payload['身宫'] = code_star_map['p10']
    elif dz_int % 6 == 2:
      payload['身宫'] = code_star_map['p8']
    elif dz_int % 6 == 3:
      payload['身宫'] = code_star_map['p6']
    elif dz_int % 6 == 4:
      payload['身宫'] = code_star_map['p4']
    elif dz_int % 6 == 5:
      payload['身宫'] = code_star_map['p2']
    elif dz_int % 6 == 0:
      payload['身宫'] = code_star_map['p0']

    return payload

  def setPalaceDZ(self, payload:dict, tg:str) -> dict:
    ''' Set 12 宫地支
  
      Args:
        tg: tian gan of birth year
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setPalaceDZ() running...')
    
    tg_int_reduced = int(tg[2:]) % 5
    start = tg_palace_dz_map[tg_int_reduced]
    logger.warning(start)

    for i in range(0,12):
      payload[(i+2)%12]['地支'] = code_star_map['tg'+str((start+i)%10)]

    return payload


if __name__ == '__main__':
  pm = PlaceMapper()
  r = {
      '身宫': '', '五行局': '',
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
  test = pm.setAllPlace(r, 11, 'dz10')
  logger.debug(test)
  test2 = pm.setPalaceDZ(test, 'tg5')
  logger.debug(test2)