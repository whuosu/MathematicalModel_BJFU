"""
Author:Shuo Wu
Date  :2020/5/20
For   :Mathematical Model
"""


import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xdrlib


""" Define Variable """
dayOfData = 0
infectedNumber = []
incresedNumber = []
deadNumber = []
curedNumber = []
curePercent = []
deadPercent = []


""" Get Data From Excel """
def getDataForFile(numList, beginCol, index = 0, filePath = 'Data.xlsx'):
    try:
        data = xlrd.open_workbook(filePath)
        table = data.sheet_by_index(0)
        for col in [(x * 7 + beginCol - 1) for x in range(0, 8)]:
            for row in range(1, 16):
                numList.append(table.cell(col, row).value)
        numList.pop()
    except:
        pass


getDataForFile(infectedNumber, 4)
getDataForFile(incresedNumber, 5)
getDataForFile(curedNumber, 6)
getDataForFile(deadNumber, 7)
getDataForFile(curePercent, 8)
getDataForFile(deadPercent, 9)


""" Data Visualable """

def dataVisualableOfNumber(infectedNumber, incresedNumber, curedNumber, deadNumber):
    plt.plot([x for x in range(0, len(infectedNumber))], infectedNumber, label='Infected')
    plt.plot([x for x in range(0, len(incresedNumber))], incresedNumber, label='Increased')
    plt.plot([x for x in range(0, len(curedNumber))], curedNumber, label='Cured')
    plt.plot([x for x in range(0, len(deadNumber))], deadNumber, label='Dead')

    plt.xlabel('Day')
    plt.ylabel('Number')

    plt.title('Number of Infected, Increased, Cured People with COVID-19')
    plt.legend()
    plt.show()


def dataVisualableOfPercent(curePercent, deadPercent):
    plt.plot([x for x in range(0, len(deadPercent))], deadPercent, label='DeadPercent')
    plt.plot([x for x in range(0, len(curePercent))], curePercent, label='CuredPercent')

    plt.xlabel('Day')
    plt.ylabel('Percentage')
    plt.yticks([0.5])

    plt.title('Percentage of Dead, Cured People with COVID-19')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    dataVisualableOfNumber(infectedNumber, incresedNumber, curedNumber, deadNumber)
    dataVisualableOfPercent(curePercent, deadPercent)