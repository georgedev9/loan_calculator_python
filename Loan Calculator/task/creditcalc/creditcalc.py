import argparse
from math import ceil, log

parser = argparse.ArgumentParser()

parser.add_argument("-p1", "--payment", default=0)
parser.add_argument("-p2", "--principal", default=0)
parser.add_argument("-p3", "--periods", default=0)
parser.add_argument("-i", "--interest", default=0)
parser.add_argument("-t", "--type")

args = parser.parse_args()

calc_type = args.type
principal = int(args.principal)
payment = float(args.payment)
interest = float(args.interest)
periods = int(args.periods)


def calc_differentiated_payments():
    i = interest / (12 * 100)
    overpayment = 0
    for m in range(1, periods + 1):
        diff_payment = (principal / periods) + i * (principal - (principal * (m - 1)) / periods)
        overpayment += ceil(diff_payment)
        print(f"Month {m}: payment is {ceil(diff_payment)}")

    print(f"\nOverpayment = {ceil(overpayment - principal)}")


def calc_number_monthly_payments():
    nominal_interest = interest / (12 * 100)
    x = payment / (payment - nominal_interest * principal)
    number_of_months = ceil(log(x, 1 + nominal_interest))
    years = number_of_months / 12
    months = (12 * (years % 1))
    overpayment = (ceil(payment) * number_of_months) - principal
    print(f"It will take {int(years)} years and {months:.0f} months to repay this loan!")
    print(f"Overpayment = {overpayment}")


def calc_monthly_payment():
    monthly_interest = interest / (12 * 100)
    monthly_payment = (principal * (monthly_interest * (1 + monthly_interest) ** periods)
                       / ((1 + monthly_interest) ** periods - 1))
    overpayment = (ceil(monthly_payment) * periods) - principal
    print(f"Your annuity payment = {ceil(monthly_payment)}!")
    print(f"Overpayment = {overpayment}")


def calc_loan_principal():
    i = interest / (12 * 100)
    p = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    overpayment = (ceil(payment) * periods) - p
    print(f"Your loan principal = {p:.0f}!")
    print(f"Overpayment = {overpayment:.0f}")


if calc_type == "annuity" and principal > 0 and payment > 0 and interest > 0:
    calc_number_monthly_payments()
elif calc_type == "annuity" and principal > 0 and periods > 0 and interest > 0:
    calc_monthly_payment()
elif calc_type == "annuity" and interest > 0 and payment > 0 and periods > 0:
    calc_loan_principal()
elif calc_type == "diff" and principal > 0 and interest > 0 and periods > 0:
    calc_differentiated_payments()
else:
    print("Incorrect parameters")
