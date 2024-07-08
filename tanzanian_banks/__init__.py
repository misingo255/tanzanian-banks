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

    def get_commercial_banks(self):
        banks = self.get_banks()
        commercial_banks = [
            bank for bank in banks if bank["category"] == "Commercial Bank"
        ]
        return commercial_banks

    def get_mortgage_banks(self):
        banks = self.get_banks()
        mortgage_banks = [bank for bank in banks if bank["category"] == "Mortgage Bank"]
        return mortgage_banks

    def get_community_banks(self):
        banks = self.get_banks()
        community_banks = [
            bank for bank in banks if bank["category"] == "Community Bank"
        ]
        return community_banks

    def get_development_banks(self):
        banks = self.get_banks()
        development_banks = [
            bank
            for bank in banks
            if bank["category"] == "Development Financial Institution"
        ]
        return development_banks

    def get_microfinance_banks(self):
        banks = self.get_banks()
        microfinance_banks = [
            bank for bank in banks if bank["category"] == "Microfinance Bank"
        ]
        return microfinance_banks
    
    def get_bank_contacts(self, bank_code: str):
        pass

    def get_bank_branches(self, bank_code: str):
        pass

    def get_bank_regional_branches(self, bank_code: str, region_code: str):
        pass




tanzanian_banks = Banks()
