#改编自    https://github.com/FoskyTech/E-Campus-Electricity
import requests
class ECampusElectricity:    #爬虫类
    def __init__(self, config=None):
        if config and isinstance(config, dict) and config:
            self.config = config
        else:
            self.config = {
                'shiroJID': '',
                'ymId': ''
            }
    def set_config(self, config):
        if config and isinstance(config, dict) and config:
            self.config = config
    def query_area(self):
        data = self._request('queryArea', {'type': 1})
        if data.get('success'):
            return {
                'error': 0,
                'data': data['rows']
            }
        else:
            return {
                'error': 1,
                'error_description': self._errcode(data.get('statusCode', 0))
            }
    def query_building(self, area_id):
        data = self._request('queryBuilding', {'areaId': area_id})
        if data.get('success'):
            return {
                'error': 0,
                'data': data['rows']
            }
        else:
            return {
                'error': 1,
                'error_description': self._errcode(data.get('statusCode', 0))
            }
    def query_floor(self, area_id, building_code):
        data = self._request('queryFloor', {'areaId': area_id, 'buildingCode': building_code})
        if data.get('success'):
            return {
                'error': 0,
                'data': data['rows']
            }
        else:
            return {
                'error': 1,
                'error_description': self._errcode(data.get('statusCode', 0))
            }
    def query_room(self, area_id, building_code, floor_code):
        data = self._request('queryRoom', {'areaId': area_id, 'buildingCode': building_code, 'floorCode': floor_code})
        if data.get('success'):
            return {
                'error': 0,
                'data': data['rows']
            }
        else:
            return {
                'error': 1,
                'error_description': self._errcode(data.get('statusCode', 0))
            }
    def query_room_surplus(self, area_id, building_code, floor_code, room_code):
        data = self._request('queryRoomSurplus', {'areaId': area_id, 'buildingCode': building_code, 'floorCode': floor_code, 'roomCode': room_code})
        if data.get('success'):
            return {
                'error': 0,
                'data': {
                    'surplus': data['data']['amount'],
                    'roomName': data['data']['displayRoomName']
                }
            }
        else:
            return {
                'error': 1,
                'error_description': self._errcode(data.get('statusCode', 0))
            }
    def _errcode(self, code=0):
        errors = {
            204: 'shiroJID无效',
            0: '未知错误'
        }
        return errors.get(code, errors[0])
    def _request(self, uri, params=None):
        url = f'https://application.xiaofubao.com/app/electric/{uri}'
        headers = {'Cookie': f'shiroJID={self.config["shiroJID"]}'}
        params['ymId'] = self.config['ymId']
        params['platform'] = ''
        response = requests.post(url, headers=headers, data=params)
        return response.json()
    def get_room_and_surplus(self):  #需自己设置校区等具体信息
        area_info = self.query_area()
        area_id = area_info['data'][1]['id']
        building_list = self.query_building(area_id)
        building_code = building_list['data'][8]['buildingCode']
        floor_list = self.query_floor(area_id, building_code)
        floor_code = floor_list['data'][5]['floorCode']
        room_list = self.query_room(area_id, building_code, floor_code)
        room_code = room_list['data'][3]['roomCode']
        room_info = self.query_room_surplus(area_id, building_code, floor_code, room_code)
        surplus = room_info['data']['surplus']
        name = room_info['data']['roomName']
        return name,surplus