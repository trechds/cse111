# Example 1

# try:
        # Write normal code here. This block must include
        # code that falls into two groups:
        # 1. Code that may cause an exception to be raised
        # 2. Code that depends on the results of the code
        #    in the first group
# except ZeroDivisionError as zero_div_err:
        # Code that the computer executes if the code in the try
        # block caused a function to raise a ZeroDivisionError.
# except ValueError as val_err:
        # Code that the computer executes if the code in the
        # try block caused a function to raise a ValueError.
# except (TypeError, KeyError, IndexError) as error:
        # Code that the computer executes if the code in the
        # try block caused a function to raise a TypeError,
        # KeyError, or IndexError.
# except Exception as excep:
        # Code that the computer executes if the code in the try
        # block caused a function to raise any exception that
        # was not handled by one of the previous except blocks.
# except:
        # Code that the computer executes if the code in the
        # try block caused a function to raise anything that
        # was not handled by one of the previous except blocks.
# else:
        # Code that the computer executes after the code
        # in the try block if the code in the try block
        # did not cause any function to raise an exception.
# finally:
        # Code that the computer executes after all the other
        # code in try, except, and else blocks regardless of
        # whether an exception was raised or not.