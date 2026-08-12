def hanoi_solver(total_disks):
    rod_source = []
    rod_aux = []
    rod_target = []
    history = []
    
    for d in range(total_disks, 0, -1):
        rod_source.append(d)
        
    def add_to_history():
        history.append(f'{rod_source} {rod_aux} {rod_target}')
        
    add_to_history()
    
    def move_disk(n, source, aux, target):
        if n == 1:
            moved_disk = source.pop()
            target.append(moved_disk)
            add_to_history()
        else:
            move_disk(n - 1, source, target, aux)
            moved_disk = source.pop()
            target.append(moved_disk)
            add_to_history()
            move_disk(n - 1, aux, source, target)
            
    move_disk(total_disks, rod_source, rod_aux, rod_target)
    
    return '\n'.join(history)
print(hanoi_solver(20))