def initialize_spreadsheet(sheet):
    sheet.write(0, 0, "Time Section")
    sheet.write(9, 0, "Quotient Sum Section")
    for row in range(8):
        sheet.write(row+1, 0, str(2**(row+2)) + "-Bit Case")
    for row in range(10, 18):
        sheet.write(row, 0, str(2**(row - 8)) + "-Bit Case")


def calculate_average_runtime(number_of_test_cases, sheet):
    """
     OK SO I can't find the average on the same line as where I input data
     So I decided to make it so it will show average run times in the first column
     Which just so happens to start at row 10 instead of 1 so I have to offset by 9
     TL:DR All averages are thrown in the first column and need to be offset by 9 to do so
    """
    # Initializing the Column
    sheet.write(18, 0, "Average Run Times")
    sheet.write(18, 3, "Average Quotient")
    # This is starting at the first row and ending at the last
    for row in range(19, 27):
        # Setting averages of rows this command in excel
        # =SUM(row:row)/number_of_test_cases
        # This should calculate the average value of all the run times in that row
        sheet.write(row, 0, "=SUM(" + str(row - 17) + ":" + str(row - 17) + ")/"
                    + str(number_of_test_cases))
        sheet.write(row, 3, "=SUM(" + str(row - 8) + ":" + str(row - 8) + ")/"
                    + str(number_of_test_cases))


def time_to_test(number_of_test_cases):
    from divide import main_div
    from random_input_generator import create_json_file
    import xlwt
    # Creating file
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Sheet")
    initialize_spreadsheet(sheet)
    for i in range(number_of_test_cases):
        # we ignore the 0 column since that was initialized
        column = (2 * i) + 2
        row = 0
        sheet.write(row, column, "Time Trial " + str(i + 1))
        sheet.write(row + 9, column, "Total Quotient " + str(i + 1))
        row += 1
        create_json_file()
        time, quotient = main_div(1)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(2)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(3)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(4)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(5)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(6)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(7)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        time, quotient = main_div(8)
        sheet.write(row, column, time)
        sheet.write(row + 9, column, quotient)
        row += 1
        print(str(i) + " Case Finished")
    # Setting up first column starting at row 10 to be showing average run times
    calculate_average_runtime(number_of_test_cases, sheet)
    # Saving file
    book.save("Trial Spread Sheet.xls")


if __name__ == '__main__':
    # Enter the number of test cases you want to run
    time_to_test(4)