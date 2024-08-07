import os
import json


class Banks(object):
    SYSTEM_PATH = os.getcwd()
    BANKS_FILE = os.path.join(SYSTEM_PATH, "data/banks.json")
    BANKS_BRANCHES_FILE = os.path.join(SYSTEM_PATH, "data/branches.json")
    BANKS_CONTACTS_FILE = os.path.join(SYSTEM_PATH, "data/contacts.json")

    def get_file_data(self, json_file_path: str):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data

    def get_banks(self):
        data = self.get_file_data(self.BANKS_FILE)
        banks = data["banks"]
        return banks

    def get_bank(self, bank_code: str):
        banks = self.get_banks()
        for bank in banks:
            if bank["code"] == bank_code:
                return bank
        return {"message": "A bank with that code doesnt exist"}

    def get_regional_town_council_banks(self):
        banks = self.get_banks()
        regional_town_council_banks = [
            bank for bank in banks if bank["category"] == "regional town council bank"
        ]
        return regional_town_council_banks

    def get_regional_town_municipal_banks(self):
        banks = self.get_banks()
        regional_town_municipal_banks = [
            bank for bank in banks if bank["category"] == "regional town municipal bank"
        ]
        return regional_town_municipal_banks

    def get_regional_town_municipal_outside_reginal_capital_banks(self):
        banks = self.get_banks()
        regional_town_municipal_outside_reginal_capital_banks = [
            bank
            for bank in banks
            if bank["category"]
            == "regional town municipal outside reginal capital bank"
        ]
        return regional_town_municipal_outside_reginal_capital_banks

    def get_house_financing_banks(self):
        banks = self.get_banks()
        house_financing_banks = [
            bank for bank in banks if bank["category"] == "house financing bank"
        ]
        return house_financing_banks

    def get_commercial_banks(self):
        banks = self.get_banks()
        commercial_banks = [
            bank for bank in banks if bank["category"] == "commercial bank"
        ]
        return commercial_banks

    def get_mortgage_financing_banks(self):
        banks = self.get_banks()
        mortgage_financing_bank = [
            bank for bank in banks if bank["category"] == "mortigage refinancing bank"
        ]
        return mortgage_financing_bank

    def get_leasing_banks(self):
        banks = self.get_banks()
        leasing_banks = [bank for bank in banks if bank["category"] == "leasing bank"]
        return leasing_banks

    def get_development_banks(self):
        banks = self.get_banks()
        development_banks = [
            bank for bank in banks if bank["category"] == "developement bank"
        ]
        return development_banks

    def get_microfinance_banks(self):
        banks = self.get_banks()
        microfinance_banks = [
            bank for bank in banks if bank["category"] == "microfinance bank"
        ]
        return microfinance_banks

    def get_bank_contacts(self, bank_code: str):
        pass

    def get_all_branches_for_all_banks(self):
        pass

    def get_all_branches_for_all_banks_by_region(self, region_code: str):
        pass

    def get_bank_branches(self, bank_code: str):
        pass

    def get_bank_branches_by_region(self, bank_code: str, region_code: str):
        pass


tanzanian_banks = Banks()
