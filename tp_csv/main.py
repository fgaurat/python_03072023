import sys
import json


def main():
    
     with open('users.json') as f:
         users = json.load(f)
         
         print(users[0])
         
         
    
    
    
def main_write_json():
    result = []
    with open(r'.\tp_csv\MOCK_DATA.csv', 'r') as f:
        all_data = f.readlines()
        header = all_data[0].strip().split(',')
        data = all_data[1:]
        
        for line in data:
            user ={}
            theListFromTheLine=line.strip().split(',')

            z = zip(header,theListFromTheLine)
            user = dict(z)
            # for i,h in enumerate(header):
            #     user[h] = theListFromTheLine[i]
                
            
            result.append(user)

    print(result)
    with open('users.json','w') as f:
        json.dump(result, f)

if __name__ == '__main__':
    main()
