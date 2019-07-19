'''
    CS5001
    Fall 2018
    HW5
    Brad Egan
'''

from hanoi_viz import *

SOURCE = 'Bob'
TARGET = 'Jerry'
TEMP = 'Pat'
MIN_DISKS = 1
MAX_DISK = 8


def move_tower(SOURCE, TARGET, TEMP, tower_dict, num_disks):
    ''' Function: move_tower
        Parameters: SOURCE, str
                    TARGET, str
                    TEMP, str
                    tower_dict, dictionary
                    num_disks, int
        Returns: none
        Does: Move tower function that initiates Tower of Hanoi sequence.
              Moves single disk in base case from SOURCE to TARGET tower.
              Otherwise calls, move_tower function, and move_disk function to
              recursively determine the ordering of movement to move from SOURCE
              to TARGET.
              
    '''
    if num_disks == 1:
        move_disk(SOURCE, TARGET, tower_dict)
    else:
        move_tower(SOURCE, TEMP, TARGET, tower_dict, num_disks -1)
        move_disk(SOURCE, TARGET, tower_dict)
        move_tower(TEMP, TARGET, SOURCE, tower_dict, num_disks -1)
        

def main():
    ''' Function: main
        Parameters: none
        Returns: none
        Does: Prompts user for number of disks between 1 and 8.
        Initializes tower dictionary of disk locations, then initilizes
        move_tower function which moves disks from SOURCE to TARGET
    '''
    
    while True:
        try:
            num_disks = int(input("What is the number of disk (1-8)? \n"))
            if num_disks >= MIN_DISKS and num_disks <= MAX_DISK:
                break
        except ValueError:
            print ("Needs to be an integer 1-8! Please try again.")
            
    tower_dict = initialize_towers(num_disks, SOURCE, TARGET, TEMP)
    move_tower(SOURCE, TARGET, TEMP, tower_dict, num_disks)
        
main()
