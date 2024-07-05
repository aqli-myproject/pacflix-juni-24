# # Import necessary libraries for table formatting and mathematical calculations
from tabulate import tabulate
from math import sqrt

# Create object class Membership
class Membership:
    """
    A class to represent and manage membership data, benefits, requirements, and pricing for users.
    
    Attributes:
        data (dict): A class-level dictionary to store user memberships.
    """
    # Initialize membership data
    data = {
            "Sumbul": "Platinum",
            "Ana": "Gold",
            "Cahya": "Platinum"
        }
    
    # inisialisai attribute
    def __init__(self, username: str):
        """
        Initializes the Membership instance with a username.

        Args:
            username (str): The username of the member.
        """
        self.username = username
        
    # method untuk menampilkan benefit membership
    def show_benefit(self) -> None:
        """
        Displays the benefits of each membership tier in a tabulated format.
        """
        # Define headers for the table
        headers = ["Tier Membership", "Discount", "Benefit"]
        
        # Define the benefit details for each membership tier
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojol"],
            ["Silver", "8%", "Voucher Makanan"]
        ]
        
        print("PacCommerce Benefit Membership")
        print("")
        print(tabulate(tables, headers, tablefmt="presto"))
        
    def show_requirements(self) -> None:
         """
        Displays the requirements for each membership tier in a tabulated format.
        """
        # Define headers for the table
        headers = ["Tier Membership", "Monthly Expense (Juta)", "Monthly Income (Juta)"]
        
        # Define the requirement details for each membership tier
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]
        
        print("PacCommerce Requirements Membership")
        print("")
        print(tabulate(tables, headers, tablefmt = "presto"))
        
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, monthly_expense: float, monthly_income: float):
        """
        Predicts the membership tier based on the user's monthly expense and income using Euclidean distance.

        Args:
            monthly_expense (float): The user's monthly expense.
            monthly_income (float): The user's monthly income.

        Raises:
            Exception: If monthly expense is greater than monthly income.
        """
        # Define the parameters for each membership tier
        parameter_data = [[8, 15], [6, 10], [5, 7]]
        
        # List to store calculated distances
        result_tmp = []
            
        # iterate for each tier membership
        for idx in range(len(parameter_data)):
            
            # Check if the monthly expense is less than the monthly income
            if monthly_expense < monthly_income:
                
                # Calculate Euclidean distance for each tier
                euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                      (monthly_income - parameter_data[idx][1])**2), 2)
                
                # store the result to list
                result_tmp.append(euclidean_dist)
                
            else:
                raise Exception("Expense tidak boleh lebih besar dari Income")
    
        # Store the distances in a dictionary with the corresponding membership tier
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {dict_result}")
    
        # Find the minimum distance
        get_min_distance = min(result_tmp)
        
        # Determine the membership tier with the minimum distance
        for key, value in dict_result.items():
            # compare with minimum data
            if value == get_min_distance:
                print(key)
                # Assign the predicted membership to the user
                self.data[self.username] = key

    # method to show membership data
    # from the database
    def show_membership(self, username):
        if username in self.data:
            return self.data.get(username)
    
    def calculate_price(self, username: str, list_harga: list):
        """
        Calculates the total price for a user after applying the membership discount.

        Args:
            username (str): The username of the member.
            list_harga (list): A list of item prices.

        Returns:
            float: The total price after applying the discount.

        Raises:
            Exception: If the membership is not valid or an error occurs.
        """
        try:
            # Get the user's membership tier
            membership = self.data.get(username)
            
            # Calculate the total price of the items
            sum_harga = sum(list_harga)
            
            # Apply the discount based on the membership tier
            if membership == "Platinum":
                # get discount 15%
                total_price = sum_harga - (sum_harga * 0.15)
                
                return total_price
                
            elif membership == "Gold":
                total_price = sum_harga - (sum_harga * 0.10)
                
                return total_price
            
            elif membership == "Silver":
                total_price = sum_harga - (sum_harga * 0.08)
                
                return total_price
            
            else:
                raise Exception("Membership tidak Valid!!!!!")
            
        except:
            raise Exception("Error in Program")



# Create Object for User
user_1 = Membership(username = "Santoso")
print("User saat ini adalah Santoso")
print("---------------------------------")
print(" ")

# Tes Case 1
print("Test Case 1 get benefit")
print("---------------------------------")
user_1.show_benefit()
print(" ")
print(" ")

# Tes Case 2
print("Test Case 2 get requirements")
print("---------------------------------")
user_1.show_requirements()
print(" ")
print(" ")

# Tes Case 3
print("Test Case 3 predict membership")
print("---------------------------------")
user_1.predict_membership(monthly_expense = 3,
                         monthly_income = 20)
print(" ")
print(" ")

print("show membership")
print("---------------------------------")
status_membership = user_1.show_membership(user_1.username)
print(f"Status membership Ana adalah {status_membership}")
print(" ")
print(" ")

# Tes Case 4
print("Tes Case 4 calculate price")
print("---------------------------------")
calculate_membership_price = user_1.calculate_price(user_1.username, [150000, 200000, 400000])
print(f"Biaya membership Santoso adalah Rp {calculate_membership_price}")
print(" ")
print(" ")

print("show data user membership")
print("---------------------------------")
print(user_1.data)
print(" ")
print(" ")

print("another tes case user Ana")
print("---------------------------------")
status_membership = user_ana = Membership(username = "Ana")
print(f"Status membership Ana adalah {status_membership}")
user_ana.data
calculate_membership_price = user_ana.calculate_price(user_ana.username, [150000, 200000, 400000])
print(f"Biaya membership Ana adalah Rp {calculate_membership_price}")

print("another tes case user Bambang")
print("---------------------------------")
user_bambang = Membership(username = "Bambang")
user_bambang.predict_membership(monthly_expense=3, monthly_income=4)
status_membership = user_bambang.show_membership(user_bambang.username)
print(f"Status membership Bambang adalah {status_membership}")
calculate_membership_price = user_bambang.calculate_price(user_bambang.username, [300_000, 150_000, 1_250_000, 15_000])
print(f"Biaya membership Bambang adalah Rp {calculate_membership_price}")