def fair_sharer(values, num_iterations, share=0.1):

   
    # code
    for i in range(num_iterations):
        
        #print(values)
        share_value = max(values) * share
        new_max_value = max(values) - (share_value * 2)

        max_value_idx = values.index(max(values))

        left_neighbor = values[max_value_idx - 1] + share_value
        right_neighbor = values[max_value_idx + 1] + share_value
        #print(left_neighbor)
        #print(right_neighbor)
        values[max_value_idx - 1] = left_neighbor #Update value for left neighbor of the highest value 
        values[max_value_idx + 1] = right_neighbor #Update value for right neighbor of the highest value
        values[max_value_idx] = new_max_value
        
    return print(values)

fair_sharer([0, 1000, 800, 0], 1) # [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2) # [100, 890, 720, 90]
