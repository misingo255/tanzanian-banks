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
        """
        Read and return data from a specified JSON file.

        Args:
            json_file_path (str): The path to the JSON file.

        Returns:
            dict: The data from the JSON file.

        Example:
            from tanzanian_banks import tanzanian_banks
            data = tanzanian_banks.get_file_data(self.bank_file)
        """
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data

    def get_banks(self):
        """
        Retrieve the list of all banks.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_banks()
        """
        data = self.get_file_data(self.bank_file)
        return data.get("banks", [])

    def get_contacts(self):
        """
        Retrieve the list of all bank contacts.

        Returns:
            list: A list of dictionaries containing bank contact details.

        Example:
            from tanzanian_banks import tanzanian_banks
            contacts = tanzanian_banks.get_contacts()
        """
        data = self.get_file_data(self.banks_contacts_file)
        return data.get("contacts", [])

    def get_regions(self):
        """
        Retrieve the list of all regions.

        Returns:
            list: A list of dictionaries containing region details.

        Example:
            from tanzanian_banks import tanzanian_banks
            regions = tanzanian_banks.get_regions()
        """
        data = self.get_file_data(self.banks_regions_file)
        return data.get("regions", [])

    def get_categories(self):
        """
        Retrieve the list of all bank categories.

        Returns:
            list: A list of dictionaries containing bank category details.

        Example:
            from tanzanian_banks import tanzanian_banks
            categories = tanzanian_banks.get_categories()
        """
        data = self.get_file_data(self.banks_categories_file)
        return data.get("categories", [])

    def get_bank(self, bank_code: str):
        """
        Retrieve a specific bank by its code.

        Args:
            bank_code (str): The code of the bank.

        Returns:
            dict: A dictionary containing bank details or an error message if the bank is not found.

        Example:
            from tanzanian_banks import tanzanian_banks
            bank = tanzanian_banks.get_bank("123")
        """
        banks = self.get_banks()
        for bank in banks:
            if bank["code"] == bank_code:
                return bank
        return {"message": "Wrong bank code, please check the list of all banks to know its code"}

    def get_regional_town_council_banks(self):
        """
        Retrieve all banks categorized as 'regional town council bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_regional_town_council_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "regional town council bank"]

    def get_regional_town_municipal_banks(self):
        """
        Retrieve all banks categorized as 'regional town municipal bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_regional_town_municipal_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "regional town municipal bank"]

    def get_regional_town_municipal_outside_regional_capital_banks(self):
        """
        Retrieve all banks categorized as 'regional town municipal outside regional capital bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_regional_town_municipal_outside_regional_capital_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "regional town municipal outside regional capital bank"]

    def get_house_financing_banks(self):
        """
        Retrieve all banks categorized as 'house financing bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_house_financing_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "house financing bank"]

    def get_commercial_banks(self):
        """
        Retrieve all banks categorized as 'commercial bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_commercial_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "commercial bank"]

    def get_mortgage_financing_banks(self):
        """
        Retrieve all banks categorized as 'mortgage refinancing bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_mortgage_financing_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "mortgage refinancing bank"]

    def get_leasing_banks(self):
        """
        Retrieve all banks categorized as 'leasing bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_leasing_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "leasing bank"]

    def get_development_banks(self):
        """
        Retrieve all banks categorized as 'development bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_development_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "development bank"]

    def get_microfinance_banks(self):
        """
        Retrieve all banks categorized as 'microfinance bank'.

        Returns:
            list: A list of dictionaries containing bank details.

        Example:
            from tanzanian_banks import tanzanian_banks
            banks = tanzanian_banks.get_microfinance_banks()
        """
        banks = self.get_banks()
        return [bank for bank in banks if bank["category"] == "microfinance bank"]

    def get_bank_contacts(self, bank_code: str):
        """
        Retrieve contacts for a specific bank by its code.

        Args:
            bank_code (str): The code of the bank.

        Returns:
            list: A list of dictionaries containing bank contact details or an error message if the bank is not found.

        Example:
            from tanzanian_banks import tanzanian_banks
            contacts = tanzanian_banks.get_bank_contacts("123")
        """
        contacts = self.get_contacts()
        filtered_contacts = [contact for contact in contacts if contact["code"] == bank_code]
        if filtered_contacts:
            return filtered_contacts
        return {"message": "Wrong bank code, please check the list of all banks to know its code"}

    def get_all_branches_for_all_banks(self):
        """
        Retrieve all branches for all banks.

        Returns:
            list: A list of dictionaries containing branch details.

        Example:
            from tanzanian_banks import tanzanian_banks
            branches = tanzanian_banks.get_all_branches_for_all_banks()
        """
        data = self.get_file_data(self.banks_branches_file)
        return data.get("branches", [])

    def get_bank_branches(self, bank_code: str):
        """
        Retrieve all branches for a specific bank by its code.

        Args:
            bank_code (str): The code of the bank.

        Returns:
            list: A list of dictionaries containing branch details or an error message if the bank is not found.

        Example:
            from tanzanian_banks import tanzanian_banks
            branches = tanzanian_banks.get_bank_branches("123")
        """
        branches = self.get_all_branches_for_all_banks()
        filtered_branches = [branch for branch in branches if branch["code"] == bank_code]
        if filtered_branches:
            return filtered_branches
        return {"message": "Wrong bank code, please check the list of all banks to know its code"}

    def get_all_branches_for_all_banks_by_region(self, region_code: str):
        """
        Retrieve all branches for all banks in a specific region.

        Args:
            region_code (str): The code of the region.

        Returns:
            list: A list of dictionaries containing branch details or an error message if the region is not found.

        Example:
            from tanzanian_banks import tanzanian_banks
            branches = tanzanian_banks.get_all_branches_for_all_banks_by_region("456")
        """
        regions = self.get_regions()
        region = next((region for region in regions if region["code"] == region_code), None)
        if not region:
            return {"message": "Wrong region code, please check the list of all regions to know its code"}
        branches = self.get_all_branches_for_all_banks()
        filtered_branches = [branch for branch in branches if branch["region"] == region_code]
        if filtered_branches:
            return filtered_branches
        return {"message": "Wrong region code, please check the list of all regions to know its code"}

    def get_bank_branches_by_region(self, bank_code: str, region_code: str):
        """
        Retrieve all branches for a specific bank in a specific region.

        Args:
            bank_code (str): The code of the bank.
            region_code (str): The code of the region.

        Returns:
            list: A list of dictionaries containing branch details or an error message if the bank or region is not found.

        Example:
            from tanzanian_banks import tanzanian_banks
            branches = tanzanian_banks.get_bank_branches_by_region("123", "456")
        """
        regions = self.get_regions()
        region = next((region for region in regions if region["code"] == region_code), None)
        if not region:
            return {"message": "Wrong region code, please check the list of all regions to know its code"}
        branches = self.get_all_branches_for_all_banks()
        filtered_branches = [branch for branch in branches if branch["region"] == region_code and branch["code"] == bank_code]
        if filtered_branches:
            return filtered_branches
        return {"message": "Wrong region code or bank code, please check the list of all regions and banks to know their code"}


tanzanian_banks = Banks()

