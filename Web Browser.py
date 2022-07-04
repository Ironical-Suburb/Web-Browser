#----------------------------------------------------
# web browser simulator
# has forward and backward button functionality and add a new site 
#----------------------------------------------------

def getAction():
    '''
    
    1.This function accepts the key
    2.Tells the main function about which key is selected
    3.Returns"Invalid Key" if the key is not given in the condition
    
    Inputs: takes a URL as input 
    Returns: Key as 'str'
    
    '''
    
    key = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    while key in ('<','q','>','='):
        return (key)
    else:
        print('Invalid entry')
    
    
        
def goToNewSite(current, pages):
    '''
    
    1.Creates a new variable to take new URL as input 
    2.Inserts the new URL into the pages list
    3.Returns the updated current index 
    
    Inputs: Takes the new page as input
    Returns: updated current index and pages
    
    '''   
    current = current + 1
    new_page = input("URL: ")
    pages.insert(current,new_page)
    
    '''
    Test
    print(current,pages)
    '''
    return current

    
def goBack(current, pages):
    '''
    1.Checks whether the current index is less than the length of the pages
    2.If the condition is not satisfied error is displayed 
    2.Returns the updated current index 
    
    Inputs: Takes the updated pages and updated index as input
    Returns: updated current website
    
    '''    
    
    if ( current-1 <= len(pages)):
        return current -1 
    if current < 0:
        print('Cannot go back')
    else:
        print('Cannot go back')
        
        '''
        Test
        print(current,pages)
        '''  
        
        return current 

def goForward(current, pages):
    '''
    
    1.Checks whether the current index is more than or equal to length of pages 
    2.If the condition is not satisfied error is displayed 
    2.Returns the updated current index 
    
    Inputs: Takes the updated pages and updated index as input
    Returns: updated current website
    
    '''    
   
    if ( current+1 >= len(pages)) :
        print('Cannot go forward')
    else:
        return (current+1)
        
    '''
        Test
        print(current,pages)
    '''       
        
    return current     


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.Github.com'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('Currently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.',currentIndex)    
    
        
if __name__ == "__main__":
    main()
