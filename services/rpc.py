import logging
from lib.basehandler import RpcHandler
from lib.jsonrpc import ServerException
import models


class ApiHandler(RpcHandler):

# Sensor Section
    def list_sensor(self):

        sensors = models.Sensor.select().order_by(models.Sensor.id)

        return [sensor.to_client() for sensor in sensors]

    def get_sensor(self, sensor_id):

        sensor = models.Sensor.get_by_id(sensor_id)

        if not sensor:
            sensor = models.Sensor()

        return sensor.to_client()

    def save_sensor(self, data):
        id = data.get('id')
        if id:
            sensor = models.Sensor.get_by_id(id)
        else:
            sensor = models.Sensor()

        sensor.label = data.get('label')
        sensor.pin = data.get('pin')
        sensor.save()

        return sensor.to_client()

    def delete_sensor(self, sensor_id):

        sensor = models.Sensor.get_by_id(sensor_id)

        if sensor:
            sensor.delete_instance()
            return True
        return False

# Device Section
    def list_device(self):

        devices = models.Device.select().order_by(models.Device.id)

        return [device.to_client() for device in devices]

    def get_device(self, device_id):

        device = models.Device.get_by_id(device_id)

        if not device:
            device = models.Device()

        return device.to_client()

    def save_device(self, data):
        id = data.get('id')
        if id:
            device = models.Device.get_by_id(id)
        else:
            device = models.Device()

        device.label = data.get('label')
        device.pin = data.get('pin')
        device.value = False    # Always starts as False
        device.save()

        return device.to_client()

    def delete_device(self, device_id):

        device = models.Device.get_by_id(device_id)

        if device:
            device.delete_instance()
            return True
        return False

# Rule Section
    def list_rule(self):

        return [
            {
                'id': 1,
                'label': 'Turn on the maintenance light at night.',
            },
            {
                'id': 2,
                'label': 'Turn on water when moisture is low.',
            },
            {
                'id': 3,
                'label': 'Turn on fan when heat is high.',
            },
            {
                'id': 4,
                'label': 'Turn on the CO2 tank when CO2 is low.',
            }
        ]