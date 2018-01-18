# A quick calc program to track expenses
def main():
  print("Calculate ten year investiment")
  principle = float(input("Enter principle: "))

  apr = float(input("Annual APR: "))

  for i in range(10):
      principle = principle * (1 + apr)

  print("Investment value after 10 years is:", principle, sep="---")

main()
