"""
Using nested if-statements should enhance the
readability of our code and make the logic clear
and correct. If you have to pause, scratch your
head, and try really hard to understand some logic,
Python developers believe it is a virtue to break
the logic down into short, distinct, easy to
understand steps.
"""

MINIMUM_SALARY = 30000.0     # The minimum annual salary
MINIMUM_NUMBER_OF_YEARS = 2  # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= MINIMUM_SALARY:
    if years_on_job >= MINIMUM_NUMBER_OF_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed'
              , 'for at least', MINIMUM_NUMBER_OF_YEARS,
              'years to qualify.')
else:
    print('You must earn at least $'
          , format(MINIMUM_SALARY, ',.2f')
          , ' per year to qualify.', sep='')
