"""Agentic SAS-to-Python migration built on LangGraph."""
"""Agentic SAS-to-Python migration built on LangGraph."""
from .config import PROGRAMS, SasProgram, get_program
from .graph import MigrationState, build_graph

def migrate_program(
    program_id: str,
    prior_code: dict[str, str] | None = None,
) -> dict:
    """Analyze, translate, and save a SAS program.

    Args:
        program_id: ID of the SAS program to migrate.
        prior_code: Previously translated Python programs.

    Returns:
        Final LangGraph state containing the analysis,
        translated code, and output directory.
    """
    graph = build_graph()

    initial_state: MigrationState = {
        "program_id": program_id,
        "prior_code": prior_code or {},
    }

    return graph.invoke(initial_state)


def migrate_all() -> dict[str, dict]:
    """Migrate all registered SAS programs in pipeline order.

    Passes previously translated programs to subsequent
    migrations so they can reference earlier code.
    """
    results = {}
    prior_code = {}

    for program in PROGRAMS:
        result = migrate_program(
            program_id=program.id,
            prior_code=prior_code,
        )

        results[program.id] = result
        prior_code[program.id] = result["code"]

    return results


__all__ = [
    "PROGRAMS",
    "SasProgram",
    "get_program",
    "MigrationState",
    "build_graph",
    "migrate_program",
    "migrate_all",
]
