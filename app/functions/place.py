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
    life_location = 3 + month - dz_int

    # 排12宫
    circular_loop = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(1,13):
      # loc: location of palace
      loc = circular_loop[life_location-i]
      payload[loc]['宫位'] = code_star_map['p' + str(i)]
    
    # 找身宫
    if dz_int % 6 == 1:
      payload['身宫'] = code_star_map['p1']
    elif dz_int % 6 == 2:
      payload['身宫'] = code_star_map['p11']
    elif dz_int % 6 == 3:
      payload['身宫'] = code_star_map['p9']
    elif dz_int % 6 == 4:
      payload['身宫'] = code_star_map['p7']
    elif dz_int % 6 == 5:
      payload['身宫'] = code_star_map['p5']
    elif dz_int % 6 == 0:
      payload['身宫'] = code_star_map['p3']

    return payload

  def setPalaceDZ(self, payload:dict, tg:str) -> dict:
    ''' Function description
  
      Args:
        tg: tian gan of birth year
      Returns:
        payload: dict
    '''
    logger.info('='*100)
    logger.info('setPalaceDZ() running...')
    
    tg_int_reduced = int(tg[2:])
    if tg_int_reduced > 5:
      tg_int_reduced -= 5
    loop = [3,4,5,6,7,8,9,10,11,12,1,2]
    
    for i in range(0,12):
      payload[loop[i]]['地支'] = code_star_map[tg_palace_dz_map[tg_int_reduced][i]]

    return payload


if __name__ == '__main__':
  pm = PlaceMapper()
  r = {
      '身宫': '', '五行局': '',
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
  test = pm.setAllPlace(r, 11, 'dz11')
  test2 = pm.setPalaceDZ(test, 'tg6')
  logger.debug(test2)