high_income=True
good_record=False

if high_income and good_record:
  print("Elegible for loan")
elif high_income or good_record:
  print("Needed more information")
else:
  print("Not elegible for loan")