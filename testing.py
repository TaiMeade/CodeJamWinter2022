import os
import cv2
# desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))

# newFolder = os.path.join(desktopPath, "qrCodes")
# os.mkdir(newFolder)

# directory = 'files'
 
# # iterate over files in
# # that directory
# folderName = input("Please enter the folder that your QR Codes are stored in: ")

# desktopPath = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop')) # Creds to StackOverflow

# directory = f"{desktopPath}/{folderName}"

# for filename in os.listdir(desktopPath + "\qrCodes"):
#     f = os.path.join(directory, filename)
#     if os.path.isfile(f):
#         d = cv2.QRCodeDetector()
#         value, points, straightQRCode = d.detectAndDecode(cv2.imread(f))
#         print(value)
        
#print(desktopPath)

#-----------------------------------------------------------------------------------------------------------------------


# importing the csv module
import csv
 
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
 
# name of csv file
filename = "university_records.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)