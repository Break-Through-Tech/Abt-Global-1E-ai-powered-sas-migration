import sys

from .syntax_semantics_agent import check_program

program_id = sys.argv[1] if len(sys.argv) > 1 else "program1"
print(check_program(program_id))