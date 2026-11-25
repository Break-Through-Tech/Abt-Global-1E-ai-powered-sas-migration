"""Syntax & semantics agent: checks a translated Python program against its SAS source."""

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from .. import config, prompts

# Gemini finish reasons that mean the response is unusable.
_BLOCKED = {"SAFETY", "RECITATION", "BLOCKLIST", "PROHIBITED_CONTENT", "SPII"}


def build_llm() -> BaseChatModel:
    # GOOGLE_API_KEY is read from the environment, which config.py fills from .env.
    return init_chat_model(config.MODEL, timeout=900)


def _ask(llm: BaseChatModel, prompt: str) -> str:
    response = llm.invoke([SystemMessage(prompts.SYSTEM), HumanMessage(prompt)])
    finish_reason = response.response_metadata.get("finish_reason")
    if finish_reason in _BLOCKED:
        raise RuntimeError(f"Model blocked the response (finish_reason={finish_reason})")
    if finish_reason == "MAX_TOKENS":
        raise RuntimeError("Model hit its output token limit; the response is truncated.")
    return response.text


def check_program(program_id: str, llm: BaseChatModel | None = None) -> str:
    """Compare program_id's SAS source with its translated Python and save a report."""
    llm = llm or build_llm()
    program = config.get_program(program_id)

    out_dir = config.MIGRATED_DIR / program_id
    python_path = out_dir / f"{program_id}.py"
    if not python_path.exists():
        raise FileNotFoundError(f"No translated code at {python_path}; run the translation first.")

    prompt = prompts.fill(
        prompts.SYNTAX_SEMANTICS,
        sas_file=program.sas_file,
        sas_code=program.path.read_text(errors="replace"),
        macros=config.MACROS_FILE.read_text(errors="replace"),
        python_code=python_path.read_text(),
    )

    report = _ask(llm, prompt)
    (out_dir / "syntax_semantics_report.md").write_text(report)
    return report