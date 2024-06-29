from tabulate import tabulate
from typing import Dict

# Create Data User
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

# Create User Class
class User:

    # define atribute username
    def __init__(self, username: str):
        self.username = username

    # create method to check all plan Pacflix
    def check_benefit(self):

        # init columns names
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", 'Benefit']

        #init data
        table = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]

        print("=== PacFLix Plan LIst ===")
        print("")
        print(tabulate(table, headers, tablefmt='github'))

    #method to check current plan based on username
    def check_plan(self) -> None:
        for keys, values in data.items():
            #branching memfilter username
            if self.username == keys:
                #create variabel to store the values
                get_current_plan = values[0]
                get_duration_plan = values[1]

                print(f"username: {self.username}")
                print(f"current plan: {get_current_plan}")
                print(f"duration plan: {get_duration_plan}")

    def upgrade_plan(self, upgrade_plan: str) -> float:

        #define constant for discount
        DISCOUNT_UPGRADE = 0.05

        #iterasi keys & values based on data
        for keys, values in data.items():

            #branching based on username for get current plan and duration plan
            if self.username == keys:

                #get current plan and duration plan data
                get_current_plan = values[0]
                get_duration_plan = values[1]

                #logic to filter not pick the same plan
                if get_duration_plan >= 12:

                    #logic discount
                    if upgrade_plan == "Basic Plan":
                        total_price = 120_000 - (120_000 * DISCOUNT_UPGRADE)
                        return total_price
                        
                    elif upgrade_plan == "Standard Plan":
                        total_price = 160_000 - (160_000 * DISCOUNT_UPGRADE)
                        return total_price

                    elif upgrade_plan == "Premium Plan":
                        total_price = 200_000 - (200_000 * DISCOUNT_UPGRADE)
                        return total_price

                    else:
                        raise Exception("Plan didn't exist!")
                else:
                    #branching if not discount
                    if upgrade_plan == "Basic Plan":
                        total_price = 120_000
                        return total_price
                        
                    elif upgrade_plan == "Standard Plan":
                        total_price = 160_000
                        return total_price

                    elif upgrade_plan == "Premium Plan":
                        total_price = 200_000
                        return total_price

                    else:
                        raise Exception("Plan didn't exist!")

# Create New User Object
class NewUser:

    # create empty list to store referral code
    referral_code = []
    
    def __init__(self, username: str):
        self.username = username

    #method to generate referral code based on data
    def generate_referral_code(self, data: Dict[str, str]):
        #iterasi data
        for value in data.values():
            #store the refcode  to vars
            get_ref_code = value[2]
            #append to empty list
            self.referral_code.append(get_ref_code)

    #method to new user pick plan
    def pick_plan(self, new_plan: str, referral_code: str) -> float:
        #init discount
        DISCOUNT_NEW_USER = 0.04

        #valid referral code
        if referral_code in self.referral_code:
            #discount logic
            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT_NEW_USER)
                return total_price

            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT_NEW_USER)
                return total_price
                
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT_NEW_USER)
                return total_price
            else:
                raise Exception("Plan is not ready")
                
        #not input referral code get normal price
        elif (referral_code == "") or (referral_code == None):
            #get normal price
            if new_plan == "Basic Plan":
                total_price = 120_000
                return total_price

            elif new_plan == "Standard Plan":
                total_price = 160_000
                return total_price
                
            elif new_plan == "Premium Plan":
                total_price = 200_000
                return total_price
            else:
                raise Exception("Plan is not ready")
                
        #not valid referral code
        else:
            raise Exception("Referral code didn't exist!")


# Create Object for User
user_1 = User(username = 'Bagus')
print("User saat ini adalah Bagus")
print("--------------")

# Test Case 1
print("Test Case 1 Check Benefit")
print("--------------")
user_1.check_benefit()
print("--------------")

# Test Case 2
print("Test Case 2 Check Plan")
print("--------------")
user_1.check_plan()
print("--------------")

# Tes Case 3
print("Test Case 3 Upgread Plan")
print("--------------")
calculate_upgrade = user_1.upgrade_plan(upgrade_plan = 'Premium Plan')
print(f"Plan baru yang harus dibayar Bagus adalah Rp {calculate_upgrade}")
print("--------------")

# Create Object for NewUser
faizal = NewUser(username = "faizal_icikiwir")
print("User baru yang akan mendaftar layanan pacflix adalah Faizal")
print("--------------")

# Test Case 4
print("Test Case 4 New User Plan with referral code")
print("--------------")
faizal.username
faizal.generate_referral_code(data=data)
faizal.referral_code
calculate_plan_price = faizal.pick_plan(new_plan = "Basic Plan",
                referral_code = "ana-2f9g")
print(f"Plan yang harus dibayar Faizal adalah Rp {calculate_plan_price}")
print("--------------")
print(" ")

print("Test Case 4 New User Plan with referral code None")
print("--------------")
calculate_plan_price = faizal.pick_plan(new_plan = "Basic Plan",
                referral_code = None)
print(f"Plan yang harus dibayar Faizal adalah Rp {calculate_plan_price}")
print("--------------")
print(" ")

print("Test Case 4 New User Plan with referral code Kosong")
print("--------------")
calculate_plan_price = faizal.pick_plan(new_plan = "Basic Plan",
                referral_code = "")
print(f"Plan yang harus dibayar Faizal adalah Rp {calculate_plan_price}")
print("--------------")
print(" ")

print("Test Case 4 New User Plan with referral code Tidak ada dalam daftar")
print("--------------")
calculate_plan_price = faizal.pick_plan(new_plan = "Basic Plan",
                referral_code = "indira-w1we")
print(f"Plan yang harus dibayar Faizal adalah Rp {calculate_plan_price}")
print("--------------")
print(" ")
