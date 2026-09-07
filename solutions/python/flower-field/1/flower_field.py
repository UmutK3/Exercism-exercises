
def annotate(garden):

    if any(len(garden[i]) != len(garden[i + 1]) for i in range(len(garden)- 1)):
        raise ValueError("The board is invalid with current input.")
    result = []

    for r_index,row in enumerate(garden):
        row_result = []
        for c_index,c in enumerate(row):
            if c != " " and c != "*":
                raise ValueError("The board is invalid with current input.")
            count = 0
            if c  == "*":
                row_result.append("*")
                continue
            top_row = garden[r_index - 1] if r_index != 0 else []
            bottom_row = garden[r_index + 1] if r_index != len(garden) - 1 else []  
        
            start = c_index -1 if c_index != 0 else c_index
            end = c_index + 2 if c_index != (len(row) - 1) else c_index + 1

            for x in range(start,end):
                if top_row and top_row[x] == "*":
                    count += 1
                if bottom_row  and bottom_row[x] == "*":
                    count += 1
                if row[x] == "*":
                    count += 1

            if count == 0:
                row_result.append(" ")
                continue
            row_result.append(str(count))
        result.append("".join(row_result))
    return result