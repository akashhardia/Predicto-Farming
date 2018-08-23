import sys, json, numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()
    #lines = dict(lines)
    #print(lines)
    lr  = LinearRegression()
    df = pd.read_csv(r"C:\Users\akash\Downloads\aids.csv")
    lr.fit(df[['Unnamed: 0', 'year', 'quarter', 'delay', 'dud', 'time']],df['y'])
    df2 = df[['Unnamed: 0', 'year', 'quarter', 'delay', 'dud', 'time']]
    #print(lr.predict(pd.DataFrame(np.array([3,1983,3,5,0,1]).reshape(1,-1))))
    print(lr.predict(pd.DataFrame(np.array([lines['Unnamed: 0'],lines['year'],lines['quarter'],
                     lines['delay'],lines['dud'],lines['time']]).reshape(1,-1))))

    #print(lines['Unnamed: 0'])
    #print(lines['year'])
    #print(lines['quarter'])
    #print(lines['delay'])
    #print(lines['dud'])
    #print(lines['time'])
    #print("ankur")
    #print("akash")

#start process
if __name__ == '__main__':
    main()
