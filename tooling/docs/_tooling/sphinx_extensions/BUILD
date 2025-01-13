load("@rules_python//python:defs.bzl", "py_library")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("@pip_sphinx//:requirements.bzl", "all_requirements", "requirement")

py_library(
    name = "sphinx_extensions",
    srcs = glob(["sphinx_extensions/**/*.py"]),
    imports = ["."],
    visibility = [
        "//visibility:public",
    ],
    deps = [
        requirement("sphinx"),
        requirement("sphinx-needs"),
        requirement("sphinxcontrib-plantuml"),
    ],
)

compile_pip_requirements(
    name = "requirements",
    src = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)
