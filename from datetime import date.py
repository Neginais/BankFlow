from datetime import date

# ---------------------- BankAccount Class ----------------------

class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def show_balance(self):
        print(f'Current Balance: ${self.balance:.2f}')

# ---------------------- CreditScore Class ----------------------

class CreditScore:
    def __init__(self):
        self.score = 300

    # Placeholder: You can add methods to update credit score based on transactions

# ---------------------- Loan Class ----------------------

class Loan:
    PLAN_1_AMOUNT = 10000
    PLAN_1_INTEREST = 0.05
    PLAN_1_PERIOD = 3

    PLAN_2_AMOUNT = 10000
    PLAN_2_INTEREST = 0.06
    PLAN_2_PERIOD = 5

    PLAN_3_AMOUNT = 20000
    PLAN_3_INTEREST = 0.04
    PLAN_3_PERIOD = 3

    PLAN_4_AMOUNT = 20000
    PLAN_4_INTEREST = 0.05
    PLAN_4_PERIOD = 5

    def __init__(self, current_balance, credit_score):
        self.current_balance = current_balance
        self.credit_score = credit_score
        self.amount = 0
        self.period = 0

    def loan_request(self):
        self.amount = int(input("Enter the loan amount you want: $"))
        self.period = int(input("Enter loan period in years: "))
        return self.amount, self.period

    def suggested_plan(self):
        if self.amount <= self.PLAN_1_AMOUNT and self.period <= self.PLAN_1_PERIOD and self.credit_score.score > 350:
            return "Plan 1", self.PLAN_1_AMOUNT, self.PLAN_1_INTEREST, self.PLAN_1_PERIOD

        elif self.amount <= self.PLAN_2_AMOUNT and self.period <= self.PLAN_2_PERIOD:
            return "Plan 2", self.PLAN_2_AMOUNT, self.PLAN_2_INTEREST, self.PLAN_2_PERIOD

        elif self.amount <= self.PLAN_3_AMOUNT and self.period <= self.PLAN_3_PERIOD and self.current_balance >= 3000 and self.credit_score.score >= 350:
            return "Plan 3", self.PLAN_3_AMOUNT, self.PLAN_3_INTEREST, self.PLAN_3_PERIOD

        elif self.amount <= self.PLAN_4_AMOUNT and self.period <= self.PLAN_4_PERIOD and self.current_balance > 3000:
            return "Plan 4", self.PLAN_4_AMOUNT, self.PLAN_4_INTEREST, self.PLAN_4_PERIOD

        else:
            return None, 0, 0, 0

    def calculate_monthly_payment(self, loan_amount, interest_rate, years):
        monthly_interest = interest_rate / 12
        months = years * 12
        p = loan_amount
        # Amortization formula
        if monthly_interest == 0:
            return p / months
        payment = (monthly_interest * p) / (1 - (1 + monthly_interest) ** (-months))
        return payment

# ---------------------- LoanAgreement Class ----------------------

class LoanAgreement:
    def __init__(self, account_holder, account_number, loan_amount, interest_rate, monthly_payment, payment_period):
        self.account_holder = account_holder
        self.account_number = account_number
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.monthly_payment = monthly_payment
        self.payment_period = payment_period

    def generate_agreement(self):
        print("\n--- LOAN AGREEMENT ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Loan Amount: ${self.loan_amount}")
        print(f"Interest Rate: {self.interest_rate * 100:.2f}% per annum")
        print(f"Monthly Payment: ${self.monthly_payment:.2f}")
        print(f"Payment Period: {self.payment_period} years")
        print("\nYou may prepay the loan anytime without penalty.")
        print("Defaulting on payments will make the full balance immediately due.")
        print("----------------------------\n")
        confirm = input("Do you confirm this agreement? (yes or no): ").strip().lower()
        if confirm == "yes":
            print("Agreement confirmed. Thank you!")
            return True
        else:
            print("Agreement cancelled.")
            return False

# ---------------------- Main Program Loop ----------------------

def main():
    while True:
        print("\n=== Welcome to Capital One Banking System ===\n")

        # Create bank account
        account = BankAccount(1234567, "John Smith", 5000)
        account.deposit()
        account.withdraw()
        account.deposit()
        account.show_balance()

        # Credit score object (fixed 300 for now)
        credit_score = CreditScore()

        # Loan process
        print("\n--- Loan Application ---")
        loan = Loan(account.balance, credit_score)
        loan.loan_request()
        plan, amount, interest, years = loan.suggested_plan()

        if plan:
            print(f"\nSuggested Loan Plan: {plan}")
            print(f"Loan Amount: ${amount}")
            print(f"Interest Rate: {interest * 100:.2f}%")
            print(f"Payment Period: {years} years")
            monthly_payment = loan.calculate_monthly_payment(amount, interest, years)
            print(f"Estimated Monthly Payment: ${monthly_payment:.2f}")

            confirm = input("Would you like to confirm this loan? (yes or no): ").strip().lower()
            if confirm == "yes":
                agreement = LoanAgreement(account.account_holder_name, account.account_number,
                                         amount, interest, monthly_payment, years)
                if agreement.generate_agreement():
                    print("Loan process completed. Exiting program.")
                    break  # Exit loop after loan approval
                else:
                    print("Loan agreement not confirmed. Restarting...\n")
            else:
                print("Loan cancelled. Restarting...\n")

        else:
            print("Sorry, we cannot offer a loan based on your request.")
        
        retry = input("Would you like to try again? (yes or no): ").strip().lower()
        if retry != "yes":
            print("Thank you for banking with us. Goodbye!")
            break

if __name__ == "__main__":
    main()
