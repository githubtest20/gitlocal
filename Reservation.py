import sys
import json

"""
    This code will auto assign seats based on the nos of tickets
    requested by the user and update the seats in JSON file to
    'RESERVED' and save it for future feed.
"""

book_ticket = int(input('Please enter nos of tickets required : '))
f_path = sys.argv[1]

with open(f_path, 'r+') as f:
    data = json.load(f)  # load the data from json file to a variable
    available_seats = {}
    # Load all the available seats from each row
    for i in data['seats'].keys():
        if data['seats'][i]['status'] == 'AVAILABLE':
            available_seats.setdefault(i[0], []).append(data['seats'][i]['column'])

    nos_of_ticks = []  # list of system chosen tickets

    # Reserving the seats with 'center' as preference
    for row in sorted(available_seats):
        to_assign = sorted(available_seats[row])  # getting row available seats
        m_ind = len(to_assign)//2  # get the middle index for assignment

        # When the entire row is free, getting the mid seats
        if len(available_seats[row]) == data['venue']['layout']['columns']:
            cnt = len(to_assign)//2 - (-(-book_ticket//2))
            mid_seats = [to_assign[cnt+i] for i in range(book_ticket)]
            # Updating the seats to reserved
            for val in mid_seats:
                data['seats'][row+str(val)]['status'] = 'RESERVED'
                nos_of_ticks.append(row+str(val))
            print(f'Your reservation confirmed : {nos_of_ticks}')
            break
        else:  # get the left & right set of seats when mid is reserved
            l_seats = [to_assign[0]]
            r_seats = []
            for ind, val in enumerate(to_assign[1:], start=1):
                if l_seats[-1] == val-1:
                    l_seats.append(val)
                else:
                    r_seats.extend(to_assign[ind:])
                    break

        # fill single seat
        if (book_ticket == 1) and (book_ticket <= len(to_assign)):
            data['seats'][row+str(to_assign[m_ind])]['status'] = 'RESERVED'
            print(f'Your reservation confirmed : {row+str(to_assign[m_ind])}')
            break
        # When the middle seats are already taken, filling the rest if book_ticket > 1
        elif ((book_ticket > 1) and (len(to_assign) < data['venue']['layout']['columns']) and ((len(l_seats) >= book_ticket) or (len(r_seats) >= book_ticket))):
            if len(l_seats) >= book_ticket:
                upd_seats = l_seats[::-1]
            elif len(r_seats) >= book_ticket:
                upd_seats = r_seats[:]

            for ind in range(book_ticket):
                data['seats'][row+str(upd_seats[ind])]['status'] = 'RESERVED'
                nos_of_ticks.append(row+str(upd_seats[ind]))
            print(f'Your reservation confirmed : {nos_of_ticks}')
            break
        else:
            continue

    f.seek(0)  # to move cursor to beginning of file
    json.dump(data, f)  # load the changes into the JSON file
    f.truncate()  # to handle when new data is smaller than the previous
