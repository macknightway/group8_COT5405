def initialize_spreadsheet(sheet):
    for row in range(8):
        sheet.write(row+1, 0, str(2**(row+2)) + "-Bit Case")


def calculate_average_runtime(number_of_test_cases, sheet):
    """
     OK SO I can't find the average on the same line as where I input data
     So I decided to make it so it will show average run times in the first column
     Which just so happens to start at row 10 instead of 1 so I have to offset by 9
     TL:DR All averages are thrown in the first column and need to be offset by 9 to do so
    """
    # Initializing the Column
    sheet.write(9, number_of_test_cases + 1, "Average Run Times")
    # This is starting at the first row and ending at the last
    for row in range(1, 9):
        # Setting averages of rows this command in excel
        # =SUM(row:row)/number_of_test_cases
        # This should calculate the average value of all the run times in that row
        sheet.write(row + 9, 0, "=SUM(" + str(row + 1) + ":" + str(row + 1) + ")/"
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
        column = i + 1
        row = 0
        sheet.write(row, column, "Time Trial " + str(column))
        row += 1
        create_json_file()
        sheet.write(row, column, main_div(1))
        row += 1
        sheet.write(row, column, main_div(2))
        row += 1
        sheet.write(row, column, main_div(3))
        row += 1
        sheet.write(row, column, main_div(4))
        row += 1
        sheet.write(row, column, main_div(5))
        row += 1
        sheet.write(row, column, main_div(6))
        row += 1
        sheet.write(row, column, main_div(7))
        row += 1
        sheet.write(row, column, main_div(8))
        row += 1
        print(str(i) + " Case Finished")
    # Setting up first column starting at row 10 to be showing average run times
    calculate_average_runtime(number_of_test_cases, sheet)
    # Saving file
    book.save("Trial Spread Sheet.xls")


if __name__ == '__main__':
    # Enter the number of test cases you want to run
    time_to_test(200)