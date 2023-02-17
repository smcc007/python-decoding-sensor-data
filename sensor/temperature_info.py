from house_info import HouseInfo


class TemperatureData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(int(rec, base=10))
