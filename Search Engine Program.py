#Code By Satyam Toriya on 10/06/2020

#Function Search the svery string in each element of the List
def string_searcher(string):
    List=['Welcome to Python','This is Good ','Python is Good ','''Python is programming Language
  not python Snake''','Hello World','Python Language','I Love Python','Help | Python.org',
          'Python Tutiorial' , 'Python for Beginners']
    #Empty Dictionary for adding Matched Strings with counts
    Dict={}
    #Take Elements from List and convert into lower case letters to both input string
    #and List of String and then split to form a List of strings and then compare List of string
    #with Input String
    for i in List :
        count=0
        for j in string.lower().split():
            if j in i.lower().split():
                count+=i.lower().split().count(j)
        Dict[i]=count
    Dict1=Dict.copy()
    for i in Dict1.keys():
        if Dict1[i]==0:
            Dict.pop(i)
    sort_List=sorted(Dict,key=lambda x: Dict[x],reverse=True)
    print(f"Search Result Found {len(sort_List)} : ")
    for i in sort_List:
        print('*',i)

#Driver code
if __name__=='__main__':
    string=input("Enter String for Search : ")
    string_searcher(string)
    
