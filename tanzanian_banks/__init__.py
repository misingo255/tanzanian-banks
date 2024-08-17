import os
import json


class Banks(object):
    system_path = os.getcwd()
    bank_file = os.path.join(system_path, "data/banks.json")
    banks_branches_file = os.path.join(system_path, "data/branches.json")
    banks_contacts_file = os.path.join(system_path, "data/contacts.json")
    banks_regions_file = os.path.join(system_path, "data/regions.json")
    banks_categories_file = os.path.join(system_path, "data/categories.json")

    def get_file_data(self, json_file_path: str):
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data

    def get_banks(self):
        data = self.get_file_data(self.bank_file)
        banks = data["banks"]
        return banks

    def get_contacts(self):
        data = self.get_file_data(self.banks_contacts_file)
        contacts = data["contacts"]
        return contacts

    def get_regions(self):
        data = self.get_file_data(self.banks_regions_file)
        regions = data["regions"]
        return regions

    def get_categories(self):
        data = self.get_file_data(self.banks_categories_file)
        categories = data["categories"]
        return categories

    def get_bank(self, bank_code: str):
        banks = self.get_banks()
        for bank in banks:
            if bank["code"] == bank_code:
                return bank
        return {
            "message": "Wrong bank code, please check the list of all banks to know its code"
        }

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
        contacts = self.get_contacts()
        contacts = [contact for contact in contacts if contact["code"] == bank_code]
        if contacts:
            return contacts
        return {
            "message": "Wrong bank code, please check the list of all banks to know its code"
        }

    def get_all_branches_for_all_banks(self):
        data = self.get_file_data(self.banks_branches_file)
        branches = data["branches"]
        return branches

    def get_bank_branches(self, bank_code: str):
        branches = self.get_all_branches_for_all_banks()
        branches = [branch for branch in branches if branches["code"] == bank_code]
        if branches:
            return branches
        return {
            "message": "Wrong bank code, please check the list of all banks to know its code"
        }

    def get_all_branches_for_all_banks_by_region(self, region_code: str):
        regions = self.get_regions()
        region = [region for region in regions if regions["code"] == region_code]
        if not region:
            return {
                "message": "Wrong region code, please check the list of all regions to know its code"
            }
        branches = self.get_all_branches_for_all_banks()
        branches = [branch for branch in branches if branches["region"] == region]
        if not branches:
            return {
                "message": "Wrong region code, please check the list of all regions to know its code"
            }
        return branches

    def get_bank_branches_by_region(self, bank_code: str, region_code: str):
        regions = self.get_regions()
        region = [region for region in regions if regions["code"] == region_code]
        if not region:
            return {
                "message": "Wrong region code, please check the list of all regions to know its code"
            }
        branches = self.get_all_branches_for_all_banks()
        branches = [
            branch
            for branch in branches
            if branches["region"] == region and branches["code"] == bank_code
        ]
        if not branches:
            return {
                "message": "Wrong region code or bank code, please check the list of all regions and banks to know their code"
            }
        return branches


tanzanian_banks = Banks()
