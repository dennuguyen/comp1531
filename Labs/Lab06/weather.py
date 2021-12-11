"""
Module docstring because pylint said so
"""
import sys
from datetime import datetime
from statistics import mean

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
        DATE = sys.argv[1]
        PLACE = sys.argv[2]

        # Check date and place is not empty
        assert DATE
        assert PLACE

        # Check date is in correct format and rearrange to YYYY-MM-DD format
        DATE = datetime.strptime(DATE, "%d-%m-%Y").strftime("%Y-%m-%d")

    except AssertionError:
        raise AssertionError("Invalid input")

    except ValueError:
        raise ValueError("Expected DD-MM-YYYY format")

    with open("weatherAUS.csv", "r") as in_file:

        # Get the file line by line into a list
        LIST_ = in_file.readlines()
        del LIST_[0]  # Remove header

        # Modify list to only include entries from correct place
        LIST_ = [day for day in LIST_ if PLACE in day]

        AVG_MIN_LIST = []
        AVG_MAX_LIST = []

        for day in LIST_:
            day_list = day.split(',')  # Split the day into lists

            try:  # Get the average min and max temp of the data set
                AVG_MIN_LIST.append(float(day_list[2]))
                AVG_MAX_LIST.append(float(day_list[3]))
            except ValueError:  # Handle could not convert string to float: "NA"
                pass

            # Get the min temp and max temp of the day
            if day.startswith(DATE + "," + PLACE + ","):
                min_temp = float(day_list[2])
                max_temp = float(day_list[3])

        try:  # If min_temp is None then there was no match
            assert min_temp
        except:
            raise NameError("Did not find a match")

        # Print results
        print(
            f"MinTemp is {round(mean(AVG_MIN_LIST) - min_temp, 1)} degrees below average minimum"
        )
        print(
            f"MaxTemp is {round(mean(AVG_MAX_LIST) - max_temp, 1)} degrees below average maximum"
        )
