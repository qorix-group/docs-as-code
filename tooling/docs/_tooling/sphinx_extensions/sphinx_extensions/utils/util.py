from sphinx.util.logging import SphinxLoggerAdapter
from sphinx_needs.data import NeedsInfoType

#######################################################################################
#                       CUSTOM REUSABLE FUNCTIONS
#######################################################################################

prologPath = "docs/_extensions/prolog.inc"
try:
    with open(prologPath, "r") as prologFile:
        # +1 is needed as the insert in the RST file a newline at the end.
        rst_prolog_length = len(prologFile.readlines()) + 1
except Exception as ex:
    print("[ERROR:] While reading '{0!s}'.".format(prologPath))
    print(ex)
    rst_prolog_length = 0


def check_option(
    need: NeedsInfoType,
    option: str,
    log: SphinxLoggerAdapter,
    allowed_values: list[str | int | bool] = None,
    allow_empty: bool = False,
    msg: str = "",
) -> bool:
    empty_values = [[], "", None]

    # Check if option exists in need
    if option not in need:
        if msg == "":
            msg = f'Need: {need["id"]} is missing required option: `{option}`.'
        log_custom_warning(need, log, msg)
        return True

    if need[option] in empty_values and not allow_empty:
        if msg == "":
            msg = f'Need: {need["id"]} is missing required option: `{option}`.'
        log_custom_warning(need, log, msg)
        return True

    if allowed_values:
        if need[option] not in allowed_values:
            if msg == "":
                msg = f'Need: {need["id"]} has `{option}` option wrongly set. Got: `{need[option]}` wanted one of: `{allowed_values}`\n'
            log_custom_warning(need, log, msg)
            return True
    return False


def log_custom_warning(need: NeedsInfoType, log: SphinxLoggerAdapter, msg: str):
    if need["lineno"] is not None and need["docname"] is not None:
        linenr_fixed = f"{int(need['lineno']) - rst_prolog_length}"
        location = f"{need['docname']}.rst:{linenr_fixed}"
    else:
        location = None
    # Note: passing the location as a string allows us to use readable relative paths,
    # passing as a tuple results in absolute paths to ~/.cache/.../bazel-out/..
    log.warning(msg, location=location)
