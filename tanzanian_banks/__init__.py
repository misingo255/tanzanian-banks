import os
import json


class Banks(object):
    SYSTEM_PATH = os.getcwd()
    BANKS_FILE = os.path.join(SYSTEM_PATH, "data/banks.json")

    def get_file_data(self, json_file_path: str):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data

    def get_banks(self):
        pass

    def get_bank(self, bank_code: str):
        pass

    def get_commercial_banks(self):
        pass

    def get_mortigage_banks(self):
        pass

    def get_community_banks(self):
        pass

    def get_developmement_banks(self):
        pass

    def get_microfinace_banks(self):
        pass

    def get_branches(self, bank_code: str):
        pass

    def get_regional_branches(self, bank_code: str, region_code: str):
        pass

    def count(self):
        data = self.get_file_data(self.BANKS_FILE)
        amount = len(data["banks"])
        return amount


tanzanian_banks = Banks()
