# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************
load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@pip_process//:requirements.bzl", "all_requirements")
load("@score_python_basics//:defs.bzl", "score_py_pytest")

py_library(
    name = "score_header_service",
    srcs = glob(
        ["*.py"],
        exclude = ["test/**"],
    ),
    imports = ["."],
    visibility = ["//visibility:public"],
    # TODO: Figure out if all requirements are needed or if we can break it down a bit
    deps = all_requirements,
)

score_py_pytest(
    name = "score_header_service_test",
    size = "small",
    srcs = glob(["test/**/*.py"]),
    # All requirements already in the library so no need to have it double
    deps = [":score_header_service"],
)
