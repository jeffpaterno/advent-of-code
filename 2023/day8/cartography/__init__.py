from typing import Dict


def navigate(instr: str, nodes: Dict[str, Dict[str, str]], start: str = 'AAA', finish: str = 'ZZZ') -> int:
    if not instr or not nodes:
        return 0
    steps = 0
    instr_len = len(instr)
    curr_node = start
    while curr_node != finish:
        left_or_right = 'left' if instr[steps % instr_len] == 'L' else 'right'
        curr_node = nodes[curr_node][left_or_right]
        steps += 1
    return steps
